from random import randint
import json
import requests

class Pokemon:
    pokemons = {}


    

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.stats = self.get_stats()
        
        self.Pikachu : bool = False
        
        with open('achievements.json', 'r') as json_file:
            achievement = json_file.read()
            print(achievement)
            self.achievements_converted = json.loads(achievement)

        Pokemon.pokemons[pokemon_trainer] = self



    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return 'https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru'
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            self.Pikachu = True
            return "Pikachu"
        
    def achievements(self):
        if self.achievements_converted['achievements'][0]['get'] != True:
            with open('achievements.json', 'w') as json_file:
                self.achievements_converted['achievements'][0]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][0]['message']
        if self.pokemon_number == 6 and self.achievements_converted['achievements'][1]['get'] != True:
            with open('achievements.json', 'w') as json_file:
                self.achievements_converted['achievements'][1]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][1]['message']  
        if self.achievements_converted['achievements'][2]['get'] != True and self.Pikachu != False:
                self.achievements_converted['achievements'][2]['get'] = True
                self.New_achievements_Json = json.dumps(self.achievements_converted, indent=2)
                json_file.write(self.New_achievements_Json)
                # self.UpdateAch()
                # self.achievements()
                return self.achievements_converted['achievements'][2]['message']  
        else: 
            print('no achievements :"( ')    
            return


    def get_stats(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hp = data['stats'][0]['base_stat']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            special_attack = data['stats'][3]['base_stat']
            special_defense = data['stats'][4]['base_stat']
            speed = data['stats'][5]['base_stat']

            return f" \nhp: {hp} \nattack: {attack} \ndefense: {defense} \nspecial-attack: {special_attack} \nspecial-defense: {special_defense} \nspeed: {speed}"
        


    # Метод класса для получения информации
    def info(self):
        return f" Имя твоего покеомона: {self.name} \nстатистика: {self.stats}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



