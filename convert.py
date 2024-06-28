import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_folder, filename)

            output_filename = os.path.splitext(filename)[0] + ".mp3"
            output_file = os.path.join(output_folder, output_filename)

            try:
                video_clip = VideoFileClip(input_file)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(output_file)

                video_clip.close()
                audio_clip.close()

                # Remove o arquivo de vídeo após a conversão
                os.remove(input_file)
                print(f"Arquivo '{input_file}' foi removido com sucesso após a conversão.")
            except Exception as e:
                print(f"Erro durante a conversão do arquivo '{input_file}': {e}")

