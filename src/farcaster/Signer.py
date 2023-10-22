# This is a very first take on a 
from eth_account import Account
from eth_account.messages import encode_structured_data
import time

from web3 import Web3
import json
from nacl.signing import SigningKey
from pkg_resources import resource_string

SIGNED_KEY_REQUEST_METADATA_ABI = json.loads(
    resource_string(__name__, "abi/SignedKeyRequestMetadataABI.json")
)

KEY_REGISTRY_ABI = json.loads(
    resource_string(__name__, "abi/KeyRegistryABI.json")
)

SIGNED_KEY_REQUEST_VALIDATOR_EIP_712_DOMAIN = {
  'name': "Farcaster SignedKeyRequestValidator",
  'version': "1",
  'chainId': 10, # OP Mainnet
  'verifyingContract': "0x00000000fc700472606ed4fa22623acf62c60553",
} 

SIGNED_KEY_REQUEST_TYPE = [
  { 'name': "requestFid", 'type': "uint256" },
  { 'name': "key", 'type': "bytes" },
  { 'name': "deadline", 'type': "uint256" },
]

class Signer:
    def __init__(self, op_eth_provider, account_fid, account_key, app_fid, app_key):
        self.account_fid = account_fid
        self.account = Account.from_key(account_key)
        self.app_fid = app_fid
        self.app = Account.from_key(app_key)

        self.signer = Account.create()
        self.signer25519 = SigningKey(self.signer.key)
        self.key = self.signer.key

        self.w3 = Web3(Web3.HTTPProvider(op_eth_provider))
        self.w3.eth.default_account = self.account.address

    def signer_pub(self):
        return self.signer25519.verify_key.encode()
    
    def _signed_params(self):
        deadline = int( time.time() + 60 * 60 ) # 1 hour from now. FC_TIME?
        signer_public_key = self.signer_pub()
        data = {
            'domain': SIGNED_KEY_REQUEST_VALIDATOR_EIP_712_DOMAIN,
            'types': {
                'SignedKeyRequest': SIGNED_KEY_REQUEST_TYPE,
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                    {"name": "verifyingContract", "type": "address"}
                ],
            },
            'message': {
                'requestFid': self.app_fid,
                'key': signer_public_key,
                'deadline': deadline,
            },
            'primaryType': "SignedKeyRequest",
        }
        structured_msg = encode_structured_data(data)
        signed_data = self.app.sign_message(structured_msg)
        SignedKeyRequestMetadata = self.w3.eth.contract(abi=SIGNED_KEY_REQUEST_METADATA_ABI)
        signed_call = SignedKeyRequestMetadata.encodeABI("encodeMetadata", args=[(
            self.app_fid,  
            Web3.to_checksum_address(self.app.address), 
            signed_data['signature'], 
            deadline)
        ])
        return "0x" + signed_call[10:]
    
    def approve_signer(self) -> str: # Returns transaction hash
        KeyRegistry = self.w3.eth.contract(
            address=Web3.to_checksum_address("0x00000000fc9e66f1c6d86d750b4af47ff0cc343d"), #KeyRegistry address 
            abi=KEY_REGISTRY_ABI)

        params = self._signed_params()
        prepare_tx = KeyRegistry.functions.add(1, self.signer_pub(), 1, self._signed_params()).build_transaction({
            "from": self.account.address,
            "nonce": self.w3.eth.get_transaction_count(self.account.address),
        })
        
        signed_tx = self.w3.eth.account.sign_transaction(prepare_tx, private_key=self.account.key)


        # Send the raw transaction:
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_hash.hex()

def removeSigner(op_eth_provider:str, user_key: str, signer_pub_key: str) -> str:
    account = Account.from_key(user_key)
    KEY_REGISTRY_ABI = json.loads(
        resource_string(__name__, "abi/KeyRegistryABI.json")
    )
    w3 = Web3(Web3.HTTPProvider(op_eth_provider))
    KeyRegistry = w3.eth.contract(
        address=Web3.to_checksum_address("0x00000000fc9e66f1c6d86d750b4af47ff0cc343d"),
        abi=KEY_REGISTRY_ABI
    )
    prepare_tx = KeyRegistry.functions.remove(bytes.fromhex(signer_pub_key[2:])).build_transaction({
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
    })

    signed_tx = w3.eth.account.sign_transaction(prepare_tx, private_key=account.key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    return f"{tx_hash.hex()}"


