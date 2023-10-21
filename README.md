# farcaster-py
Python bindings for [Farcaster](https://farcaster.xyz).

The bindings are based on the protocol implementation by [Hubble](https://thehubble.xyz) which can be found at [@farcaster/hub-monorepo](https://github.com/farcasterxyz/hub-monorepo/).

This is stil **work in progress**. Do not rely on this code for production purposes.

# Quick start

Until there is a proper pipy package, a quick and easy way to play around:

1. `pip install farcaster-py`
2. Create `.env` with the following entries:
```
FARCASTER_HUB="farcaster_hub:grpc_port"

OP_ETH_PROVIDER="OP provider endpoint"

APP_FID="application fid"
APP_PRIVATE_KEY="application private key"

USER_FID="User fid"
USER_PRIVATE_KEY="User private key" 
APP_SIGNER_KEY="You have to create a signer first. Use examples/approve_new_signer.py." 
```
3. Download the examples found in `examples/` and try `python ./get_user_casts.py`

# Internals

I have tried to both follow Farcaster's conventions and naming, but also provide a pythonic API that make sense to use without requiring deep knowledge of the underlying protocols.

## HubServce
The `HubService` class uses Hubble's gRPC interface to interact with hubs. Most of the gRPC described in [the protocol specification](https://github.com/farcasterxyz/protocol/blob/main/docs/SPECIFICATION.md) is avalable through farcaster-py.

Example:

```python
from farcaster.HubService import HubService
hub = HubService(hub_address, use_async=False)
casts = hub.GetCastsByFid(fid=280)
for cast in casts.messages:
	print(cast)
```

- Secure connections have not been implemented.
- 99% of the gRPC API is read-only: You get data from the hubs. The only (I think) call that allows you to change the global state is `HubService.SubmitMessage(Message) -> Message`. (see next section)

## Message

The `Message.MessageBuilder` class offers three types of methods:
- The initializer that creates a new `MessageBuilder` with specific characteristics (hash scheme, signature scheme and the user's private key)
- Methods like `MessageBuilder.link.add(...)` and `Message.link.remove(...)` that return a `MessageData` protobuf.
- `MessageBuilder.message(self, data: MessageData)` that gets `MessageData` and hashes, signs, etc and returns a `Message` protobuf object ready to be used by `HubService.SubmitMessage(Message)`

Example:

```python
from farcaster.HubService import HubService
from farcaster.fcproto.message_pb2 import SignatureScheme, HashScheme, Embed
from farcaster import Message

hub_address	= '....'
app_signer = '....'
user_fid = '....'

hub = HubService(hub_address, use_async=False)
message_builder = Message.MessageBuilder(
	HashScheme.HASH_SCHEME_BLAKE3, 
	SignatureScheme.SIGNATURE_SCHEME_ED25519, 
	bytes.fromhex(app_signer[2:])
)
data = message_builder.cast.add(
	fid = user_fid, 
	text = "Hello, world!" 
	)
msg  = message_builder.message(data)
ret  = hub.SubmitMessage(msg)
```

## Signer
The `Signer` class provides a simple interface to creating signers.

To create a signer, you need:
1. Fid and corresponding private key of the user that will approve the signer.
2. The fid and private key of the application that will create and use the signer.

Once you have this data, you create a new `Signer`, and use `approve_signer()` to submit the on-chain tx:
```python
# snippet from examples/approve_new_signer.py
s = Signer( op_eth_provider, user_fid, user_key, app_fid, app_key )
tx_hash = s.approve_signer()
signer_private_key = s.key
signer_public_key = s.signer_pub()
```

## Updating protobuf shemas

If you are installing from source, you use `generate_proto.sh <HUBBLE VERSION>`
to generate the corresponding protbuffer Python code.


```bash
./generate_proto.sh 1.5.6                                                                                                                                                                                  git:main*
x schemas/
x schemas/gossip.proto
x schemas/hub_event.proto
x schemas/hub_state.proto
x schemas/job.proto
x schemas/message.proto
x schemas/onchain_event.proto
x schemas/request_response.proto
x schemas/rpc.proto
x schemas/sync_trie.proto
x schemas/username_proof.proto

Protobuf schemas parsed.
```

# Versioning

Eventually, farcaster-py will follow the version numbers of farcaster protocol buffers (when/if they become a separate package).

Until then, I'll keep version numbers low (0.0.x) and update them manually.

# License
`farcaster-py` is distributed under the [MIT License](LICENSE).

# Credits

This package was created and is maintained by [@vrypan.eth](https://warpcast.com/vrypan.eth).

An older repository, called [hub_py](https://github.com/mirceapasoi/hub_py) has been a valuable source while building the initial version of `farcaster-py`.