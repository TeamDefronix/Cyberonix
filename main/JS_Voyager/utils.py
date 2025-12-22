import math
from urllib.parse import urlparse


def calculate_entropy(data: str) -> float:
    """Shannon entropy calculator (detect high-entropy strings)."""
    if not data:
        return 0
    entropy = 0
    for x in set(data):
        p_x = float(data.count(x)) / len(data)
        entropy -= p_x * math.log(p_x, 2)
    return entropy


def normalize_domain(url: str) -> str:
    """Extract domain name to create folder names."""
    try:
        parsed = urlparse(url)
        return parsed.netloc.replace(":", "_").replace(".", "_")
    except:
        return "unknown_domain"
