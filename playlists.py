from pytube import Playlist
import json

def get_playlist_links(playlist_url):
    playlist = Playlist(playlist_url)
    video_urls = [video.watch_url for video in playlist.videos]
    return video_urls

def save_links_to_json(links, filename):
    data = {"links": links}
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    playlist_url = input("Digite a URL da playlist do YouTube: ").strip()
    if playlist_url:
        video_urls = get_playlist_links(playlist_url)
        save_links_to_json(video_urls, 'links.json')
        print("Links extraídos e salvos em 'links.json'.")
    else:
        print("Nenhuma URL da playlist fornecida.")
