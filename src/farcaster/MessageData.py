from . fcproto.message_pb2 import (
    MessageType, FarcasterNetwork, MessageData,
    LinkBody, CastId, SignatureScheme, HashScheme,
    CastAddBody, CastRemoveBody,
    ReactionBody, UserDataType, UserDataBody
    )
import time

import re
from functools import reduce


FARCASTER_EPOCH = 1609459200  # January 1, 2021 UTC

class Link:
    def _link(cls, message_type: MessageType, fid: int, target_fid: int, link_type: str="follow") -> MessageData:
        return MessageData(
            type = message_type,
            fid = fid,
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET,
            link_body = LinkBody(
                type = link_type,
                target_fid=target_fid
            )
        )

    def add(cls, fid: int, target_fid: int, link_type: str="follow") -> MessageData:
        return cls._link(MessageType.MESSAGE_TYPE_LINK_ADD, fid, target_fid, link_type)
    def remove(cls, fid: int, target_fid: int, link_type: str="follow") -> MessageData:
        return cls._link(MessageType.MESSAGE_TYPE_LINK_REMOVE, fid, target_fid, link_type)

class Cast:
    def add(self, fid, text, mentions=[], mentions_positions=[], embeds=[]) -> MessageData:
        md = MessageData(
            type = MessageType.MESSAGE_TYPE_CAST_ADD,
            fid = fid,
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET,
            cast_add_body = CastAddBody(
                text = text,
                embeds = [],
                mentions = [],
                mentions_positions=[]
            )
        )
        md.cast_add_body.mentions.extend(mentions)
        md.cast_add_body.mentions_positions.extend(mentions_positions)
        md.cast_add_body.embeds.extend(embeds)
        return md
    def remove(self, fid, target_hash) -> MessageData:
        return MessageData(
            type = MessageType.MESSAGE_TYPE_CAST_REMOVE,
            fid = fid,
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET,
            cast_remove_body = CastRemoveBody(
                target_hash = bytes.fromhex(target_hash[2:])
            )
        )

class Reaction:
    def _do(cls, message_type, fid, reaction_type, cast_fid=None, cast_hash=None, target_url=None):
        if cast_hash:
            hash_bytes = hash=bytes.fromhex(cast_hash[2:])
        return MessageData(
            type = message_type,
            fid = fid,
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET,
            reaction_body = ReactionBody(type = reaction_type, target_cast_id=CastId(fid=cast_fid, hash=hash_bytes)
            ) if not target_url else ReactionBody(type = reaction_type, target_url=target_url)
        )
    def add(cls, fid, reaction_type, cast_fid, cast_hash):
        return cls._do(MessageType.MESSAGE_TYPE_REACTION_ADD, fid, reaction_type, cast_fid, cast_hash)
    def remove(cls, fid, reaction_type, cast_fid, cast_hash):
        return cls._do(MessageType.MESSAGE_TYPE_REACTION_REMOVE, fid, reaction_type, cast_fid, cast_hash)
class ReactionToCast(Reaction):
    def add(cls, fid, reaction_type, cast_fid, cast_hash):
        return cls._do(message_type=MessageType.MESSAGE_TYPE_REACTION_ADD, 
            fid=fid, reaction_type=reaction_type, cast_fid=cast_fid, cast_hash=cast_hash, target_url=None)
    def remove(cls, fid, reaction_type, cast_fid, cast_hash):
        return cls._do(message_type=MessageType.MESSAGE_TYPE_REACTION_REMOVE, 
            fid=fid, reaction_type=reaction_type, cast_fid=cast_fid, cast_hash=cast_hash, target_url=None)
class ReactionToUrl(Reaction):
    def add(cls, fid, reaction_type, target_url):
        return cls._do(message_type=MessageType.MESSAGE_TYPE_REACTION_ADD, fid=fid, reaction_type=reaction_type, target_url=target_url)
    def remove(cls, fid, reaction_type, target_url):
        return cls._do(message_type=MessageType.MESSAGE_TYPE_REACTION_REMOVE, fid=fid, reaction_type=reaction_type, target_url=target_url)

class UserData:
    def add(cls, fid: int, data_type:UserDataType, data_value:str) -> MessageData:
        return MessageData(
            type = MessageType.MESSAGE_TYPE_USER_DATA_ADD,
            fid = fid,
            timestamp = int( time.time() ) - FARCASTER_EPOCH,
            network = FarcasterNetwork.FARCASTER_NETWORK_MAINNET,
            user_data_body = UserDataBody(
                type = data_type,
                value = data_value
            )
        )
"""
enum UserDataType {
  USER_DATA_TYPE_NONE = 0;
  USER_DATA_TYPE_PFP = 1; // Profile Picture for the user
  USER_DATA_TYPE_DISPLAY = 2; // Display Name for the user
  USER_DATA_TYPE_BIO = 3; // Bio for the user
  USER_DATA_TYPE_URL = 5; // URL of the user
  USER_DATA_TYPE_USERNAME = 6; // Preferred Name for the user
}
"""
"""
def extract_mentions(text: str, hub_addr) -> (str, list, list):
        hub_service = HubService(hub_addr, use_async=False)
        text2 = ''
        mentions = []
        mentions_positions = []
        for i in re.split('(@\w*\.eth|@\w*)(\W)', text):
            #print(f"--|{i}|--{len(i)}")
            if len(i)>1 and len(mentions)<11 and i[0] == '@':
                try:
                    fid = hub_service.GetUsernameProof(i[1:]).fid
                    mentions.append(fid)
                    mentions_positions.append(len(bytes(text2,'utf-8')))
                except:
                    text2 += i
            else:
                text2 += i
        return (text2, mentions, mentions_positions)
"""