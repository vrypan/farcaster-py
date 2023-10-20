import os
from dotenv import load_dotenv
from farcaster.Signer import Signer

load_dotenv()
op_eth_provider	= os.getenv("OP_ETH_PROVIDER") # "Your OP ETH provider endpoint"
user_fid 		= os.getenv("USER_FID") # "User fid that will approve the signer"
user_key 		= os.getenv("USER_PRIVATE_KEY") # "User's private key."
app_fid 		= os.getenv("APP_FID") # "Application fid that will issue the signer."
app_key 		= os.getenv("APP_PRIVATE_KEY") # "Application's private key"

"""
- If you just want a signer to post for yourself (i.e., no app),
you can set app_fid=user_fid and app_key=user_key.

- If you don't know your (user or application) private keys, see:
https://eth-account.readthedocs.io/en/stable/eth_account.html#eth_account.account.Account.from_mnemonic

Example:
>>> from eth_account import Account
>>> Account.enable_unaudited_hdwallet_features()
>>> acct = Account.from_mnemonic("your secret phrase here")
>>> acct.address
"""

s = Signer( op_eth_provider, int(user_fid), user_key, int(app_fid), app_key )


tx_hash = s.approve_signer()
signer_private_key = s.key
signer_public_key = s.signer_pub()

print(f"=== New Signer approved.")
print(f"Tx: {tx_hash}")
print(f"User Fid: {user_fid}")
print(f"App Fid: {user_fid}")
print(f"Signer private key: {s.key.hex()}")
print(f"Signer public key: {s.signer_pub().hex()}")