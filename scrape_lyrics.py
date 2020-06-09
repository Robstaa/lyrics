import requests
from bs4 import BeautifulSoup

LYRICS_COM_ROOT = 'http://lyrics.com'
LYRICS_COM_ARTIST_ROOT = 'https://www.lyrics.com/artist/'


def get_lyrics_of_artist(artist, number_of_songs):
    links = []
    res = requests.get(f'{LYRICS_COM_ARTIST_ROOT}{artist}')
    soup = BeautifulSoup(res.text, 'html.parser')
    song_links = soup.find_all(
      'td', {'class': 'tal qx'},
      limit=number_of_songs
    )
    for song_link in song_links:
        link_path = song_link.a.get('href')
        links.append(LYRICS_COM_ROOT + link_path)
    links = list(set(links))

    lyrics = []
    for link in links:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        lyrics_body = soup.find(id="lyric-body-text").get_text().replace('\n', '<br/>')
        name = soup.find(id="lyric-title-text").get_text()
        lyrics.append({'text': lyrics_body, 'name': name})

    return lyrics
