# ffmpeg is required -> git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg

# size = kbps * time

import os, ffmpeg
import tkinter as tk
from tkinter import filedialog

def get_variables():
    root = tk.Tk()
    root.withdraw()

    target_size_list = [
        ('whatsapp', 16),
        ('messenger', 25)
    ]
    
    input_files = filedialog.askopenfilenames()

    return input_files, target_size_list    


def compress_video(video_full_path, output_file_name, target_size):
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'h264_nvenc', 'b:v': video_bitrate, 'f': 'mp4'}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'h264_nvenc', 'b:v': video_bitrate, 'c:a': 'aac', 'b:a': audio_bitrate}
                  ).overwrite_output().run()

if __name__ == '__main__':
    # ? git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
    os.chdir('ffmpeg/bin')


    input_files, target_size_list = get_variables()

    for input_file in input_files:

        splited_path = input_file.split('/')
        file_name = splited_path[-1]
        output_directory = '/'.join(splited_path[:-1]) + '/Compressed_' + file_name
        
        if (not os.path.exists(output_directory)):
            os.mkdir(output_directory)

        for app_name, target_size in target_size_list:
            
            output_file = f'{output_directory}/{app_name}_{file_name}'

            compress_video(input_file, output_file, target_size * 1000)