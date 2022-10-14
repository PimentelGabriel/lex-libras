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
    `letra` char(1),
    `palavra` varchar(50) NOT NULL,
    `descricao` text,
    `exemplo_glosalibras` text,
    `exemplo_ptbr` text,
    `assunto` tinyint UNSIGNED,
    `mao` tinyint UNSIGNED,
    `video_url` varchar(50),
    `video_ines` varchar(50),
    `image_ines` varchar(50),
    `classe_gramatical` int(11),
    `origem` tinyint UNSIGNED,
    `status` tinyint UNSIGNED,
    PRIMARY KEY (`id`),
    INDEX (`palavra`),
    KEY `classe_gramatical` (`classe_gramatical`),
    CONSTRAINT `classe_gramatical_fk_1` FOREIGN KEY (`classe_gramatical`) REFERENCES `classes_gramaticais` (`id`) ON UPDATE CASCADE ON DELETE RESTRICT,
    CONSTRAINT `assunto_fk_2` FOREIGN KEY (`assunto`) REFERENCES `assuntos` (`id`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;