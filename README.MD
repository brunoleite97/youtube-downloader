# Download musicas MP3

## Objetivo do projeto

Possibilitar o download de musicas do youtube localmente, sem o risco de virus ou impedimento por anuncios.

## Inicio

### Preparação do ambiente

Será necessario o [Python](https://www.python.org/), após pronto, será preciso clonar o repositorio.

```
https://github.com/brunoleite97/youtube-downloader.git
```

### Instalação
Para a instalação crie o ambiente virtual e instale as dependencias

```
python -m venv env
```
```
env\Scripts\activate
```
```
pip install -r requirements.txt
```

### Preparando o download

Para o download, será necessario criar um arquivo.json, onde será informado os links dos das musicas a serem baixadas. Ele deve ter o seguinte formato:
<details><summary>arquivo.json</summary>

```
{
    "links": [
        "https://www.youtube.com/watch?v=fregObNcHC8",
        "https://www.youtube.com/watch?v=hTWKbfoikeg"
    ]
}
```
</details>

### Execução

```
python main.py
```
