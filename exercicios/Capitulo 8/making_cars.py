def make_car(fabricante, modelo, **add_infos):
    car_info = {}
    
    car_info['fabricante'] = fabricante
    car_info['modelo'] = modelo
    
    for key, value in add_infos.items():
        car_info[key] = value
    
    return car_info
