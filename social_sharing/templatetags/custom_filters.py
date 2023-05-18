from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc
