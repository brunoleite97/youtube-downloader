import os
from urllib.parse import urlparse, parse_qs
import yt_dlp

def extrair_id_video(link):
    parsed_url = urlparse(link)
    video_id = parse_qs(parsed_url.query).get('v')
    return video_id[0] if video_id else None

def verificar_existencia_arquivo(nome_arquivo, pasta):
    for filename in os.listdir(pasta):
        if filename.startswith(nome_arquivo) and filename.endswith(".mp3"):
            return True
    return False

def baixar_video(link):
    try:
        if not os.path.exists("Videos"):
            os.makedirs("Videos")

        # Extrai o título do vídeo sem baixar
        ydl_opts_info = {
            'skip_download': True,
            'quiet': True,
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            video_title = info_dict.get('title', None)

        if verificar_existencia_arquivo(video_title, "Musica"):
            print(f"'{video_title}' já existe na pasta 'Musica'. Pulando o download...")
            return False

        ydl_opts = {
            'format': 'best',
            'outtmpl': f'Videos/{video_title}.%(ext)s',
        }

        print(f"Baixando o vídeo de '{link}'...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"Vídeo baixado com sucesso: {link}")
        return True
    except Exception as e:
        print(f"Erro ao baixar o vídeo de '{link}': {e}")
        return False

def baixar_videos(lista_links):
    for link in lista_links:
        baixar_video(link)