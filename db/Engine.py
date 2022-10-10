from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, ForeignKey, String, Integer

engine = create_engine(
    'mysql+pymysql://root:@localhost:3306/LEX_LIBRAS',
    echo=True,
    future=False  # Verificar pq quando True, dar erro
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# A seção deve ser instanciada em outro arquivo
# session = Session()

#conn = engine.connect()


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

    classWords = relationship(
        "ClassWord",
        back_populates="dictionary"
        #cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Dicitonary (\n\tid={self.id},\n\tword={self.word},\n\tid_class_word={self.id_class_word},\n\tpath_video={self.path_video}\n)"


class ClassWord(Base):
    __tablename__ = "class_word"

    id_class = Column(Integer, primary_key=True, autoincrement=True)
    name_class = Column(String, nullable=False)
    desc_class = Column(String)

    dictionary = relationship("Dictionary", back_populates="classWords")

    def __repr__(self):
        return f"ClassWord (\n\tid_class={self.id_class},\n\tname_class={self.name_class},\n\tdesc_class={self.desc_class}\n)"


# resp = conn.execute("SELECT * FROM class_word")
# for row in resp:
#     print(row[1])

# class User(Base):
#     __tablename__ = "user_account"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     fullname = Column(String)

#     addresses = relationship(
#         "Address", back_populates="user", cascade="all, delete-orphan"
#     )

#     def __repr__(self):
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# class Address(Base):
#     __tablename__ = "address"

#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

#     user = relationship("User", back_populates="addresses")

#     def __repr__(self):
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
