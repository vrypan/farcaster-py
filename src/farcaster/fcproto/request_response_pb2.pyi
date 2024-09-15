from . import message_pb2 as _message_pb2
from . import onchain_event_pb2 as _onchain_event_pb2
from . import hub_event_pb2 as _hub_event_pb2
from . import username_proof_pb2 as _username_proof_pb2
from . import gossip_pb2 as _gossip_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STORE_TYPE_NONE: _ClassVar[StoreType]
    STORE_TYPE_CASTS: _ClassVar[StoreType]
    STORE_TYPE_LINKS: _ClassVar[StoreType]
    STORE_TYPE_REACTIONS: _ClassVar[StoreType]
    STORE_TYPE_USER_DATA: _ClassVar[StoreType]
    STORE_TYPE_VERIFICATIONS: _ClassVar[StoreType]
    STORE_TYPE_USERNAME_PROOFS: _ClassVar[StoreType]

class StorageUnitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNIT_TYPE_LEGACY: _ClassVar[StorageUnitType]
    UNIT_TYPE_2024: _ClassVar[StorageUnitType]
STORE_TYPE_NONE: StoreType
STORE_TYPE_CASTS: StoreType
STORE_TYPE_LINKS: StoreType
STORE_TYPE_REACTIONS: StoreType
STORE_TYPE_USER_DATA: StoreType
STORE_TYPE_VERIFICATIONS: StoreType
STORE_TYPE_USERNAME_PROOFS: StoreType
UNIT_TYPE_LEGACY: StorageUnitType
UNIT_TYPE_2024: StorageUnitType

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SubscribeRequest(_message.Message):
    __slots__ = ["event_types", "from_id", "total_shards", "shard_index"]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SHARDS_FIELD_NUMBER: _ClassVar[int]
    SHARD_INDEX_FIELD_NUMBER: _ClassVar[int]
    event_types: _containers.RepeatedScalarFieldContainer[_hub_event_pb2.HubEventType]
    from_id: int
    total_shards: int
    shard_index: int
    def __init__(self, event_types: _Optional[_Iterable[_Union[_hub_event_pb2.HubEventType, str]]] = ..., from_id: _Optional[int] = ..., total_shards: _Optional[int] = ..., shard_index: _Optional[int] = ...) -> None: ...

class EventRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class HubInfoRequest(_message.Message):
    __slots__ = ["db_stats"]
    DB_STATS_FIELD_NUMBER: _ClassVar[int]
    db_stats: bool
    def __init__(self, db_stats: bool = ...) -> None: ...

