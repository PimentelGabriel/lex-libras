from db.configs.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class Dictionary(Base):
    __tablename__ = "dictionary"
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, nullable=False)
    id_class_word = Column(
        Integer,
        ForeignKey("class_word.id_class"),
        nullable=False
    )
    path_video = Column(String)

    # classWords = relationship(
    #     "ClassWord",
    #     back_populates="dictionary"
    #     #cascade="all, delete-orphan"
    # )

    def __repr__(self):
        return f"Dicitonary (\n\tid={self.id},\n\tword={self.word},\n\tid_class_word={self.id_class_word},\n\tpath_video={self.path_video}\n)"
