import requests


def get_html(url, method):
    try:
        result = getattr(requests, method)(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False
