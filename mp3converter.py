# save this file as mp3converter.py
import os
import sys
from pydub import AudioSegment

def convert_to_mp3(base_dir):
    # Location of files
    dir_src = os.path.join(base_dir, 'Convert2Mp3/')
    dir_dst = os.path.join(base_dir, 'Converted/')
    dir_arch = os.path.join(base_dir, 'Archive/')  # Archive directory

    # File types to convert
    file_types = ['.m4a', '.amr', '.wav', '.aac']

    # Ensure directories exist, if not, create them
    for dir_path in [dir_src, dir_dst, dir_arch]:
        os.makedirs(dir_path, exist_ok=True)

    # Iterate over directory of files
    for filename in os.listdir(dir_src):
        name, extension = os.path.splitext(filename)
        # Check if file is any of the file types
        if extension in file_types:
            # Open file
            sound = AudioSegment.from_file(os.path.join(dir_src, filename))
            # Output file as mp3 to destination folder
            sound.export(os.path.join(dir_dst, name + '.mp3'), format="mp3")
            # Move the source file to archive directory
            os.rename(os.path.join(dir_src, filename), os.path.join(dir_arch, filename))

    print("All files have been converted and moved to the archive directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mp3converter.py /path/to/base/directory/")
        sys.exit(1)

    base_dir = sys.argv[1]
    convert_to_mp3(base_dir)