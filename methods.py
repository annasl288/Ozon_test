import requests
import allure
from helpers import Urls, Const, Messages


class Methods:

    @allure.step("Получить список всех супергероев")
    def get_list_of_all_superheroes(self):
        return requests.get(f"{Urls.BASE_URL}{Urls.ALL}")

    @allure.step("Создать список супергероев, подходящих под критерии")
    def filter_superheroes(self, gender: str, is_employed: bool) -> list:
        if not isinstance(gender, str) or not isinstance(is_employed, bool):
            raise TypeError(Messages.WRONG_TYPE_ERROR)
        response = self.get_list_of_all_superheroes().json()
        superheroes = []
        for hero in response:
            if hero.get("appearance").get("gender") == gender:
                if ((hero.get("work").get("occupation") == "-" and is_employed is False)
                        or (hero.get("work").get("occupation") != "-" and is_employed is True)):
                    new_hero = {"name": hero.get("name"), "height": hero.get("appearance").get("height")[1]}
                    superheroes.append(new_hero)
        if superheroes == []:
            raise ValueError(Messages.NO_SUPERHEROES_ERROR)
        return superheroes

    @allure.step("Перевести рост супергероев в числовое значение в сантиметрах")
    def convert_height_to_number(self, superheroes: list) -> list:
        height_converted = []
        if not isinstance(superheroes, list):
            raise TypeError(Messages.WRONG_TYPE_ERROR)
        if superheroes == []:
            raise ValueError(Messages.EMPTY_LIST_ERROR)
        for hero in superheroes:
            height = hero.get("height")
            if height.endswith("meters"):
                hero["height"] = float(height.replace(" meters", "")) * Const.CM
                height_converted.append(hero)
            elif height.endswith("cm"):
                hero["height"] = float(height.replace(" cm", ""))
                height_converted.append(hero)
            else:
                print(Messages.WRONG_HEIGHT, hero)
        return height_converted

    @allure.step("Определить самого высокого супергероя в списке")
    def find_tallest_superhero(self, gender: str, is_employed: bool) -> dict:
        if not isinstance(gender, str) or not isinstance(is_employed, bool):
            raise TypeError(Messages.WRONG_TYPE_ERROR)
        filtered_list = self.filter_superheroes(gender, is_employed)
        list_with_cm = self.convert_height_to_number(filtered_list)
        tallest_superhero = {"name": "", "height": 0}
        for hero in list_with_cm:
            height = hero.get("height")
            name = hero.get("name")
            if height > tallest_superhero.get("height"):
                tallest_superhero["name"] = name
                tallest_superhero["height"] = height
        print(f"Самый высокий супергерой - {tallest_superhero.get("name")} с ростом {tallest_superhero.get("height")} см.")
        return tallest_superhero
