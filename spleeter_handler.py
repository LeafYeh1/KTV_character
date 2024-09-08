import os

def spearate_music(audio_name):
    try:
        os.system(f"spleeter separate -p spleeter:2stems -o {audio_name}-output {audio_name}.mp3")
        return "Separation successful"
    except Exception as e:
        return f"Error: {str(e)}"
