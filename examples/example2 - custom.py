import sys
sys.path.append("/home/ted/github_repos/tls-client-python")
from rich import pretty, print
pretty.install()
import tls_client

# You can find more details about the arguments in `session.py` e.g. what 1, 2, 3, 4 etc. represents in h2_settings
session = tls_client.Session()
session.proxy = "http://localhost:8083"
res = session.get(
    "https://httpbin.org/cookies/set/a/b",
    headers={
        "key1": "value1",
    },
    verify=False,
    with_custom_cookie_jar=True
)
print(res.text)
print(session.cookies)
r = session.get_cookies_from_session("")
print(r)
session.cookies.pop("a")
session.add_cookies_to_session("https://httpbin.org/", [{'expires': 0, 'domain': '', 'name': 'a', 'path': '/', 'value': 'bb', 'maxAge': -1, 'secure': False, 'httpOnly': False}])
print(session.get_cookies_from_session(""))
print(session.get("https://httpbin.org/cookies", verify=False))
