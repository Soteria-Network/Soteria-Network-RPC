import json
from soteriarpc import Soteria

soteria = Soteria('soteria', 'SOTERIA_pass01')
blockchaininfo = soteria.getblockchaininfo()
print(json.dumps(blockchaininfo, indent=4))
print("\nThis was a successful test of the SOTERIA Python RPC Daemon Bridge")
