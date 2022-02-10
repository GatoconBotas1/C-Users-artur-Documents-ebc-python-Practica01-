user = {
    "name": {'Paulo', 'Gasca'},
    "Edad": 18,
    "Ocupación": {"Estudiante"}
}

print(type(user))

for key in user:
    print(f'element[{key}]: {user[key]}')
    