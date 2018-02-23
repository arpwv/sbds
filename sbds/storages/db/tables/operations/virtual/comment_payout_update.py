# coding=utf-8

from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Numeric
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy import Boolean
from sqlalchemy import SmallInteger
from sqlalchemy import Integer
from sqlalchemy import BigInteger

#from sqlalchemy.dialects.mysql import JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import JSON

from ...import Base
from ....enums import operation_types_enum
from ....field_handlers import amount_field
from ....field_handlers import amount_symbol_field
from ....field_handlers import comment_body_field
from ..base import BaseOperation
from ..base import BaseVirtualOperation

class CommentPayoutUpdateOperation(Base, BaseVirtualOperation):
    """
    
    
    Steem Blockchain Example
    ======================


    

    """
    
    __tablename__ = 'sbds_op_virtual_comment_payout_updates'
    __operation_type__ = 'comment_payout_update_operation'
    
    author = Column(String(50), index=True) # steem_type:account_name_type
    permlink = Column(Unicode(512), index=True) # name:permlink
    operation_type = Column(
        operation_types_enum,
        nullable=False,
        index=True,
        default='comment_payout_update_operation')
    
    _fields = dict(
        author=lambda x: x.get('author'),
        permlink=lambda x: x.get('permlink'),
    )

