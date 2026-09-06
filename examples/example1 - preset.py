import json
import sys,os
import uuid
sys.path.append("/home/ted/github_repos/tls-client-python")
import tls_client

from rich import print

session = tls_client.Session(
    client_identifier="firefox_147",
    random_tls_extension_order=False
)

res = session.get(
    "https://www.rivalo.bet.br/api/offer/v3/categories?sport=Football",
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br, zstd",
        "referer": "https://www.rivalo.bet.br/pt/sportsbook",
        "credentials": "include",
        "x-correlation-id": str(uuid.uuid4()),
        "x-request-id": str(uuid.uuid4()),
        "x-betr-operator": "matchserv",
        "x-betr-brand": "rivalo.bet.br",
        "x-locale": "en",
        "x-session-id": str(uuid.uuid4()),
        "sec-gpc": "1",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "priority": "u=4",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "te": "trailers",
    },
    proxy="a:a@localhost:8083",
    verify=False
)
