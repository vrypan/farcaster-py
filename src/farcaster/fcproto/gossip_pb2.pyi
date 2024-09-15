from . import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GossipVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    GOSSIP_VERSION_V1: _ClassVar[GossipVersion]
    GOSSIP_VERSION_V1_1: _ClassVar[GossipVersion]
GOSSIP_VERSION_V1: GossipVersion
GOSSIP_VERSION_V1_1: GossipVersion

class GossipAddressInfo(_message.Message):
    __slots__ = ["address", "family", "port", "dns_name"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DNS_NAME_FIELD_NUMBER: _ClassVar[int]
    address: str
    family: int
    port: int
    dns_name: str
    def __init__(self, address: _Optional[str] = ..., family: _Optional[int] = ..., port: _Optional[int] = ..., dns_name: _Optional[str] = ...) -> None: ...

class ContactInfoContentBody(_message.Message):
    __slots__ = ["gossip_address", "rpc_address", "excluded_hashes", "count", "hub_version", "network", "app_version", "timestamp"]
    GOSSIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_HASHES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HUB_VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    gossip_address: GossipAddressInfo
    rpc_address: GossipAddressInfo
    excluded_hashes: _containers.RepeatedScalarFieldContainer[str]
    count: int
    hub_version: str
    network: _message_pb2.FarcasterNetwork
    app_version: str
    timestamp: int
    def __init__(self, gossip_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., rpc_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., excluded_hashes: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ..., hub_version: _Optional[str] = ..., network: _Optional[_Union[_message_pb2.FarcasterNetwork, str]] = ..., app_version: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ContactInfoContent(_message.Message):
    __slots__ = ["gossip_address", "rpc_address", "excluded_hashes", "count", "hub_version", "network", "app_version", "timestamp", "body", "signature", "signer", "data_bytes"]
    GOSSIP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RPC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_HASHES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HUB_VERSION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    DATA_BYTES_FIELD_NUMBER: _ClassVar[int]
    gossip_address: GossipAddressInfo
    rpc_address: GossipAddressInfo
    excluded_hashes: _containers.RepeatedScalarFieldContainer[str]
    count: int
    hub_version: str
    network: _message_pb2.FarcasterNetwork
    app_version: str
    timestamp: int
    body: ContactInfoContentBody
    signature: bytes
    signer: bytes
    data_bytes: bytes
    def __init__(self, gossip_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., rpc_address: _Optional[_Union[GossipAddressInfo, _Mapping]] = ..., excluded_hashes: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ..., hub_version: _Optional[str] = ..., network: _Optional[_Union[_message_pb2.FarcasterNetwork, str]] = ..., app_version: _Optional[str] = ..., timestamp: _Optional[int] = ..., body: _Optional[_Union[ContactInfoContentBody, _Mapping]] = ..., signature: _Optional[bytes] = ..., signer: _Optional[bytes] = ..., data_bytes: _Optional[bytes] = ...) -> None: ...

class PingMessageBody(_message.Message):
    __slots__ = ["ping_origin_peer_id", "ping_timestamp"]
    PING_ORIGIN_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    PING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ping_origin_peer_id: bytes
    ping_timestamp: int
    def __init__(self, ping_origin_peer_id: _Optional[bytes] = ..., ping_timestamp: _Optional[int] = ...) -> None: ...

class AckMessageBody(_message.Message):
    __slots__ = ["ping_origin_peer_id", "ack_origin_peer_id", "ping_timestamp", "ack_timestamp"]
    PING_ORIGIN_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    ACK_ORIGIN_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    PING_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ping_origin_peer_id: bytes
    ack_origin_peer_id: bytes
    ping_timestamp: int
    ack_timestamp: int
    def __init__(self, ping_origin_peer_id: _Optional[bytes] = ..., ack_origin_peer_id: _Optional[bytes] = ..., ping_timestamp: _Optional[int] = ..., ack_timestamp: _Optional[int] = ...) -> None: ...

class NetworkLatencyMessage(_message.Message):
    __slots__ = ["ping_message", "ack_message"]
    PING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ping_message: PingMessageBody
    ack_message: AckMessageBody
    def __init__(self, ping_message: _Optional[_Union[PingMessageBody, _Mapping]] = ..., ack_message: _Optional[_Union[AckMessageBody, _Mapping]] = ...) -> None: ...

class MessageBundle(_message.Message):
    __slots__ = ["hash", "messages"]
    HASH_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    hash: bytes
    messages: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    def __init__(self, hash: _Optional[bytes] = ..., messages: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class GossipMessage(_message.Message):
    __slots__ = ["message", "contact_info_content", "network_latency_message", "message_bundle", "topics", "peer_id", "version", "timestamp"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_CONTENT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LATENCY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: _message_pb2.Message
    contact_info_content: ContactInfoContent
    network_latency_message: NetworkLatencyMessage
    message_bundle: MessageBundle
    topics: _containers.RepeatedScalarFieldContainer[str]
    peer_id: bytes
    version: GossipVersion
    timestamp: int
    def __init__(self, message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., contact_info_content: _Optional[_Union[ContactInfoContent, _Mapping]] = ..., network_latency_message: _Optional[_Union[NetworkLatencyMessage, _Mapping]] = ..., message_bundle: _Optional[_Union[MessageBundle, _Mapping]] = ..., topics: _Optional[_Iterable[str]] = ..., peer_id: _Optional[bytes] = ..., version: _Optional[_Union[GossipVersion, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...
