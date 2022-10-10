from db.repository.class_word_repository import ClassWordRepository
from db.repository.dictionary_repository import DictionaryRepository

repo = DictionaryRepository()
data = repo.select()

print(data[0])
