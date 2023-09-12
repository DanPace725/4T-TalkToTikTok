import subprocess

def convert_mp4_to_mp3(input_file, output_file):
    """
    Convert an MP4 file to MP3 using ffmpeg.

    Parameters:
    - input_file (str): Path to the input MP4 file.
    - output_file (str): Path to the output MP3 file.

    Returns:
    - None
    """
    command = [
        'ffmpeg',
        '-i', input_file,
        '-q:a', '0',  # Best quality audio
        '-map', 'a',
        output_file
    ]

    process = subprocess.run(command)
    return process.returncode == 0  # Return True if successful, False otherwise

convert_mp4_to_mp3("E:/Coding/4T/Whisper Trials/@reallyverycrunchy_video_7277547092736904494.mp4","testmp3.mp3")