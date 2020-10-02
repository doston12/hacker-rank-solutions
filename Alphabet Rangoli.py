
def tracklist(**kwargs):
    for k, v in kwargs.items():
        print(k)
        for t, w in v.items():
            print('ALBUM:', t, 'TRACK:', w)

tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintegration": "Lovesong",
                "Wish": "Friday I'm in love",
                "Seventeen Seconds": "A Forest"})
