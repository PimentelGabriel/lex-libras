from Engine import Session

session = Session()

# Exemplos para CRUD
# Insert
# data_insert = Dictionary(word="MÂE", id_class_word=2, path_video="http://")
# session.add(data_insert)
# session.commit()

# Delete
# session.query(Dictionary).filter(Dictionary.word == "MÂE").delete()
# assert session.commit()

# Update
# session.query(Dictionary).filter(Dictionary.word == "MÂE").update(
#     {"path_video": "http://api/words/mãe/"}
# )

# Select
# data = session.query(Dictionary).all()
# for row in data:
#     print(row.word)


# session.close()


# with Session(engine) as session:
#     spongebob = User(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#     )
#     sandy = User(
#         name="sandy",
#         fullname="Sandy Cheeks",
#         addresses=[
#             Address(email_address="sandy@sqlalchemy.org"),
#             Address(email_address="sandy@squirrelpower.org"),
#         ],
#     )
#     patrick = User(name="patrick", fullname="Patrick Star")
#     session.add_all([spongebob, sandy, patrick])
#     session.commit()
