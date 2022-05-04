-- DROP TABLE avaliacao;
-- DROP TABLE filme;
-- DROP TABLE filme_genero;
-- DROP TABLE genero;
CREATE TABLE filme (
  id INTEGER PRIMARY KEY,
  titulo_promocional VARCHAR NOT NULL,
  titulo_original VARCHAR NOT NULL,
  adulto BOOLEAN NOT NULL,
  ano_de_lancamento INTEGER NULL,
  duracao_em_minutos INTEGER NULL
);
CREATE TABLE genero (
  id INTEGER PRIMARY KEY,
  nome VARCHAR UNIQUE NOT NULL
);
CREATE TABLE avaliacao (
  id INTEGER PRIMARY KEY,
  filme_id INTEGER NOT NULL,
  media NUMERIC NOT NULL,
  votos INTEGER NULL,
  FOREIGN KEY (filme_id) REFERENCES filme (id)
);
CREATE TABLE filme_genero (
  filme_id INTEGER NOT NULL,
  genero_id INTEGER NOT NULL,
  FOREIGN KEY (filme_id) REFERENCES filme (id),
  FOREIGN KEY (genero_id) REFERENCES genero (id)
);