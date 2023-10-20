import os
from dotenv import load_dotenv
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import SignatureScheme, HashScheme, Embed
from farcaster import Message

load_dotenv()
# Make sure you check .env.sample to create .env
hub_address	= os.getenv("FARCASTER_HUB")
app_signer = os.getenv("APP_SIGNER_KEY")
user_fid = int( os.getenv("USER_FID") )


# Scenario:
# - user_fid has approved app_signer.
# - message with message_hash has been posted by user_fid
# - we will use the signer to delete the cast


hub = HubService(hub_address, use_async=False)
message_builder = Message.MessageBuilder(
	HashScheme.HASH_SCHEME_BLAKE3, 
	SignatureScheme.SIGNATURE_SCHEME_ED25519, 
	bytes.fromhex(app_signer[2:])
)

# replace the hash with the actual message hash.
message_hash = "0x3baaaa16eb549203b0e0ae8e67b47728c8bfaf70" 

message_data = message_builder.cast.remove(fid=user_fid, target_hash=message_hash)
message = message_builder.message(message_data)
ret = hub.SubmitMessage(message)
print(ret)
