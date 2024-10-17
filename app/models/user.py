import uuid

from sqlalchemy import Column, Integer, Text, UUID, String
from sqlalchemy_utils import EncryptedType

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
