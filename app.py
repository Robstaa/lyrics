#!flask/bin/python
from flask import Flask, request, render_template
from scrape_lyrics import get_lyrics_of_artist

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def my_form_post():
    artist = request.form['artist']
    number_of_songs = int(request.form['number_of_songs'])
    lyrics = get_lyrics_of_artist(
      artist=artist,
      number_of_songs=number_of_songs
    )
    return render_template('results.html', lyrics=lyrics, artist=artist)


if __name__ == '__main__':
    app.run(debug=True)
