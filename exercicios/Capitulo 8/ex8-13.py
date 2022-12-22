def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_info = build_profile('luis', 'neto', location='bom jesus', hobby='coding', skill='clean codes')

print(user_info)