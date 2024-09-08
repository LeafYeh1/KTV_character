from youtubesearchpython import VideosSearch

def findYT(search_words):
    try:
        result = VideosSearch(search_words, limit=1).result()["result"]
        if result:
            video_id = result[0]["id"]
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            return youtube_url
        else:
            return "No results found."
    except Exception as e:
        return f"Error: {str(e)}"
