from sqlalchemy import Column, BigInteger, Text, DateTime, ForeignKey, Boolean
from infrastructure.databases.base import Base

class SyllabusCommentModel(Base):
    # Tên bảng số nhiều, snake_case
    __tablename__ = 'syllabus_comments'
    __table_args__ = {'extend_existing': True}

    # Khóa chính: id, BIGINT
    id = Column(BigInteger, primary_key=True, autoincrement=True)

    # Khóa ngoại: Đề cương đang được thảo luận
    syllabus_id = Column(BigInteger, ForeignKey('syllabuses.id'), nullable=False)

    # Khóa ngoại: Người viết comment
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)

    # Nội dung góp ý: TEXT, Not Null
    content = Column(Text, nullable=False)
    
    # Khóa ngoại tự tham chiếu: ID của comment cha (để tạo luồng reply)
    parent_id = Column(BigInteger, ForeignKey('syllabus_comments.id'), nullable=True)

    # Trạng thái đã giải quyết hay chưa
    is_resolved = Column(Boolean, default=False)

   # Thời gian tạo và cập nhật
    created_at = Column(DateTime)
    updated_at = Column(DateTime)