CREATE DATABASE `LEX_LIBRAS`
/*!40100 DEFAULT CHARACTER SET utf8mb4 collate_utf8mb4_general-ci */
CREATE TABLE
  dictionary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    word VARCHAR(50),
    id_class_word INT,
    path_video VARCHAR(255),
    FOREIGN KEY (id_class_word) REFERENCES class_word(id_class) ON DELETE RESTRICT ON UPDATE CASCADE
  );


-- DADOS DE TESTE ----
INSERT INTO
  dictionary(word, id_class_word, path_video)
VALUES
  ('IR', 1, 'http://'),
  ('VENCER', 1, 'http://'),
  ('MOSQUITO', 2, 'http://');


CREATE TABLE
  class_word (
    id_class INT PRIMARY KEY AUTO_INCREMENT,
    name_class VARCHAR(20) NOT NULL,
    desc_class VARCHAR(225)
  );


INSERT INTO
  class_word(name_class, desc_class) VALUE(
    "VERB-CONJU",
    "Verbo que sobre conjugação quanto a pessoa, tanto no sujeito como no objeto"
  );


INSERT INTO
  class_word(name_class, desc_class) VALUE("SUBSTANTIVO", "Substantivo simples");