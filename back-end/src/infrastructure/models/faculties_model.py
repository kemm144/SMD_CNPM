from sqlalchemy import Column, BigInteger, String, DateTime
from infrastructure.databases.base import Base

class FacultyModel(Base):
    __tablename__ = 'faculties'
    __table_args__ = {'extend_existing': True}
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    
     # Thời gian tạo và cập nhật
    created_at = Column(DateTime)
    updated_at = Column(DateTime)