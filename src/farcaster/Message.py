from blake3 import blake3
from nacl.signing import SigningKey
from eth_account import Account
from eth_keys import keys
from eth_account.messages import encode_structured_data
from . fcproto.message_pb2 import (
    SignatureScheme, HashScheme, MessageData
    )
from . fcproto.message_pb2 import Message as Message_pb2

from . import MessageData

class MessageBuilder:
    def __init__(self, hash_scheme, signature_scheme, signer_key):
        self.hash_scheme = hash_scheme
        self.signature_scheme = signature_scheme
        if self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_ED25519:
            self.signer = SigningKey(signer_key)
        elif self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_EIP712:
            self.signer = Account.from_key(signer_key)
        else:
            raise Exception(f"Signature scheme {self.signature_scheme} not implemented.")
        self.link = MessageData.Link()
        self.cast = MessageData.Cast()
        self.reaction_to_cast = MessageData.ReactionToCast()
        self.reaction_to_url = MessageData.ReactionToUrl()
        self.user_data = MessageData.UserData()
        
    def sign25519(self, hash: bytes) -> bytes:
        return self.signer.sign(hash).signature

    def sign712(self, hash: bytes) -> bytes:
        eip712_schema = {
            "types": {
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "salt", "type": "bytes32"},
                ],
                "MessageData": [
                    {"name": "hash", "type": "bytes"},
                ],
            },
            "domain": {
                "name": "Farcaster Verify Ethereum Address",
                "version": "2.0.0",
                # fixed salt to minimize collisions, should be the same as
                # packages/core/src/crypto/eip712.ts in @farcaster/hub-monorepo
                "salt": bytes.fromhex(
                    "f2d857f4a3edcb9b78b4d503bfe733db1e3f6cdc2b7971ee739626c97e86a558"
                ),
            },
            "primaryType": "MessageData",
            "message": {
                "hash": hash,
            },
        }
        encoded_message = encode_structured_data(eip712_schema)
        signature = self.signer.sign_message(encoded_message)
        return bytes(signature.signature)

    def signer_pub_key(self) -> bytes:
        if self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_ED25519:
            return self.signer.verify_key.encode()
        elif self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_EIP712:
            return keys.PrivateKey(self.signer.key).public_key.to_bytes()
        else:
            raise Exception(f"Signature scheme {self.signature_scheme} not implemented.")
    
    def hash(self, s) -> str:
        if self.hash_scheme == HashScheme.HASH_SCHEME_BLAKE3:
            return blake3(s).digest(length=20)
        else:
            raise Exception(f"Hash scheme {self.hash_scheme} not implemented.")

    def sign(self, hash:bytes) -> bytes:
        if self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_ED25519:
            return self.sign25519(hash)
        elif self.signature_scheme == SignatureScheme.SIGNATURE_SCHEME_EIP712:
            return self.sign712(hash)
        else:
            raise Exception(f"Signature scheme {self.signature_scheme} not implemented.")

    def message(self, data: MessageData) -> Message_pb2:
        data_serialized = data.SerializeToString()
        #data_serialized = patched_serialize_to_string(data)
        msg_hash = self.hash(data_serialized)
        msg_signature = self.sign(msg_hash)
        
        return Message_pb2(
            data = data,
            hash = msg_hash,
            hash_scheme = self.hash_scheme,
            signature = msg_signature,
            signature_scheme = self.signature_scheme,
            signer = self.signer_pub_key(),
            data_bytes = data_serialized
        )
