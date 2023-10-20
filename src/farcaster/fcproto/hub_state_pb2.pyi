from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HubState(_message.Message):
    __slots__ = ["last_fname_proof", "last_l2_block"]
    LAST_FNAME_PROOF_FIELD_NUMBER: _ClassVar[int]
    LAST_L2_BLOCK_FIELD_NUMBER: _ClassVar[int]
    last_fname_proof: int
    last_l2_block: int
    def __init__(self, last_fname_proof: _Optional[int] = ..., last_l2_block: _Optional[int] = ...) -> None: ...
