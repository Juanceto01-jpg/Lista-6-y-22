from typing import Any, Optional

class List(list):

    CRITERION_FUNCTIONS = {}

    def add_criterion(
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        for element in self:
            print(element)

    def delete_value(
        self,
        value,
        key_value: str = None, # type: ignore
    ) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(
        self,
        criterion_key: str = None, # type: ignore
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(
        self,
        search_value,
        search_key: str = None, # type: ignore
    ) -> int: # type: ignore
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None # type: ignore

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2


jedi = [
    {"name": "Ahsoka Tano", "masters": ["Anakin Skywalker"], "lightsabers": ["verde", "azul", "blanco"], "species": "Togruta"},
    {"name": "Kit Fisto", "masters": ["Yoda"], "lightsabers": ["verde"], "species": "Nautolano"},
    {"name": "Luke Skywalker", "masters": ["Obi-Wan Kenobi", "Yoda"], "lightsabers": ["azul", "verde"], "species": "Humano"},
    {"name": "Yoda", "masters": [], "lightsabers": ["verde"], "species": "Desconocida"},
    {"name": "Qui-Gon Jinn", "masters": ["Conde Dooku"], "lightsabers": ["verde"], "species": "Humano"},
    {"name": "Mace Windu", "masters": ["Cyslin Myr"], "lightsabers": ["violeta"], "species": "Humano"},
    {"name": "Anakin Skywalker", "masters": ["Obi-Wan Kenobi"], "lightsabers": ["azul"], "species": "Humano"},
    {"name": "Obi-Wan Kenobi", "masters": ["Qui-Gon Jinn"], "lightsabers": ["azul"], "species": "Humano"},
    {"name": "Aayla Secura", "masters": ["Quinlan Vos"], "lightsabers": ["azul"], "species": "Twi'lek"},
]


lista = List()
for jed in jedi:
    lista.append(jed)


def criterio_nombre(j): return j["name"]
def criterio_especie(j): return j["species"]

lista.add_criterion("name", criterio_nombre)
lista.add_criterion("species", criterio_especie)


print("\n(a) Listado ordenado por nombre:")
lista.sort_by_criterion("name")
lista.show()

print("\n(a) Listado ordenado por especie:")
lista.sort_by_criterion("species")
lista.show()



print("\n(b) Info de Ahsoka Tano y Kit Fisto:")
for nombre in ["Ahsoka Tano", "Kit Fisto"]:
    pos = lista.search(nombre, "name")
    if pos is not None:
        print(lista[pos])



print("\n(c) Padawans de Yoda:")
for jed in lista:
    if "Yoda" in jed["masters"]:
        print(jed["name"])

print("\n(c) Padawans de Luke Skywalker:")
for jed in lista:
    if "Luke Skywalker" in jed["masters"]:
        print(jed["name"])



print("\n(d) Jedi humanos y twi'lek:")
for jed in lista:
    if jed["species"].lower() in ["humano", "twi'lek"]:
        print(jed["name"], "-", jed["species"])



print("\n(e) Jedi que comienzan con A:")
lista.sort_by_criterion("name")
for jed in lista:
    if jed["name"].startswith("A"):
        print(jed["name"])



print("\n(f) Jedi con más de un color de sable:")
for jed in lista:
    if len(set(jed["lightsabers"])) > 1:
        print(jed["name"], "-", jed["lightsabers"])



print("\n(g) Jedi con sable amarillo o violeta:")
for jed in lista:
    if "amarillo" in jed["lightsabers"] or "violeta" in jed["lightsabers"]:
        print(jed["name"], "-", jed["lightsabers"])



print("\n(h) Padawans de Qui-Gon Jinn:")
for jed in lista:
    if "Qui-Gon Jinn" in jed["masters"]:
        print(jed["name"])

print("\n(h) Padawans de Mace Windu:")
for jed in lista:
    if "Mace Windu" in jed["masters"]:
        print(jed["name"])
