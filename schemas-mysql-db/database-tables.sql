CREATE TABLE `classes_gramaticais` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `flag` varchar(15) NOT NULL,
  `descricao` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `assuntos` (
    `id` TINYINT UNSIGNED PRIMARY KEY,
    `nome` VARCHAR(50) NOT NULL
);



CREATE TABLE `palavras` (
    `id` INT UNSIGNED,
    `ident` SMALLINT UNSIGNED,
    `letra` CHAR(1),
    `palavra` VARCHAR(50) NOT NULL,
    `conjug_genero` VARCHAR(50) DEFAULT NULL,
    `descricao` TEXT,
    `exemplo_glosalibras` TEXT,
    `exemplo_ptbr` TEXT,
    `assunto` TINYINT UNSIGNED,
    `mao` TINYINT UNSIGNED,
    `video_url` VARCHAR(50),
    `video_ines` VARCHAR(50),
    `image_ines` VARCHAR(50),
    `classe_gramatical` INT(11),
    `origem` tinyint UNSIGNED,
    `status` tinyint UNSIGNED,
    PRIMARY KEY (`id`),
    INDEX (`palavra`),
    KEY `classe_gramatical` (`classe_gramatical`),
    CONSTRAINT `classe_gramatical_fk_1` FOREIGN KEY (`classe_gramatical`) REFERENCES `classes_gramaticais` (`id`) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT `assunto_fk_2` FOREIGN KEY (`assunto`) REFERENCES `assuntos` (`id`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;