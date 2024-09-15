from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateOrRevokeJobState(_message.Message):
    __slots__ = ["last_job_timestamp", "last_fid"]
    LAST_JOB_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_FID_FIELD_NUMBER: _ClassVar[int]
    last_job_timestamp: int
    last_fid: int
    def __init__(self, last_job_timestamp: _Optional[int] = ..., last_fid: _Optional[int] = ...) -> None: ...

class HubState(_message.Message):
    __slots__ = ["last_fname_proof", "last_l2_block", "validate_or_revoke_state"]
    LAST_FNAME_PROOF_FIELD_NUMBER: _ClassVar[int]
    LAST_L2_BLOCK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_OR_REVOKE_STATE_FIELD_NUMBER: _ClassVar[int]
    last_fname_proof: int
    last_l2_block: int
    validate_or_revoke_state: ValidateOrRevokeJobState
    def __init__(self, last_fname_proof: _Optional[int] = ..., last_l2_block: _Optional[int] = ..., validate_or_revoke_state: _Optional[_Union[ValidateOrRevokeJobState, _Mapping]] = ...) -> None: ...
