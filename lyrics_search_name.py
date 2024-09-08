import requests
import urllib.parse
from bs4 import BeautifulSoup

def lyric_to_name(lyrics):
    try:
        converted_lyrics = urllib.parse.quote(lyrics)
        search_url = f"https://search.azlyrics.com/search.php?q={converted_lyrics}&x=d3164bfec6ed15dd56fbb3c94c3f5c6d6f37a9ea84b1980c4c61e72aa015acda"
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        b_tags = soup.find_all('b')
        result = []
        for b_tag in b_tags:
            if b_tag.get_text() == 'Lyrics results:':
                panel = b_tag.find_parent('div', class_='panel')
                tr_elements = panel.find_all('tr')
                for tr in tr_elements[:5]:
                    song_name = tr.find('span').text.strip()
                    result.append(song_name)
        return result
    except Exception as e:
        return f"Error: {str(e)}"
