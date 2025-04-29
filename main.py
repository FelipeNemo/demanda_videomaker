"""" Atualiza o doogle drive com o ai.videos, sup.videos(videos de suporte - explicações, referencias etc) e roteiro"""
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import os

def upload_video_to_drive(file_path):
    """Upload a video file to Google Drive and return the file ID."""
    creds, _ = google.auth.default()

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    try:
        # Create Drive API client
        service = build("drive", "v3", credentials=creds)

        file_name = os.path.basename(file_path)  # Pega o nome do arquivo, tipo 'meu_video.mp4'
        mime_type = "video/mp4"  # MIME type para vídeos MP4

        file_metadata = {"name": file_name}
        media = MediaFileUpload(file_path, mimetype=mime_type)

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

        print(f'Upload feito! ID do arquivo: {file.get("id")}')
        return file.get("id")

    except HttpError as error:
        print(f"Ocorreu um erro na API: {error}")
        return None

if __name__ == "__main__":
    caminho_do_video = "C:/Videos/meu_video.mp4"  # <<--- altere aqui para o caminho real do seu vídeo
    upload_video_to_drive(caminho_do_video)
