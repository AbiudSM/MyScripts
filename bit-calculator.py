# size = kbps * time

import os

def get_size(target_size, video_duration):
    kbps = target_size * 1000 * 8 / video_duration
    print(f'kbps = {kbps}\nwo audio = {kbps - 128}')

def custom():
    target_size = float(input('Target size (MB): '))
    get_size(target_size, video_duration)

video_duration = float(input('Video duration (seg): '))

# ? whatsapp
print('===== WhatsApp =====')
get_size(16,video_duration)

opc = input('\n\nCustom? (y/n)')

if opc.lower() == 'y':
    custom()
    os.system('pause')