import os
from pytube import YouTube
from urllib.parse import urlparse, parse_qs

def extrair_id_video(link):
    parsed_url = urlparse(link)
    video_id = parse_qs(parsed_url.query).get('v')
    return video_id[0] if video_id else None

def baixar_video(link):
    yt = None
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
        print(f"Baixando o vídeo '{yt.title}'...")
        stream.download(output_path="Videos", filename_prefix="")
        print(f"O vídeo '{yt.title}' foi baixado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao baixar o vídeo de '{link}': {e}")
        if yt:
            file_path = os.path.join("Videos", f"{yt.title}.mp4")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Arquivo '{yt.title}.mp4' excluído devido ao erro durante o download.")
        return False

def baixar_videos(lista_links):
    for link in lista_links:
        baixar_video(link)