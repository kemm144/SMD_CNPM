from sqlalchemy import Column, BigInteger, String, Text, DateTime, ForeignKey
from infrastructure.databases.base import Base

class WorkflowLogModel(Base):
    # Tên bảng số nhiều, snake_case
    __tablename__ = 'workflow_logs'
    __table_args__ = {'extend_existing': True}

    # Khóa chính: id, BIGINT
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    
    # Khóa ngoại: Đề cương nào đang được xử lý
    syllabus_id = Column(BigInteger, ForeignKey('syllabuses.id'), nullable=False)
    
    # Khóa ngoại: Người thực hiện thao tác (Actor)
    actor_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    
    # Hành động: SUBMIT, APPROVE, REJECT...
    action = Column(String(50), nullable=True)
    
    # Trạng thái chuyển đổi
    from_status = Column(String(50), nullable=True) # Trạng thái cũ
    to_status = Column(String(50), nullable=True)   # Trạng thái mới
    
    # Ghi chú/Lý do
    comment = Column(Text, nullable=True)
    
    # Thời gian tạo
    created_at = Column(DateTime)