class HubInfoResponse(_message.Message):
    __slots__ = ["version", "is_syncing", "nickname", "root_hash", "db_stats", "peerId", "hub_operator_fid"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_SYNCING_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    DB_STATS_FIELD_NUMBER: _ClassVar[int]
    PEERID_FIELD_NUMBER: _ClassVar[int]
    HUB_OPERATOR_FID_FIELD_NUMBER: _ClassVar[int]
    version: str
    is_syncing: bool
    nickname: str
    root_hash: str
    db_stats: DbStats
    peerId: str
    hub_operator_fid: int
    def __init__(self, version: _Optional[str] = ..., is_syncing: bool = ..., nickname: _Optional[str] = ..., root_hash: _Optional[str] = ..., db_stats: _Optional[_Union[DbStats, _Mapping]] = ..., peerId: _Optional[str] = ..., hub_operator_fid: _Optional[int] = ...) -> None: ...

class DbStats(_message.Message):
    __slots__ = ["num_messages", "num_fid_events", "num_fname_events", "approx_size"]
    NUM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NUM_FID_EVENTS_FIELD_NUMBER: _ClassVar[int]
    NUM_FNAME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    APPROX_SIZE_FIELD_NUMBER: _ClassVar[int]
    num_messages: int
    num_fid_events: int
    num_fname_events: int
    approx_size: int
    def __init__(self, num_messages: _Optional[int] = ..., num_fid_events: _Optional[int] = ..., num_fname_events: _Optional[int] = ..., approx_size: _Optional[int] = ...) -> None: ...

class SyncStatusRequest(_message.Message):
    __slots__ = ["peerId"]
    PEERID_FIELD_NUMBER: _ClassVar[int]
    peerId: str
    def __init__(self, peerId: _Optional[str] = ...) -> None: ...

class SyncStatusResponse(_message.Message):
    __slots__ = ["is_syncing", "sync_status", "engine_started"]
    IS_SYNCING_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STARTED_FIELD_NUMBER: _ClassVar[int]
    is_syncing: bool
    sync_status: _containers.RepeatedCompositeFieldContainer[SyncStatus]
    engine_started: bool
    def __init__(self, is_syncing: bool = ..., sync_status: _Optional[_Iterable[_Union[SyncStatus, _Mapping]]] = ..., engine_started: bool = ...) -> None: ...

class SyncStatus(_message.Message):
    __slots__ = ["peerId", "inSync", "shouldSync", "divergencePrefix", "divergenceSecondsAgo", "theirMessages", "ourMessages", "lastBadSync", "score"]
    PEERID_FIELD_NUMBER: _ClassVar[int]
    INSYNC_FIELD_NUMBER: _ClassVar[int]
    SHOULDSYNC_FIELD_NUMBER: _ClassVar[int]
    DIVERGENCEPREFIX_FIELD_NUMBER: _ClassVar[int]
    DIVERGENCESECONDSAGO_FIELD_NUMBER: _ClassVar[int]
    THEIRMESSAGES_FIELD_NUMBER: _ClassVar[int]
    OURMESSAGES_FIELD_NUMBER: _ClassVar[int]
    LASTBADSYNC_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    peerId: str
    inSync: str
    shouldSync: bool
    divergencePrefix: str
    divergenceSecondsAgo: int
    theirMessages: int
    ourMessages: int
    lastBadSync: int
    score: int
    def __init__(self, peerId: _Optional[str] = ..., inSync: _Optional[str] = ..., shouldSync: bool = ..., divergencePrefix: _Optional[str] = ..., divergenceSecondsAgo: _Optional[int] = ..., theirMessages: _Optional[int] = ..., ourMessages: _Optional[int] = ..., lastBadSync: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...

class TrieNodeMetadataResponse(_message.Message):
    __slots__ = ["prefix", "num_messages", "hash", "children"]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    NUM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    prefix: bytes
    num_messages: int
    hash: str
    children: _containers.RepeatedCompositeFieldContainer[TrieNodeMetadataResponse]
    def __init__(self, prefix: _Optional[bytes] = ..., num_messages: _Optional[int] = ..., hash: _Optional[str] = ..., children: _Optional[_Iterable[_Union[TrieNodeMetadataResponse, _Mapping]]] = ...) -> None: ...

class TrieNodeSnapshotResponse(_message.Message):
    __slots__ = ["prefix", "excluded_hashes", "num_messages", "root_hash"]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_HASHES_FIELD_NUMBER: _ClassVar[int]
    NUM_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ROOT_HASH_FIELD_NUMBER: _ClassVar[int]
    prefix: bytes
    excluded_hashes: _containers.RepeatedScalarFieldContainer[str]
    num_messages: int
    root_hash: str
    def __init__(self, prefix: _Optional[bytes] = ..., excluded_hashes: _Optional[_Iterable[str]] = ..., num_messages: _Optional[int] = ..., root_hash: _Optional[str] = ...) -> None: ...

class TrieNodePrefix(_message.Message):
    __slots__ = ["prefix"]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    prefix: bytes
    def __init__(self, prefix: _Optional[bytes] = ...) -> None: ...

class SyncIds(_message.Message):
    __slots__ = ["sync_ids"]
    SYNC_IDS_FIELD_NUMBER: _ClassVar[int]
    sync_ids: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, sync_ids: _Optional[_Iterable[bytes]] = ...) -> None: ...

class FidRequest(_message.Message):
    __slots__ = ["fid", "page_size", "page_token", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class FidTimestampRequest(_message.Message):
    __slots__ = ["fid", "page_size", "page_token", "reverse", "start_timestamp", "stop_timestamp"]
    FID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    fid: int
    page_size: int
    page_token: bytes
    reverse: bool
    start_timestamp: int
    stop_timestamp: int
    def __init__(self, fid: _Optional[int] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ..., start_timestamp: _Optional[int] = ..., stop_timestamp: _Optional[int] = ...) -> None: ...

class FidsRequest(_message.Message):
    __slots__ = ["page_size", "page_token", "reverse"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class FidsResponse(_message.Message):
    __slots__ = ["fids", "next_page_token"]
    FIDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    fids: _containers.RepeatedScalarFieldContainer[int]
    next_page_token: bytes
    def __init__(self, fids: _Optional[_Iterable[int]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class MessagesResponse(_message.Message):
    __slots__ = ["messages", "next_page_token"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    next_page_token: bytes
    def __init__(self, messages: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class CastsByParentRequest(_message.Message):
    __slots__ = ["parent_cast_id", "parent_url", "page_size", "page_token", "reverse"]
    PARENT_CAST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    parent_cast_id: _message_pb2.CastId
    parent_url: str
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, parent_cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ..., parent_url: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class ReactionRequest(_message.Message):
    __slots__ = ["fid", "reaction_type", "target_cast_id", "target_url"]
    FID_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CAST_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    fid: int
    reaction_type: _message_pb2.ReactionType
    target_cast_id: _message_pb2.CastId
    target_url: str
    def __init__(self, fid: _Optional[int] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., target_cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ..., target_url: _Optional[str] = ...) -> None: ...

class ReactionsByFidRequest(_message.Message):
    __slots__ = ["fid", "reaction_type", "page_size", "page_token", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    reaction_type: _message_pb2.ReactionType
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class ReactionsByTargetRequest(_message.Message):
    __slots__ = ["target_cast_id", "target_url", "reaction_type", "page_size", "page_token", "reverse"]
    TARGET_CAST_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    target_cast_id: _message_pb2.CastId
    target_url: str
    reaction_type: _message_pb2.ReactionType
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, target_cast_id: _Optional[_Union[_message_pb2.CastId, _Mapping]] = ..., target_url: _Optional[str] = ..., reaction_type: _Optional[_Union[_message_pb2.ReactionType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class UserDataRequest(_message.Message):
    __slots__ = ["fid", "user_data_type"]
    FID_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    user_data_type: _message_pb2.UserDataType
    def __init__(self, fid: _Optional[int] = ..., user_data_type: _Optional[_Union[_message_pb2.UserDataType, str]] = ...) -> None: ...

class NameRegistryEventRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    def __init__(self, name: _Optional[bytes] = ...) -> None: ...

class RentRegistryEventsRequest(_message.Message):
    __slots__ = ["fid"]
    FID_FIELD_NUMBER: _ClassVar[int]
    fid: int
    def __init__(self, fid: _Optional[int] = ...) -> None: ...

class OnChainEventRequest(_message.Message):
    __slots__ = ["fid", "event_type", "page_size", "page_token", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    event_type: _onchain_event_pb2.OnChainEventType
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., event_type: _Optional[_Union[_onchain_event_pb2.OnChainEventType, str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class OnChainEventResponse(_message.Message):
    __slots__ = ["events", "next_page_token"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_onchain_event_pb2.OnChainEvent]
    next_page_token: bytes
    def __init__(self, events: _Optional[_Iterable[_Union[_onchain_event_pb2.OnChainEvent, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class StorageLimitsResponse(_message.Message):
    __slots__ = ["limits", "units", "unit_details"]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    UNIT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    limits: _containers.RepeatedCompositeFieldContainer[StorageLimit]
    units: int
    unit_details: _containers.RepeatedCompositeFieldContainer[StorageUnitDetails]
    def __init__(self, limits: _Optional[_Iterable[_Union[StorageLimit, _Mapping]]] = ..., units: _Optional[int] = ..., unit_details: _Optional[_Iterable[_Union[StorageUnitDetails, _Mapping]]] = ...) -> None: ...

class StorageUnitDetails(_message.Message):
    __slots__ = ["unit_type", "unit_size"]
    UNIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_SIZE_FIELD_NUMBER: _ClassVar[int]
    unit_type: StorageUnitType
    unit_size: int
    def __init__(self, unit_type: _Optional[_Union[StorageUnitType, str]] = ..., unit_size: _Optional[int] = ...) -> None: ...

class StorageLimit(_message.Message):
    __slots__ = ["store_type", "name", "limit", "used", "earliestTimestamp", "earliestHash"]
    STORE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    EARLIESTTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EARLIESTHASH_FIELD_NUMBER: _ClassVar[int]
    store_type: StoreType
    name: str
    limit: int
    used: int
    earliestTimestamp: int
    earliestHash: bytes
    def __init__(self, store_type: _Optional[_Union[StoreType, str]] = ..., name: _Optional[str] = ..., limit: _Optional[int] = ..., used: _Optional[int] = ..., earliestTimestamp: _Optional[int] = ..., earliestHash: _Optional[bytes] = ...) -> None: ...

class UsernameProofRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    def __init__(self, name: _Optional[bytes] = ...) -> None: ...

class UsernameProofsResponse(_message.Message):
    __slots__ = ["proofs"]
    PROOFS_FIELD_NUMBER: _ClassVar[int]
    proofs: _containers.RepeatedCompositeFieldContainer[_username_proof_pb2.UserNameProof]
    def __init__(self, proofs: _Optional[_Iterable[_Union[_username_proof_pb2.UserNameProof, _Mapping]]] = ...) -> None: ...

class VerificationRequest(_message.Message):
    __slots__ = ["fid", "address"]
    FID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    fid: int
    address: bytes
    def __init__(self, fid: _Optional[int] = ..., address: _Optional[bytes] = ...) -> None: ...

class SignerRequest(_message.Message):
    __slots__ = ["fid", "signer"]
    FID_FIELD_NUMBER: _ClassVar[int]
    SIGNER_FIELD_NUMBER: _ClassVar[int]
    fid: int
    signer: bytes
    def __init__(self, fid: _Optional[int] = ..., signer: _Optional[bytes] = ...) -> None: ...

class LinkRequest(_message.Message):
    __slots__ = ["fid", "link_type", "target_fid"]
    FID_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FID_FIELD_NUMBER: _ClassVar[int]
    fid: int
    link_type: str
    target_fid: int
    def __init__(self, fid: _Optional[int] = ..., link_type: _Optional[str] = ..., target_fid: _Optional[int] = ...) -> None: ...

class LinksByFidRequest(_message.Message):
    __slots__ = ["fid", "link_type", "page_size", "page_token", "reverse"]
    FID_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    fid: int
    link_type: str
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, fid: _Optional[int] = ..., link_type: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class LinksByTargetRequest(_message.Message):
    __slots__ = ["target_fid", "link_type", "page_size", "page_token", "reverse"]
    TARGET_FID_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    target_fid: int
    link_type: str
    page_size: int
    page_token: bytes
    reverse: bool
    def __init__(self, target_fid: _Optional[int] = ..., link_type: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[bytes] = ..., reverse: bool = ...) -> None: ...

class IdRegistryEventByAddressRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: bytes
    def __init__(self, address: _Optional[bytes] = ...) -> None: ...

class ContactInfoResponse(_message.Message):
    __slots__ = ["contacts"]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    contacts: _containers.RepeatedCompositeFieldContainer[_gossip_pb2.ContactInfoContentBody]
    def __init__(self, contacts: _Optional[_Iterable[_Union[_gossip_pb2.ContactInfoContentBody, _Mapping]]] = ...) -> None: ...

class ValidationResponse(_message.Message):
    __slots__ = ["valid", "message"]
    VALID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    message: _message_pb2.Message
    def __init__(self, valid: bool = ..., message: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class StreamSyncRequest(_message.Message):
    __slots__ = ["get_info", "get_current_peers", "stop_sync", "force_sync", "get_sync_status", "get_all_sync_ids_by_prefix", "get_all_messages_by_sync_ids", "get_sync_metadata_by_prefix", "get_sync_snapshot_by_prefix", "get_on_chain_events", "get_on_chain_signers_by_fid"]
    GET_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_PEERS_FIELD_NUMBER: _ClassVar[int]
    STOP_SYNC_FIELD_NUMBER: _ClassVar[int]
    FORCE_SYNC_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_STATUS_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_SYNC_IDS_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_MESSAGES_BY_SYNC_IDS_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_METADATA_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_SNAPSHOT_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_ON_CHAIN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    GET_ON_CHAIN_SIGNERS_BY_FID_FIELD_NUMBER: _ClassVar[int]
    get_info: HubInfoRequest
    get_current_peers: Empty
    stop_sync: Empty
    force_sync: SyncStatusRequest
    get_sync_status: SyncStatusRequest
    get_all_sync_ids_by_prefix: TrieNodePrefix
    get_all_messages_by_sync_ids: SyncIds
    get_sync_metadata_by_prefix: TrieNodePrefix
    get_sync_snapshot_by_prefix: TrieNodePrefix
    get_on_chain_events: OnChainEventRequest
    get_on_chain_signers_by_fid: FidRequest
    def __init__(self, get_info: _Optional[_Union[HubInfoRequest, _Mapping]] = ..., get_current_peers: _Optional[_Union[Empty, _Mapping]] = ..., stop_sync: _Optional[_Union[Empty, _Mapping]] = ..., force_sync: _Optional[_Union[SyncStatusRequest, _Mapping]] = ..., get_sync_status: _Optional[_Union[SyncStatusRequest, _Mapping]] = ..., get_all_sync_ids_by_prefix: _Optional[_Union[TrieNodePrefix, _Mapping]] = ..., get_all_messages_by_sync_ids: _Optional[_Union[SyncIds, _Mapping]] = ..., get_sync_metadata_by_prefix: _Optional[_Union[TrieNodePrefix, _Mapping]] = ..., get_sync_snapshot_by_prefix: _Optional[_Union[TrieNodePrefix, _Mapping]] = ..., get_on_chain_events: _Optional[_Union[OnChainEventRequest, _Mapping]] = ..., get_on_chain_signers_by_fid: _Optional[_Union[FidRequest, _Mapping]] = ...) -> None: ...

class StreamError(_message.Message):
    __slots__ = ["errCode", "message", "request"]
    ERRCODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    errCode: str
    message: str
    request: str
    def __init__(self, errCode: _Optional[str] = ..., message: _Optional[str] = ..., request: _Optional[str] = ...) -> None: ...

class StreamSyncResponse(_message.Message):
    __slots__ = ["get_info", "get_current_peers", "stop_sync", "force_sync", "get_sync_status", "get_all_sync_ids_by_prefix", "get_all_messages_by_sync_ids", "get_sync_metadata_by_prefix", "get_sync_snapshot_by_prefix", "get_on_chain_events", "get_on_chain_signers_by_fid", "error"]
    GET_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_PEERS_FIELD_NUMBER: _ClassVar[int]
    STOP_SYNC_FIELD_NUMBER: _ClassVar[int]
    FORCE_SYNC_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_STATUS_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_SYNC_IDS_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_ALL_MESSAGES_BY_SYNC_IDS_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_METADATA_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_SYNC_SNAPSHOT_BY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GET_ON_CHAIN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    GET_ON_CHAIN_SIGNERS_BY_FID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    get_info: HubInfoResponse
    get_current_peers: ContactInfoResponse
    stop_sync: SyncStatusResponse
    force_sync: SyncStatusResponse
    get_sync_status: SyncStatusResponse
    get_all_sync_ids_by_prefix: SyncIds
    get_all_messages_by_sync_ids: MessagesResponse
    get_sync_metadata_by_prefix: TrieNodeMetadataResponse
    get_sync_snapshot_by_prefix: TrieNodeSnapshotResponse
    get_on_chain_events: OnChainEventResponse
    get_on_chain_signers_by_fid: OnChainEventResponse
    error: StreamError
    def __init__(self, get_info: _Optional[_Union[HubInfoResponse, _Mapping]] = ..., get_current_peers: _Optional[_Union[ContactInfoResponse, _Mapping]] = ..., stop_sync: _Optional[_Union[SyncStatusResponse, _Mapping]] = ..., force_sync: _Optional[_Union[SyncStatusResponse, _Mapping]] = ..., get_sync_status: _Optional[_Union[SyncStatusResponse, _Mapping]] = ..., get_all_sync_ids_by_prefix: _Optional[_Union[SyncIds, _Mapping]] = ..., get_all_messages_by_sync_ids: _Optional[_Union[MessagesResponse, _Mapping]] = ..., get_sync_metadata_by_prefix: _Optional[_Union[TrieNodeMetadataResponse, _Mapping]] = ..., get_sync_snapshot_by_prefix: _Optional[_Union[TrieNodeSnapshotResponse, _Mapping]] = ..., get_on_chain_events: _Optional[_Union[OnChainEventResponse, _Mapping]] = ..., get_on_chain_signers_by_fid: _Optional[_Union[OnChainEventResponse, _Mapping]] = ..., error: _Optional[_Union[StreamError, _Mapping]] = ...) -> None: ...

class StreamFetchRequest(_message.Message):
    __slots__ = ["idempotency_key", "cast_messages_by_fid", "reaction_messages_by_fid", "verification_messages_by_fid", "user_data_messages_by_fid", "link_messages_by_fid"]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CAST_MESSAGES_BY_FID_FIELD_NUMBER: _ClassVar[int]
    REACTION_MESSAGES_BY_FID_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_MESSAGES_BY_FID_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_MESSAGES_BY_FID_FIELD_NUMBER: _ClassVar[int]
    LINK_MESSAGES_BY_FID_FIELD_NUMBER: _ClassVar[int]
    idempotency_key: str
    cast_messages_by_fid: FidTimestampRequest
    reaction_messages_by_fid: FidTimestampRequest
    verification_messages_by_fid: FidTimestampRequest
    user_data_messages_by_fid: FidTimestampRequest
    link_messages_by_fid: FidTimestampRequest
    def __init__(self, idempotency_key: _Optional[str] = ..., cast_messages_by_fid: _Optional[_Union[FidTimestampRequest, _Mapping]] = ..., reaction_messages_by_fid: _Optional[_Union[FidTimestampRequest, _Mapping]] = ..., verification_messages_by_fid: _Optional[_Union[FidTimestampRequest, _Mapping]] = ..., user_data_messages_by_fid: _Optional[_Union[FidTimestampRequest, _Mapping]] = ..., link_messages_by_fid: _Optional[_Union[FidTimestampRequest, _Mapping]] = ...) -> None: ...

class StreamFetchResponse(_message.Message):
    __slots__ = ["idempotency_key", "messages", "error"]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    idempotency_key: str
    messages: MessagesResponse
    error: StreamError
    def __init__(self, idempotency_key: _Optional[str] = ..., messages: _Optional[_Union[MessagesResponse, _Mapping]] = ..., error: _Optional[_Union[StreamError, _Mapping]] = ...) -> None: ...
