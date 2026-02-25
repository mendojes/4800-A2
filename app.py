from flask import Flask, render_template

app = Flask(__name__)

data = [
    {
        "name" : "Ready to Fly",
        "artist" : "Masayoshi Takanaka",
        "image_url" : "https://i.scdn.co/image/ab67616d0000b273ae12b15f6e150833b0772848"
    },
    {
        "name" : "Beleza Pula",
        "artist" : "Masayoshi Takanaka",
        "image_url" : "https://i.scdn.co/image/ab67616d0000b273c718e0f746b0f671fd92421e"
    },
    {
        "name" : "Loretta",
        "artist" : "Ginger Root",
        "image_url" : "https://i.scdn.co/image/ab67616d0000b2738e9876be6bd512f0ff86de9e"
    },
    {
        "name" : "Off the Wall",
        "artist" : "Michael Jackson",
        "image_url" : "https://i.scdn.co/image/ab67616d0000b27344e53f6377a1e99e13779af9"
    },
    {
        "name": "Odo",
        "artist": "Ado",
        "image_url" : "https://i.scdn.co/image/ab67616d0000b2730f7bef8299e3738350d6846e"
    },
    {
        "name": "Show",
        "artist": "Ado",
        "image_url": "https://i.scdn.co/image/ab67616d0000b273e204aafb5c393179c77c5253"
    },
]

@app.route('/')
def start_index():
    return render_template("index.html")


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
