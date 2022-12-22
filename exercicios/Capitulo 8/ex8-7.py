def make_album(name_artist, name_album, number_track=""):
    
    dici = {'name': name_artist, 'album': name_album}
    
    if number_track:
        dici['track'] = number_track
    
    return dici

ex1 = make_album('Micheal Jackson', 'Bad', number_track=12)
print(ex1)

ex2 = make_album('Billie Eilish', "Don't Smile at Me")
print(ex2)

ex3 = make_album('Justin Bieber', 'Justice', number_track=17)
print(ex3)