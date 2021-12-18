# Gif_to_image_sequence_converter
Converts all videos (e.g. gifs) inside a directory into image sequences

1. Set the parent_directory, all folders inside that parent directory will be looped through
2. All gifs inside the child directories will be converted
3. Set the output_directory, that's the destination for the converted files
4. Set the output format for the image sequences, e.g. "png" or "jpg"
5. Run, result = for every input video the script generates a directory with the same name and saves the image sequence inside

- Parent_Directory:
  - Child_Directory_1
    - File_1_1.gif
    - File_1_2.git
  - Child_Directory_2
    - File_2_1.gif
    - File_2_2.git
  
- Output_Files:
  - File_1:
    - File_1_1.png
    - File_1_2.png
    - [...]
  - File_2:
    - File_2_1.png
    - File_2_2.png
    - [...]
