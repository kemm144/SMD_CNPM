from sqlalchemy import Column, Integer, String, Date, DateTime
from infrastructure.databases.base import Base

class AcademicYearModel(Base):
    # Tên bảng số nhiều, snake_case
    __tablename__ = 'academic_years'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), unique=True, nullable=False)
    
    # Ngày bắt đầu và kết thúc
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
    # Thời gian tạo và cập nhật
    created_at = Column(DateTime)
    updated_at = Column(DateTime)