import json
import urllib.request
import os

data = json.load(open('mihoyo-download-music.json', 'r', encoding='utf-8'))

save_dir = 'audio_files'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for i in range(1, 6):
    for j in range(1, 3):
        key = f"char-audio-{i}_{j}"
        url = data.get(key)
        if url:
            filename = f"{key}.mp3"
            filepath = os.path.join(save_dir, filename)
            urllib.request.urlretrieve(url, filepath)
            print(f"Downloaded {filename}")

print("All files downloaded and saved successfully.")