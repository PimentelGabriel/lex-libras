from db.configs.base import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class ClassWord(Base):
    __tablename__ = "class_word"

    id_class = Column(Integer, primary_key=True, autoincrement=True)
    name_class = Column(String, nullable=False)
    desc_class = Column(String)

    dictionary = relationship(
        "Dictionary", backref="Dictionary", lazy="subquery"
    )

    def __repr__(self):
        return f"ClassWord (\n\tid_class={self.id_class},\n\tname_class={self.name_class},\n\tdesc_class={self.desc_class}\n)"
