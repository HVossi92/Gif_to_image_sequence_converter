import os.path
from pathlib import Path


def convert_video_to_image_sequence():
    input_directory_path = '/home/vossi/Documents/Master_Thesis/WebScraping/Scraped_Data/testFolder_gifs/'
    input_files = next(os.walk(input_directory_path))[2]
    output_directory = '/home/vossi/Documents/Master_Thesis/WebScraping/Scraped_Data/testFolder_gifs/cloud/'
    output_format = 'png'

    for idx, input_file in enumerate(input_files):
        print(f"Converting {idx + 1} / {len(input_files)}")
        input_file_path = input_directory_path + input_file
        throw_for_invalid_paths(input_file_path, output_directory)
        output_name = os.path.splitext(os.path.basename(input_file_path))[0]
        Path(output_directory + output_name).mkdir(parents=True, exist_ok=True)
        output_file = output_name + '%d.' + output_format
        command = "ffmpeg -i " + input_file_path + " -vf fps=12 " + output_directory + output_name + "/" + output_file
        print("command: " + command)
        os.system(command)


def throw_for_invalid_paths(input_file, output_directory):
    if not os.path.isfile(input_file):
        raise FileNotFoundError("Could not find input file", input_file)
    if not os.path.isdir(output_directory):
        raise FileNotFoundError("Could not find output directory", output_directory)


if __name__ == '__main__':
    convert_video_to_image_sequence()
