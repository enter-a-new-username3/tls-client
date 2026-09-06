import sys
sys.path.append("/home/ted/github_repos/tls-client-python")

import tls_client

# You can find more details about the arguments in `session.py` e.g. what 1, 2, 3, 4 etc. represents in h2_settings
session = tls_client.Session(
    client_identifier=None,
    ja3_string="771,4865-4867-4866-49195-49199-52393-52392-49196-49200-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-34-18-51-43-13-45-28-27-65037,4588-29-23-24-25-256-257,0",
    h2_settings={
        "HEADER_TABLE_SIZE": 65536,
        "ENABLE_PUSH": 0,
        "INITIAL_WINDOW_SIZE": 131072,
        "MAX_FRAME_SIZE": 16384
    },
    h2_settings_order=[
        "HEADER_TABLE_SIZE",
        "ENABLE_PUSH",
        "INITIAL_WINDOW_SIZE",
        "MAX_FRAME_SIZE"
    ],
    supported_signature_algorithms=[
        "ECDSAWithP256AndSHA256",
        "ECDSAWithP384AndSHA384",
        "ECDSAWithP521AndSHA512",
        "PSSWithSHA256",
		"PSSWithSHA384",
		"PSSWithSHA512",
		"PKCS1WithSHA256",
		"PKCS1WithSHA384",
		"PKCS1WithSHA512",
		"ECDSAWithSHA1",
		"PKCS1WithSHA1"
    ],
    supported_versions=["1.3", "1.2"],
    key_share_curves=["X25519MLKEM768", "X25519", "P256"],
    cert_compression_algos=["zlib", "brotli", "zstd"],
    pseudo_header_order=[
        ":method",
        ":authority",
        ":scheme",
        ":path"
    ],
    connection_flow=15663105
)

res = session.post(
    "https://tls.peet.ws/api/all",
    headers={
        "key1": "value1",
    },
    json={
        "key1": "key2"
    },
    verify=False
)