def make_album(name_artist, name_album, number_track=""):
    
    names = {'name': name_artist, 'album': name_album}
    
    if number_track:
        names['track'] = number_track
    
    return names

while True:
    
    print("\n(Em qualquer momento do programa digite 'q' e ENTER para sair!)")
    
    user_name_artist = str(input("Digite o nome de um artista: "))
    if user_name_artist == 'q':
        break
    
    user_name_album = str(input("Digite o nome de um album desse artista: "))
    if user_name_album == 'q':
        break
    
    result = make_album(user_name_artist, user_name_album)
    print(result)
