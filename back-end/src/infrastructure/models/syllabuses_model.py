from sqlalchemy import Column, BigInteger, String, Text, DateTime, JSON, ForeignKey
from infrastructure.databases.base import Base

class SyllabusModel(Base):
    __tablename__ = 'syllabuses'
    __table_args__ = {'extend_existing': True}

    # Khóa chính: id, BIGINT
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # Các khóa ngoại (Foreign Keys) 
    subject_id = Column(BigInteger, ForeignKey('subjects.id'), nullable=False)
    program_id = Column(BigInteger, ForeignKey('programs.id'), nullable=False)
    academic_year_id = Column(BigInteger, ForeignKey('academic_years.id'), nullable=False)
    lecturer_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    
    # Trạng thái của giáo trình (VD: DRAFT, PUBLISHED)
    status = Column(String(50), nullable=False, default='DRAFT')
    #phiên bản
    version = Column(String(10), nullable=True)
    
    # Phân bổ thời gian cho các hoạt động học tập dưới dạng JSON
    time_allocation = Column(JSON, nullable=True)
    
    # Điều kiện tiên quyết
    prerequisites = Column(Text, nullable=True)
    
    # Thời gian tạo và cập nhật
    created_at = Column(DateTime)
    updated_at = Column(DateTime)