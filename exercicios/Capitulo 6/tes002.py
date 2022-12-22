favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python', 
    }

enquete = ['sarah', 'phil']

for name in sorted(favorite_languages.keys()):
    if name in enquete:
        print('\n{}, você devia participar da enquete!'.format(name.title()))
    else:
        print("\n{}, obrigado por participar da enquente!".format(name.title()))