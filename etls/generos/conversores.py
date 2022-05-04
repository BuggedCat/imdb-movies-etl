import csv
from typing import Optional, Union, Generator
from models import Genero


def _conversor_genero(generos: str) -> Optional[Union[Genero, list[Genero]]]:
    try:
        if "," in generos:
            return [Genero(genero) for genero in generos.split(",")]
        else:
            return Genero(generos)
    except ValueError:
        return None


def converter_tsv(
    caminho_do_arquivo: str,
) -> Generator[Optional[Union[Genero, list[Genero]]], None, None]:
    with open(caminho_do_arquivo, encoding="utf-8") as file:
        reader = csv.DictReader(file, dialect="excel-tab")
        for row in reader:
            if row["titleType"] == "movie":
                generos = _conversor_genero(row["genres"])
                yield generos
