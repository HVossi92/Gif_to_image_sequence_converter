# Gif_to_image_sequence_converter
Converts all videos (e.g. gifs) inside a directory into image sequences

1. Set the input_directory_path, all files inside that directory will be converted
2. Set the output_directory, that's the destination for the converted files
3. Set the ouput format for the image sequences, e.g. "png" or "jpg"
4. Run, result = for every input video the script generates a directory with the same name and saves the image sequence inside

-Input_Files
  -File_1.gif
  -File_2.git
  
-Output_Files:
  -File_1:
    -File_1_1.png
    -File_1_2.png
    [...]
  -File_2:
    -File_2_1.png
    -File_2_2.png
    [...]
