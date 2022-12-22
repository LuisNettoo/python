def city_country(city, country):
    get_formmated_name = city.title() + ', ' + country.title()
    return get_formmated_name

name_1 = city_country('bom jesus','brasil')
name_2 = city_country('vancouver','canada')
name_3 = city_country('chicago','estados unidos')

print(name_1)
print(name_2)
print(name_3)