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

hub = HubService(hub_address, use_async=False)
message_builder = Message.MessageBuilder(
	HashScheme.HASH_SCHEME_BLAKE3, 
	SignatureScheme.SIGNATURE_SCHEME_ED25519, 
	bytes.fromhex(app_signer[2:])
)

# add(self, fid, text, mentions=[], mentions_positions=[], embeds=[]) -> MessageData:
data = message_builder.cast.add(
	fid = user_fid, 
	text = "My first post using farcaster-py.\ncc .", 
	mentions = [280], 
	mentions_positions = [37],
	embeds = [ Embed(url='https://github.com/vrypan/farcaster-py')])
msg  = message_builder.message(data)

ret  = hub.SubmitMessage(msg)
print("Message posted!")
# print(ret)

data = message_builder.cast.add(
	fid = user_fid, 
	text = "One more message from farcaster-py." 
	)
msg  = message_builder.message(data)

ret  = hub.SubmitMessage(msg)
print("Second message posted, too!")
# print(ret)