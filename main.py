import os.path
from pathlib import Path


def convert_video_to_image_sequence(input_directory_path):
    input_files = next(os.walk(input_directory_path))[2]
    output_directory = '/home/vossi/Documents/Master_Thesis/WebScraping/Scraped_Data/Image_Sequences/'
    output_format = 'png'
    throw_for_invalid_path(input_directory_path)
    throw_for_invalid_path(output_directory)

    for idx, input_file in enumerate(input_files):
        input_file_path = input_directory_path + input_file
        output_name = os.path.splitext(os.path.basename(input_file_path))[0]
        Path(output_directory + output_name).mkdir(parents=True, exist_ok=True)
        output_file = output_name + '_%05d.' + output_format
        command = "ffmpeg -i '" + input_file_path + "' -vf fps=25 '" + output_directory + output_name + "/" + output_file + "'"
        print(f"Converting {idx + 1} / {len(input_files)}. Command: {command}")
        os.system(command)


def throw_for_invalid_path(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError("Could not find directory", directory)


if __name__ == '__main__':
    parent_directory = '/home/vossi/Documents/Master_Thesis/WebScraping/Scraped_Data/Gifs/'
    input_directory_paths = next(os.walk(parent_directory))[1]
    for directory_path in input_directory_paths:
        convert_video_to_image_sequence(parent_directory + directory_path + "/")
