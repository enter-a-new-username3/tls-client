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

