Pokemons = ["pikachu", "ggoboogie", "pairi"]


def insert_data(position, pokemon):
    if position < 0 or position > len(Pokemons):
        print("Out of range")
        return

    Pokemons.append(None)
    pLen = len(Pokemons)

    for i in range(pLen - 1, position, -1):
        Pokemons[i] = Pokemons[i - 1]
        Pokemons[i - 1] = None

    Pokemons[position] = pokemon


insert_data(2, "yadoran")
print(Pokemons)


def delete_data(position):
    if position < 0 or position > len(Pokemons):
        print("Out of range")
        return

    pLen = len(Pokemons)
    Pokemons[position] = None

    for i in range(position+1, pLen):
        Pokemons[i-1]=Pokemons[i]
        Pokemons[i]=None

    del(Pokemons[pLen-1])

delete_data(1)
print(Pokemons)