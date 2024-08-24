import os
from urllib.parse import urlparse, parse_qs
import yt_dlp

def extrair_id_video(link):
    parsed_url = urlparse(link)
    video_id = parse_qs(parsed_url.query).get('v')
    return video_id[0] if video_id else None

def baixar_video(link):
    try:
        if not os.path.exists("Videos"):
            os.makedirs("Videos")

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'Videos/%(title)s.%(ext)s',
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

if __name__ == "__main__":
    lista_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=9bZkp7q19f0"
    ]
    baixar_videos(lista_links)
