from flask import Flask

app = Flask(__name__)

data = [
    {
        "name" : "Brazilian Skies",
        "artist" : "Masayoshi Takanaka"
    },
    {
        "name" : "Beleza Pula",
        "artist" : "Masayoshi Takanaka"
    },
    {
        "name" : "Loretta",
        "artist" : "Ginger Root"
    },
    {
        "name" : "Off the Wall",
        "artist" : "Michael Jackson"
    },
]


@app.route('/welcome')
def welcome():  # put application's code here
    return 'Welcome to my app!'

@app.route('/search/<artist>')
def search(artist):
    artist = artist.lower()
    results = []
    for song in data:
        if artist.lower() in song["artist"].lower():
            results.append(song)
    return results


app.run(host='0.0.0.0')
