import os
import json
import logging
from yout import baixar_videos
from convert import convert_mp4_to_mp3

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def carregar_links_do_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data.get('links', [])

def main():
    # Carregar links do arquivo JSON
    links_dos_videos = carregar_links_do_json('links.json')

    if not links_dos_videos:
        logging.error("Nenhum link encontrado no arquivo JSON.")
        return

    try:
        logging.info("Iniciando o download dos vídeos...")
        baixar_videos(links_dos_videos)
        logging.info("Todos os vídeos foram baixados com sucesso.")
    except Exception as e:
        logging.error(f"Erro durante o download dos vídeos: {e}")
        return

    try:
        logging.info("Iniciando a conversão dos vídeos para MP3...")
        convert_mp4_to_mp3('Videos', 'Musica')
        logging.info("Conversão concluída com sucesso.")
    except Exception as e:
        logging.error(f"Erro durante a conversão dos vídeos: {e}")

if __name__ == "__main__":
    main()
