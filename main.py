import os
import json
import logging
from yout import baixar_videos
from convert import convert_mp4_to_mp3
from playlists import get_playlist_links, save_links_to_json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def carregar_links_do_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        return data.get('links', [])

def main():

    escolha = input("o link é individual (digite 'I') ou uma playlist (digite 'P')? ").strip().upper()

    if escolha == 'P':

        playlist_url = input("Digite o link da playlist: ").strip()

        if not playlist_url:
            logging.error("Nenhum link fornecido.")
            return

        logging.info("Extraindo links da playlist...")
        video_urls = get_playlist_links(playlist_url)
        save_links_to_json(video_urls, 'links.json')
        logging.info("Links extraídos com sucesso.")

        links_dos_videos = carregar_links_do_json('links.json')

        if not links_dos_videos:
            logging.error("Nenhum link encontrado no arquivo JSON.")
            return

    elif escolha == 'I':
        video_url = input("Digite o link do vídeo: ").strip()

        if not video_url:
            logging.error("Nenhum link fornecido.")
            return
        
        links_dos_videos = [video_url]

    else:
        logging.error("Opção inválida. Digite 'I para link individual ou 'p para playlist.")
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
