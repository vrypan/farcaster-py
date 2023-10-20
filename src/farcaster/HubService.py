import os

from nacl.signing import SigningKey
from nacl.encoding import HexEncoder
from eth_account import Account

import grpc
from . fcproto import rpc_pb2, rpc_pb2_grpc

from . fcproto.request_response_pb2 import (
    SubscribeRequest, EventRequest,
    HubInfoResponse, HubInfoRequest, FidRequest, MessagesResponse,
    CastsByParentRequest, MessagesResponse, CastsByParentRequest,
    ReactionRequest, ReactionsByFidRequest, ReactionsByTargetRequest,
    UserDataRequest, UsernameProofRequest, UsernameProofsResponse,
    VerificationRequest,
    SignerRequest, OnChainEventRequest, OnChainEventResponse, IdRegistryEventByAddressRequest, StorageLimitsResponse,
    LinkRequest, LinksByTargetRequest, LinksByFidRequest
    )
from . fcproto.username_proof_pb2 import UserNameProof
from . fcproto.onchain_event_pb2 import OnChainEvent
from . fcproto.message_pb2 import Message, CastId
from . fcproto.hub_event_pb2 import HubEvent 

class HubService:
    def __init__(self, address, use_async=False, use_ssl=False):
        self._async = use_async
        if use_ssl:
            raise Exception("SSL not supported by farcaster.Hub.")
        if use_async:
            self._channel = grpc.aio.insecure_channel(address)
        else:
            self._channel = grpc.insecure_channel(address)
        self._stub = rpc_pb2_grpc.HubServiceStub(self._channel)
    
    def GetInfo(self, db_stats=False) -> HubInfoResponse:
        return self._stub.GetInfo(HubInfoRequest(db_stats=db_stats))

    # rpc SubmitMessage(Message) returns (Message)
    def SubmitMessage(self, Message) -> Message:
        return self._stub.SubmitMessage(Message)
    
    """
    Event Methods
    rpc Subscribe(SubscribeRequest) returns (stream HubEvent);
    rpc GetEvent(EventRequest) returns (HubEvent);
    """
    
    def Subscribe(self, event_types, from_id=None)  -> HubEvent:
        if not self._async:
            raise Exception("Subscribe method is only available in async instances")
        pb_event_types = [t for t in event_types] 
        return self._stub.Subscribe(SubscribeRequest(
            event_types = event_types,
            from_id = from_id
        ))
    def GetEvent(self, id) -> HubEvent:
        return self._stub.GetEvent(EventRequest(id=id))

    """
    Casts:
    rpc GetCast(CastId) returns (Message);
    rpc GetCastsByFid(FidRequest) returns (MessagesResponse);
    rpc GetCastsByParent(CastsByParentRequest) returns (MessagesResponse);
    rpc GetCastsByMention(FidRequest) returns (MessagesResponse);
    """
    def GetCast(self, fid, hash) -> Message:
        r = self._stub.GetCast(CastId(fid=fid, hash=bytes.fromhex(hash[2:])))
        return r
    def GetCastsByFid(self, fid, page_size=50, page_token=None, reverse=True) -> Message:
        r = self._stub.GetCastsByFid(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))
        return r
    def GetCastsByParentCast(self, fid, hash, page_size=50, page_token=None, reverse=True ) -> MessagesResponse:
        r = self._stub.GetCastsByParent(CastsByParentRequest(
            parent_cast_id=CastId(fid=fid, hash=bytes.fromhex(hash[2:])), page_size=page_size, page_token=page_token, reverse=reverse
        ))
        return r
    def GetCastsByParentUrl(self, parent_url=None, page_size=50, page_token=None, reverse=True ) -> MessagesResponse:
        r = self._stub.GetCastsByParent(CastsByParentRequest(
            parent_url=parent_url, page_size=page_size, page_token=page_token, reverse=reverse
        ))
        return r
    def GetCastsByMention(self, fid, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        r = self._stub.GetCastsByMention(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))
        return r

    
    """
    Reactions
    rpc GetReaction(ReactionRequest) returns (Message);
    rpc GetReactionsByFid(ReactionsByFidRequest) returns (MessagesResponse);
    rpc GetReactionsByTarget(ReactionsByTargetRequest) returns (MessagesResponse);
    """
    def GetReactionByCast(self, reaction_fid, reaction_type, cast_fid, cast_hash) -> Message:
        return self._stub.GetReaction( ReactionRequest(
            fid=reaction_fid, 
            reaction_type=reaction_type, 
            target_cast_id=CastId(fid=cast_fid, hash=bytes.fromhex(cast_hash[2:]))
        ))
    def GetReactionByUrl(self, reaction_fid, reaction_type, target_url) -> Message:
        return self._stub.GetReaction( ReactionRequest(
            fid=reaction_fid, 
            reaction_type=reaction_type, 
            target_url=target_url
        ))
    def GetReactionsByFid(self, fid, reaction_type, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetReactionsByFid( ReactionsByFidRequest(
            fid=fid,
            reaction_type=reaction_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        )) 
    def GetReactionsByCast(self, cast_fid, cast_hash, reaction_type, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetReactionsByTarget( ReactionsByTargetRequest(
            target_cast_id=CastId(fid=cast_fid, hash=bytes.fromhex(cast_hash[2:])),
            reaction_type=reaction_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        ))    
    def GetReactionsByUrl(self, target_url, reaction_type, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetReactionsByTarget( ReactionsByTargetRequest(
            target_url=target_url,
            reaction_type=reaction_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        ))    
    
    """
    Fids
    rpc GetFids(FidsRequest) returns (FidsResponse);
    Not implemented.
    """

    """
    User Data
    rpc GetUserData(UserDataRequest) returns (Message);
    rpc GetUserDataByFid(FidRequest) returns (MessagesResponse);
    """
    def GetUserData(self, fid, user_data_type) -> Message:
        return self._stub.GetUserData( UserDataRequest(fid=fid, user_data_type=user_data_type) )
    def GetUserDataByFid(self, fid, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetUserDataByFid( FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse) )
    
    """
    Username Proof
    rpc GetUsernameProof(UsernameProofRequest) returns (UserNameProof);
    rpc GetUserNameProofsByFid(FidRequest) returns (UsernameProofsResponse);
    """
    def GetUsernameProof(self, name) -> UserNameProof:
        return self._stub.GetUsernameProof(UsernameProofRequest(name=bytes(name,'ascii')))
    def GetUserNameProofsByFid(self, fid, page_size=50, page_token=None, reverse=True) -> UserNameProof:
        return self._stub.GetUserNameProofsByFid(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))

    """
    Verifications
    rpc GetVerification(VerificationRequest) returns (Message);
    rpc GetVerificationsByFid(FidRequest) returns (MessagesResponse);
    """
    def GetVerification(self, fid, address) -> Message:
        return self._stub.GetVerification(VerificationRequest(fid=fid, address=bytes.fromhex(address[2:])))
    def GetVerificationsByFid(self, fid, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetVerificationsByFid(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))

    """
    OnChain Events
    rpc GetOnChainSigner(SignerRequest) returns (OnChainEvent);
    rpc GetOnChainSignersByFid(FidRequest) returns (OnChainEventResponse);
    rpc GetOnChainEvents(OnChainEventRequest) returns (OnChainEventResponse);
    rpc GetIdRegistryOnChainEvent(FidRequest) returns (OnChainEvent);
    rpc GetIdRegistryOnChainEventByAddress(IdRegistryEventByAddressRequest) returns (OnChainEvent);
    rpc GetCurrentStorageLimitsByFid(FidRequest) returns (StorageLimitsResponse);
    """
    def GetOnChainSigner(self, fid, signer) -> OnChainEvent:
        return self._stub.GetOnChainSigner(SignerRequest(fid=fid, signer=bytes.fromhex(signer[2:])))
    def GetOnChainSignersByFid(self, fid, page_size=50, page_token=None, reverse=True) -> OnChainEventResponse:
        return self._stub.GetOnChainSignersByFid(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))
    def GetOnChainEvents(self, fid, event_type, page_size=50, page_token=None, reverse=True) -> OnChainEventResponse:
        return self._stub.GetOnChainEvents(OnChainEventRequest(
            fid=fid,
            event_type=event_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        ))
    def GetIdRegistryOnChainEvent(self, fid, page_size=50, page_token=None, reverse=True) -> OnChainEvent:
        return self._stub.GetIdRegistryOnChainEvent(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))
    def GetIdRegistryOnChainEventByAddress(self, address) -> OnChainEvent:
        return self._stub.GetIdRegistryOnChainEventByAddress(IdRegistryEventByAddressRequest(address=bytes.fromhex(address[2:])))
    def GetCurrentStorageLimitsByFid(self, fid, page_size=50, page_token=None, reverse=True) -> StorageLimitsResponse:
        return self._stub.GetCurrentStorageLimitsByFid(FidRequest(fid=fid, page_size=page_size, page_token=page_token, reverse=reverse))

    """
    Links
    rpc GetLink(LinkRequest) returns (Message);
    rpc GetLinksByFid(LinksByFidRequest) returns (MessagesResponse);
    rpc GetLinksByTarget(LinksByTargetRequest) returns (MessagesResponse);
    """
    def GetLink(self, fid, link_type, target) -> Message:
        return self._stub.GetLink(LinkRequest(fid=fid, link_type=link_type, target=target))
    def GetLinksByFid(self, fid, link_type=None, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetLinksByFid(LinksByFidRequest(
            fid=fid,
            link_type=link_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse
        ))
    def GetLinksByTarget(self, target_fid, link_type=None, page_size=50, page_token=None, reverse=True) -> MessagesResponse:
        return self._stub.GetLinksByTarget(LinksByTargetRequest(
            target_fid = target_fid,
            link_type=link_type,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse  
        ))