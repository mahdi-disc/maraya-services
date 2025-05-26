import requests

def get_subdomains(domain):
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return []
        data = r.json()
        subdomains = set()
        for item in data:
            name = item.get("name_value", "")
            for sub in name.split("\n"):
                sub = sub.strip().lower()
                if sub.endswith(f".{domain}"):
                    subdomains.add(sub)
        return list(subdomains)
    except Exception as e:
        return [f"Error: {str(e)}"]

def crawl_real_subdomains(domains):
    all_subdomains = {}

    for domain in domains:
        subs = get_subdomains(domain)
        all_subdomains[domain] = subs

    result = {
        "stage": "domain_asset_discovery",
        "inputs": {
            "domains": domains
        },
        "discovered": {
            "subdomains": all_subdomains
        }
    }

    return result
