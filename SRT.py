# -*- coding: utf-8 -*-

import re
import os

def split_text(text, max_length=500):
    sentences = re.split('(?<=[.!?]) +', text)
    srt_segments = []
    current_segment = ""

    for sentence in sentences:
        if len(current_segment) + len(sentence) <= max_length:
            current_segment += " " + sentence if current_segment else sentence
        else:
            if len(sentence) > max_length:  # Handle sentences longer than max_length
                if current_segment:
                    srt_segments.append(current_segment.strip().replace('\n', ' ').replace('  ', ' '))
                    current_segment = ""
                while len(sentence) > max_length:
                    part = sentence[:max_length].rsplit(' ', 1)[0]
                    srt_segments.append(part.strip().replace('\n', ' ').replace('  ', ' '))
                    sentence = sentence[len(part):].strip()
                current_segment = sentence
            else:
                srt_segments.append(current_segment.strip().replace('\n', ' ').replace('  ', ' '))
                current_segment = sentence

    if current_segment:
        srt_segments.append(current_segment.strip().replace('\n', ' ').replace('  ', ' '))

    return srt_segments


def create_srt(segments, start_index=0):
    srt_content = ""
    segment_duration = 20  # Duration of each segment in seconds
    pause_duration = 20  # Pause duration between segments in seconds

    for i, segment in enumerate(segments, start=start_index + 1):
        start_time = format_time((i - 1) * (segment_duration + pause_duration))
        end_time = format_time((i - 1) * (segment_duration + pause_duration) + segment_duration)
        srt_content += f"{i}\n{start_time} --> {end_time}\n{segment}\n\n"

    return srt_content.strip(), i


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    milliseconds = 0
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def write_srt_file(srt_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(srt_content)


def process_input_file(input_filename, i):
    with open(input_filename, 'r', encoding='utf-8') as file:
        input_text = file.read()

    parts = input_text.split('##########')
    for index, part in enumerate(parts):
        part = part.strip()
        if part:
            segments = split_text(part)
            srt_content, _ = create_srt(segments, start_index=index * len(segments))
            output_filename = f'C:\\Users\\kstack.pnascimento\\Desktop\\Demonstracao\\Legenda.srt'
            output_filenametxt = f'C:\\Users\\kstack.pnascimento\\Desktop\\Demonstracao\\Legenda.txt'
            #output_filenametxt = f'D:\\Peter\\YT\\Metodo\\CarlJung\\{i:03d}\\Legenda.txt'
            #output_filename = f'D:\\Peter\\YT\\Metodo\\CarlJung\\{i:03d}\\Legenda.srt'

            write_srt_file(srt_content, output_filename)
            write_srt_file(srt_content, output_filenametxt)
            print(f"SRT file created successfully: {output_filename}")


if __name__ == "__main__":
    for i in range(1, 61):  # Alterar o range conforme o número de arquivos VD existentes
        input_filename = f'C:\\Users\\kstack.pnascimento\\Desktop\\Demonstracao\\Tradnovo.txt'
        process_input_file(input_filename, i)