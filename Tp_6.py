from list_ import List
from super_heroes_data import superheroes


def criterio_nombre(heroe):
    return heroe["name"]

def criterio_anio(heroe):
    return heroe["first_appearance"]

def criterio_casa(heroe):
    return heroe["casa"]

casas = {
    "Wolverine": "Marvel",
    "Dr Strange": "Marvel",
    "Capitana Marvel": "Marvel",
    "Mujer Maravilla": "DC",
    "Flash": "DC",
    "Star-Lord": "Marvel",
    "Linterna Verde": "DC",
}

for heroe in superheroes:
    nombre = heroe["name"]
    heroe["casa"] = casas.get(nombre, "Marvel")  


lista = List()
for heroe in superheroes:
    lista.append(heroe)


lista.add_criterion("name", criterio_nombre)
lista.add_criterion("year", criterio_anio)
lista.add_criterion("casa", criterio_casa)


lista.delete_value("Linterna Verde", "name")


pos = lista.search("Wolverine", "name")
if pos is not None:
    print("Wolverine apareció en:", lista[pos]["first_appearance"])


pos = lista.search("Dr Strange", "name")
if pos is not None:
    lista[pos]["casa"] = "Marvel"


print("\nHéroes con 'traje' o 'armadura':")
lista.sort_by_criterion("name")
for heroe in lista:
    bio = heroe["short_bio"].lower()
    if "traje" in bio or "armadura" in bio:
        print(heroe["name"])


print("\nHéroes antes de 1963:")
lista.sort_by_criterion("year")
for heroe in lista:
    if heroe["first_appearance"] < 1963:
        print(heroe["name"], "-", heroe["casa"])


for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    pos = lista.search(nombre, "name")
    if pos is not None:
        print(nombre, "->", lista[pos]["casa"])
    else:
        print(nombre, "no encontrado")


for nombre in ["Flash", "Star-Lord"]:
    pos = lista.search(nombre, "name")
    if pos is not None:
        print("\nInfo de", nombre, ":", lista[pos])


print("\nHéroes que empiezan con B, M o S:")
lista.sort_by_criterion("name")
for heroe in lista:
    if heroe["name"].startswith(("B", "M", "S")):
        print(heroe["name"])


conteo = {}
lista.sort_by_criterion("casa")
for heroe in lista:
    casa = heroe["casa"]
    conteo[casa] = conteo.get(casa, 0) + 1

print("\nCantidad de héroes por casa:")
for casa, cant in conteo.items():
    print(casa, ":", cant)
