def show_magicians(magicians):
    
    for magician in magicians:
        print(magician.title())

def make_great(lista):
    print(['O grande' + lista for list in lista])

names_magicians = ['mister m', 'hisoka', 'joker', 'pyong lee']

show_magicians(make_great(names_magicians))

