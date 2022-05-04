from conversores import converter_tsv

from sql import inserir_genero, criar_conexao
from tqdm import tqdm

CAMINHO_DO_TSV = "files/title_basics.tsv"
CAMINHO_DO_SQLITE = "db/imdb_filmes.db"

if __name__ == "__main__":
    db_conexao = criar_conexao(CAMINHO_DO_SQLITE)
    with tqdm(total=608540) as pbar:
        for genero in converter_tsv(CAMINHO_DO_TSV):
            pbar.update(1)
            if not genero:
                continue
            if isinstance(genero, list):
                [inserir_genero(g, db_conexao) for g in genero]
            else:
                inserir_genero(genero, db_conexao)
