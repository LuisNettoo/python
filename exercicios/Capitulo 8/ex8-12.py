def make_sandwiches(*stuffings):
    print('The sandwich stuffings is:')
    for stuffing in stuffings:
        print("- " + stuffing.title())

make_sandwiches('beef', 'cheese', 'ketchup', 'mustard')
make_sandwiches('cheese', 'ketchup')
make_sandwiches('hamburguer')