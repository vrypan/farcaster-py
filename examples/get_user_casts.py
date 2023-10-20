import os
import sys
from dotenv import load_dotenv
from farcaster.HubService import HubService

load_dotenv()
hub_address	= os.getenv("FARCASTER_HUB")
if not hub_address:
	print("No hub address. Check .env.sample")
	sys.exit(1)

hub = HubService(hub_address, use_async=False)
casts = hub.GetCastsByFid(fid=280)
for cast in casts.messages:
	print(cast)
