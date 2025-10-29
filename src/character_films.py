from character import Character

class CharacterFilms(Character):
    def __init__(self, edited, name, created, gender, skin_color,
                 hair_color, height, eye_color, mass, homeworld, birth_year):
        super().__init__(edited, name, created, gender, skin_color,
                         hair_color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films = None
        self.first_film = None
        self.alive_at_the_end = None

    def set_num_of_films(self, num):
        self.num_of_films = num

    def set_first_film(self, film):
        self.first_film = film

    def set_alive_at_the_end(self, alive):
        self.alive_at_the_end = alive