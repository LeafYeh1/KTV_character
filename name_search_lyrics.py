import requests
import urllib.parse
from bs4 import BeautifulSoup

def search_song_lyrics(song_name):
    try:
        converted_name = urllib.parse.quote(song_name)
        search_url = f"https://www.kkbox.com/tw/tc/search.php?word={converted_name}"
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        first_song_li = soup.find('song-li')
        if first_song_li:
            song_link = first_song_li.find('a', slot='song-name')['href']
            lyrics_page = requests.get(song_link)
            lyrics_page.raise_for_status()
            lyrics_soup = BeautifulSoup(lyrics_page.text, 'html.parser')
            lyrics = lyrics_soup.find('div', class_='lyrics').get_text()
            return lyrics
        else:
            return "No lyrics found."
    except Exception as e:
        return f"Error: {str(e)}"