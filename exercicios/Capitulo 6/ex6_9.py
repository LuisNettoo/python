favorite_places = {
    'itallo': ['paris', 'imperatriz', 'argentina'],
    'marcos': ['são luis', 'palmas', 'bom jesus'],    
    'danilo': ['buriticupu', 'paraopebas', 'santa luzia'],
}

for name, place in favorite_places.items():
    print('\n' + 'Os lugares favoritos do ' + name.title() + ' são:')
    for p in place:
         print('\t'*4 + p.title())
    
        