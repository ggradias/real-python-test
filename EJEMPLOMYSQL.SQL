USE VIDEOTECA;
SHOW DATABASES;



SHOW tables;

DROP TABLE IF EXISTS pelicula;
CREATE TABLE pelicula
(
   titulo VARCHAR(64) NOT NULL,
   director VARCHAR(128) NOT NULL DEFAULT '',
   interprete VARCHAR(128) NOT NULL DEFAULT '',
   PRIMARY KEY (titulo)
);

describe pelicula;

select * from pelicula;

select titulo, CONCAT(director,' , ',interprete) FROM pelicula;