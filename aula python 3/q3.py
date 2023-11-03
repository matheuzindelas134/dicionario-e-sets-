animal = {
    "Especie": "Cachorro",
    "Raça": "Pinscher",
    "Idade": int(input("Digite a idade do cachorro: ")),
    "Adestrado": True
    }
del animal["idade"]

print(animal)