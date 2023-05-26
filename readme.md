Python script to convert audio file formats to .mp3

Usage via command prompt: python mp3converter.py /path/to/base/directory/

Assumes the following folder structure in your base directory

Base directory:
- Convert2Mp3/
- Converted/
- Archive/

Current file types that this recognizes, though it can be easily modified:
- .m4a
- .amr
- .wav

This script will convert these file types to .mp3. 

To run this program, add your files into the /Convert2Mp3/ directory.  Once run, the program will move those files to /Archive/ and will add the new .mp3 files into the /Converted/ directory. 

Dependencies:
- pydub, which has a dependency of ffmpeg


