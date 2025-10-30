import json
from character_films import CharacterFilms

def main():
    character_film_list = []

    print("¡Iniciando el programa Star Wars!")
    print("Cargando datos desde el archivo JSON...")

    try:
        with open(r"C:\Users\Administrador\Desktop\LaSalle\DAM 2\Python\StarWars\StarWars.json", 'r', encoding='utf-8') as file:
            datos_star_wars = json.load(file)

        print(f"Archivo cargado correctamente. {len(datos_star_wars)} personajes encontrados.")

    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo JSON en la ruta especificada")
        return
    except json.JSONDecodeError:
        print("❌ Error: El archivo JSON tiene formato incorrecto")
        return

    for dato in datos_star_wars:
        fields = dato["fields"]

        personaje = CharacterFilms(
            edited=fields["edited"],
            name=fields["name"],
            created=fields["created"],
            gender=fields["gender"],
            skin_color=fields["skin_color"],
            hair_color=fields["hair_color"],
            height=fields["height"],
            eye_color=fields["eye_color"],
            mass=fields["mass"],
            homeworld=fields["homeworld"],
            birth_year=fields["birth_year"]
        )

        character_film_list.append(personaje)

    print(f"✅ {len(character_film_list)} personajes añadidos a la lista")

    print("\n--- BUSCANDO PERSONAJES ESPECÍFICOS ---")

    personajes_a_buscar = ["Luke Skywalker", "Chewbacca", "Anakin Skywalker"]

    for nombre_buscado in personajes_a_buscar:
        encontrado = False
        for personaje in character_film_list:
            if personaje.name == nombre_buscado:
                print(f"✅ Encontrado: {personaje.name}")

                if nombre_buscado == "Luke Skywalker":
                    personaje.set_num_of_films(5)  # Aparece en 5 películas principales
                    personaje.set_first_film("A New Hope")
                    personaje.set_alive_at_the_end(True)

                elif nombre_buscado == "Chewbacca":
                    personaje.set_num_of_films(6)
                    personaje.set_first_film("A New Hope")
                    personaje.set_alive_at_the_end(True)

                elif nombre_buscado == "Anakin Skywalker":
                    personaje.set_num_of_films(3)  # Como Anakin (no como Vader)
                    personaje.set_first_film("The Phantom Menace")
                    personaje.set_alive_at_the_end(False)  # Muere en Return of the Jedi

                info = personaje.get_info()
                print(f"   Información: {info}")
                print(f"   Películas: {personaje.num_of_films}, Primera: {personaje.first_film}, Vive al final: {personaje.alive_at_the_end}")

                encontrado = True
                break

        if not encontrado:
            print(f"❌ No encontrado: {nombre_buscado}")

    print("\n--- OPERACIONES CON LISTAS ---")

    nuevo_personaje = CharacterFilms(
        "2024-01-01T00:00:00.000Z",
        "Rey Skywalker",
        "2024-01-01T00:00:00.000Z",
        "female",
        "light",
        "brown",
        "170",
        "hazel",
        "54",
        "unknown",
        "15ABY"
    )
    character_film_list.append(nuevo_personaje)
    print(f"📝 Append: Añadido '{nuevo_personaje.name}' al final de la lista")

    otro_personaje = CharacterFilms(
        "2024-01-01T00:00:00.000Z",
        "Kylo Ren",
        "2024-01-01T00:00:00.000Z",
        "male",
        "fair",
        "black",
        "189",
        "hazel",
        "89",
        "unknown",
        "5ABY"
    )
    character_film_list.insert(0, otro_personaje)  # Al principio
    print(f"📝 Insert: Añadido '{otro_personaje.name}' en posición 0")

    if len(character_film_list) > 5:
        eliminado = character_film_list.pop(5)  # Elimina el 6to elemento
        print(f"🗑️ Pop: Eliminado '{eliminado.name}' de la posición 5")

    print(f"\n--- ESTADÍSTICAS FINALES ---")
    print(f"Total de personajes en la lista: {len(character_film_list)}")
    
    masculinos = sum(1 for p in character_film_list if p.gender == "male")
    femeninos = sum(1 for p in character_film_list if p.gender == "female")
    otros = len(character_film_list) - masculinos - femeninos

    print(f"👨 Masculinos: {masculinos}")
    print(f"👩 Femeninos: {femeninos}")
    print(f"🤖 Otros/robots: {otros}")

    print("\n--- EXPORTANDO A NUEVO JSON ---")

    datos_exportar = []
    for personaje in character_film_list:
        dato_personaje = {
            "name": personaje.name,
            "gender": personaje.gender,
            "birth_year": personaje.birth_year,
            "homeworld": personaje.homeworld,
            "num_of_films": personaje.num_of_films,
            "first_film": personaje.first_film,
            "alive_at_the_end": personaje.alive_at_the_end
        }
        datos_exportar.append(dato_personaje)

    try:
        with open("starwars_actualizado.json", 'w', encoding='utf-8') as file:
            json.dump(datos_exportar, file, indent=2, ensure_ascii=False)
        print("✅ Datos exportados correctamente a 'starwars_actualizado.json'")
    except Exception as e:
        print(f"❌ Error al exportar: {e}")

if __name__ == "__main__":
    main()
