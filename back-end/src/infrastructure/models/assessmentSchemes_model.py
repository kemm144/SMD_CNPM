from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from infrastructure.databases.base import Base

class AssessmentSchemeModel(Base):
    # Tên bảng số nhiều, snake_case
    __tablename__ = 'assessment_schemes'
    __table_args__ = {'extend_existing': True}

    # Khóa chính: id, BIGINT
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Khóa ngoại: Thuộc đề cương nào
    syllabus_id = Column(Integer, ForeignKey('syllabuses.id'), nullable=False)
    
    # Tên đầu điểm
    name = Column(String(100), nullable=False)
    weight = Column(Float, nullable=False)
    
    # Thời gian tạo và cập nhật
    created_at = Column(DateTime)
    updated_at = Column(DateTime)