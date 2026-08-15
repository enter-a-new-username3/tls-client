import json
import sys,os
sys.path.append("/home/ted/github_repos/tls-client-python")
import tls_client

from rich import print

session = tls_client.Session(
    client_identifier="chrome_150",
    random_tls_extension_order=False
)

res = session.get(
    "https://tls.peet.ws/api/tls",
    headers={
        "key1": "value1",
    },
    proxy="a:a@localhost:8083",
    verify=False
).json()
