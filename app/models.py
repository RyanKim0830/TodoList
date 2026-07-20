'''
SQLAlchemy 사용으 클래스 선언으로 DB 구조 정의
'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from database import Base
import uuid 

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, unique=True) #회원가입시 ID 사용자가 설정.
    username = Column(String)
    password_hash = Column(String)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4())) #UUID도 버전이 여러가지고 그중 랜덤값임 4를 사용
    content = Column(String)
    done = Column(Boolean)
    deadline = Column(DateTime, nullable=True) # 추후 deadline on/off 옵션 설정을 위한 nullable 설정
    user_id = Column(String, ForeignKey("users.id"))


