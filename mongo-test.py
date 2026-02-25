from pymongo import MongoClient

MONGO_URI = "mongodb+srv://mendozajessie05_db_user:kzGNT8s2BWs5e4Dx@songs-db.kpawy3u.mongodb.net/?appName=songs-db"
client = MongoClient(MONGO_URI)

db = client['songs_list']
collection = db['songs']

# collection.insert_one({'name': 'Show', 'artist': 'Ado', 'image_url': 'https://i.scdn.co/image/ab67616d0000b273e204aafb5c393179c77c5253'})
# collection.insert_one({'name': 'Beleza Pula', 'artist': 'Masayoshi Takanaka', 'image_url': 'https://i.scdn.co/image/ab67616d0000b273c718e0f746b0f671fd92421e'})
# collection.insert_one({
#         "name" : "Loretta",
#         "artist" : "Ginger Root",
#         "image_url" : "https://i.scdn.co/image/ab67616d0000b2738e9876be6bd512f0ff86de9e"
#     })
# collection.insert_one({
#         "name" : "Off the Wall",
#         "artist" : "Michael Jackson",
#         "image_url" : "https://i.scdn.co/image/ab67616d0000b27344e53f6377a1e99e13779af9"
#     })
# collection.insert_one( {
#         "name": "Odo",
#         "artist": "Ado",
#         "image_url" : "https://i.scdn.co/image/ab67616d0000b2730f7bef8299e3738350d6846e"
#     })
# collection.insert_one({
#         "name" : "Ready to Fly",
#         "artist" : "Masayoshi Takanaka",
#         "image_url" : "https://i.scdn.co/image/ab67616d0000b273ae12b15f6e150833b0772848"
#     })


doc = collection.find_one({'artist': 'Ado'})
for f in collection.find():
    print(f)
# print(doc)