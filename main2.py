# import yt_dlp
# import json
# import os
# import re

# def sanitize_filename(name):
#     return re.sub(r'[\\/*?:"<>|]', "_", name)

# def download_youtube_playlist(playlist_url, base_output_dir="downloads_final", ffmpeg_path='D:/ffmpeg/bin'):
#     os.makedirs(base_output_dir, exist_ok=True)

#     # First get the playlist info
#     ydl_opts_initial = {
#         'quiet': True,
#         'skip_download': True,
#         'extract_flat': False,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts_initial) as ydl:
#         playlist_info = ydl.extract_info(playlist_url, download=False)

#     entries = playlist_info.get("entries", [playlist_info])

#     print(f"Found {len(entries)} videos. Starting download...\n")

#     for entry in entries:
#         video_url = entry['url'] if '_type' in entry and entry['_type'] == 'url' else entry['webpage_url']

#         with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
#             video_info = ydl.extract_info(video_url, download=False)

#         title = sanitize_filename(video_info.get('title', 'unknown'))
#         output_dir = os.path.join(base_output_dir, title)
#         os.makedirs(output_dir, exist_ok=True)

#         print(f"🔽 Downloading: {title}")

#         # Set per-video download options
#         ydl_opts = {
#             'ffmpeg_location': ffmpeg_path,
#             'format': 'bestaudio/best',
#             'outtmpl': os.path.join(output_dir, f'{title}.%(ext)s'),
#             'noplaylist': True,
#             'quiet': False,
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '192',
#             }],
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=True)

#         # Save metadata
#         metadata = {
#             'id': info.get('id'),
#             'title': info.get('title'),
#             'description': info.get('description'),
#             'duration': info.get('duration'),
#             'channel': info.get('channel'),
#             'uploader': info.get('uploader'),
#             'upload_date': info.get('upload_date'),
#             'view_count': info.get('view_count'),
#             'like_count': info.get('like_count'),
#             'tags': info.get('tags'),
#             'language': info.get('language'),
#             'webpage_url': info.get('webpage_url'),
#         }

#         json_path = os.path.join(output_dir, f"{title}.json")
#         with open(json_path, 'w', encoding='utf-8') as f:
#             json.dump(metadata, f, ensure_ascii=False, indent=4)

#         print(f"✅ Done: {title}\n    ↳ Audio: {title}.mp3\n    ↳ Metadata: {title}.json\n")



# # 🧪 Example usage:
# playlist_url = "https://www.youtube.com/playlist?list=PLPDzF0B97OtFNS5ZEIHZcN-10aWjDp6eM"
# download_youtube_playlist(playlist_url)



import os 
import json

path = "D:\web-dev\jetpack_hackthon\downloads_final"

for folder in os.listdir(path):
    for file in os.listdir(os.path.join(path, folder)):
        if "filtered" in file:
            json_path = os.path.join(path, folder, file)
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            x = (data["description"])
            x=x.split("\n")
            x=x[0]
            print(x)
            print("========================================")
            data["description_final"] = x
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
