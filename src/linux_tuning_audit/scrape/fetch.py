# scrape/fetch.py

import requests


def fetch_url(url: str) -> str:
    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "linux-tuning-audit/0.1"
        }
    )

    response.raise_for_status()

    return response.text
