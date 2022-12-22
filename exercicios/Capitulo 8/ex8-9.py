def make_great(magician):
    return 'o Grande ' + magician

def show_magicians(magicians):
    
    for magician in magicians:
        print(make_great(magician.title()))

names_magicians = ['mister m', 'hisoka', 'joker', 'pyong lee']

show_magicians(names_magicians[:])

print(names_magicians)