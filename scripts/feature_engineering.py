import re
import socket
import ssl
import whois
from urllib.parse import urlparse
from datetime import datetime
import requests

def extract_features(url):
    features = {}

    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""

    # 1–23: Basic structural & symbol features
    features['length_url'] = len(url)
    features['length_hostname'] = len(hostname)
    features['ip'] = 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', hostname) else 0
    features['nb_dots'] = url.count('.')
    features['nb_hyphens'] = url.count('-')
    features['nb_at'] = url.count('@')
    features['nb_qm'] = url.count('?')
    features['nb_and'] = url.count('&')
    features['nb_or'] = url.count('|')
    features['nb_eq'] = url.count('=')
    features['nb_underscore'] = url.count('_')
    features['nb_tilde'] = url.count('~')
    features['nb_percent'] = url.count('%')
    features['nb_slash'] = url.count('/')
    features['nb_star'] = url.count('*')
    features['nb_colon'] = url.count(':')
    features['nb_comma'] = url.count(',')
    features['nb_semicolumn'] = url.count(';')
    features['nb_dollar'] = url.count('$')
    features['nb_space'] = url.count(' ')
    features['nb_www'] = url.count('www')
    features['nb_com'] = url.count('.com')
    features['nb_dslash'] = url.count('//')

    # 24–35: Tokens and structure
    features['http_in_path'] = int('http' in path)
    features['https_token'] = int('https' in path)
    features['ratio_digits_url'] = sum(c.isdigit() for c in url) / len(url)
    features['ratio_digits_host'] = sum(c.isdigit() for c in hostname) / len(hostname) if hostname else 0
    features['punycode'] = int('xn--' in url)
    features['port'] = int(bool(parsed.port))
    features['tld_in_path'] = int(any(tld in path for tld in ['.com', '.net', '.org']))
    features['tld_in_subdomain'] = int(any(tld in hostname.split('.')[0] for tld in ['.com', '.net', '.org']) if hostname else 0)
    features['abnormal_subdomain'] = int(len(hostname.split('.')) > 3)
    features['nb_subdomains'] = len(hostname.split('.')) - 2 if hostname else 0
    features['prefix_suffix'] = int('-' in hostname.split('.')[0]) if hostname else 0
    features['random_domain'] = 0  # Needs entropy calculation – skipped
    features['shortening_service'] = int(bool(re.search(r'bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc', url)))

    # 36–50: Path and word stats
    features['path_extension'] = 1 if re.search(r'\.\w{1,4}$', path) else 0
    features['nb_redirection'] = url.count('//') - 1
    features['nb_external_redirection'] = 0  # Placeholder

    # ✅ FIXED THESE LINES WITH RAW STRINGS
    words_raw = re.split(r'\W+', url)
    words_host = re.split(r'\W+', hostname)
    words_path = re.split(r'\W+', path)

    def safe_stats(words):
        lengths = [len(w) for w in words if w]
        return {
            'length_words_raw': sum(lengths),
            'char_repeat': max((url.count(c) for c in set(url)), default=0),
            'shortest_words_raw': min(lengths) if lengths else 0,
            'shortest_word_host': min((len(w) for w in words_host if w), default=0),
            'shortest_word_path': min((len(w) for w in words_path if w), default=0),
            'longest_words_raw': max(lengths) if lengths else 0,
            'longest_word_host': max((len(w) for w in words_host if w), default=0),
            'longest_word_path': max((len(w) for w in words_path if w), default=0),
            'avg_words_raw': sum(lengths) / len(lengths) if lengths else 0,
            'avg_word_host': sum(len(w) for w in words_host) / len(words_host) if words_host else 0,
            'avg_word_path': sum(len(w) for w in words_path) / len(words_path) if words_path else 0,
        }

    stats = safe_stats(words_raw)
    features.update(stats)

    # 51–56: Brand keywords, TLD, etc.
    features['phish_hints'] = int(any(kw in url for kw in ['secure', 'login', 'signin', 'account', 'update', 'banking']))
    features['domain_in_brand'] = 0  # Placeholder
    features['brand_in_subdomain'] = 0  # Placeholder
    features['brand_in_path'] = 0  # Placeholder
    features['suspecious_tld'] = int(any(tld in hostname for tld in ['.zip', '.xyz', '.top', '.club', '.info', '.tk']))
    features['statistical_report'] = 0  # Placeholder

    # 57–65: Hyperlink and redirection behavior (skipped for simplicity)
    for f in ['nb_hyperlinks', 'ratio_intHyperlinks', 'ratio_extHyperlinks', 'ratio_nullHyperlinks', 'nb_extCSS',
              'ratio_intRedirection', 'ratio_extRedirection', 'ratio_intErrors', 'ratio_extErrors']:
        features[f] = 0

    # 66–80: JavaScript behaviors and HTML forms (skipped for simplicity)
    for f in ['login_form', 'external_favicon', 'links_in_tags', 'submit_email', 'ratio_intMedia',
              'ratio_extMedia', 'sfh', 'iframe', 'popup_window', 'safe_anchor', 'onmouseover', 'right_clic',
              'empty_title', 'domain_in_title', 'domain_with_copyright']:
        features[f] = 0

    # 81–87: WHOIS, domain age, rank info (partial implementation)
    try:
        domain_info = whois.whois(hostname)
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        domain_age_days = (datetime.now() - creation_date).days if creation_date else 0
        registration_length_days = (expiration_date - creation_date).days if creation_date and expiration_date else 0

        features['whois_registered_domain'] = 1
        features['domain_registration_length'] = registration_length_days
        features['domain_age'] = domain_age_days
    except:
        features['whois_registered_domain'] = 0
        features['domain_registration_length'] = 0
        features['domain_age'] = 0

    # 84–87: Ranking info
    features['web_traffic'] = 0
    features['dns_record'] = 1 if hostname else 0
    features['google_index'] = int("site:" in url or "cache:" in url)
    features['page_rank'] = 0  # Placeholder

    return features
