import pytest
import allure
from methods import Methods
from data import Data
from helpers import Messages


class TestFullList(Methods):

    @allure.title("Получение списка всех супергероев")
    def test_get_list_of_all_superheroes(self):
        response = self.get_list_of_all_superheroes()
        assert response.status_code == 200

    @allure.title("В полученном списке супергероев присутствует id")
    def test_id_in_list_of_superheroes(self):
        response = self.get_list_of_all_superheroes().json()
        for i in range(len(response)):
            assert "id" in response[i]


class TestFilter(Methods):

    @pytest.mark.parametrize("gender, work", Data.SUPERHEROES_GENDER_WORK)
    def test_filter_superheroes(self, gender, work):
        allure.dynamic.title(f"Создание списка супергероев, подходящих под критерии "
                             f"(пол - {gender}, наличие работы - {work})")
        superheroes = self.filter_superheroes(gender, work)
        assert superheroes != []

    @allure.title("Вызов ошибки при передаче в функцию создания списка супергероев пустой строки вместо пола")
    def test_filter_superheroes_empty_gender(self):
        with pytest.raises(ValueError) as exception:
            self.filter_superheroes("", True)
        assert str(exception.value) == Messages.NO_SUPERHEROES_ERROR

    @pytest.mark.parametrize("gender, work", Data.SUPERHEROES_WRONG_DATA_TYPE)
    def test_filter_superheroes_wrong_data_type(self, gender, work):
        allure.dynamic.title(f"Вызов ошибки при передаче в функцию создания списка супергероев некорректного типа данных "
                             f"(пол - {type(gender).__name__}, наличие работы - {type(work).__name__})")
        with pytest.raises(TypeError) as exception:
            self.filter_superheroes(gender, work)
        assert str(exception.value) == Messages.WRONG_TYPE_ERROR


class TestConvertHeight(Methods):

    @allure.title("Перевод роста супергероев в числовое значение в сантиметрах")
    def test_convert_height_to_number(self):
        list_with_cm = self.convert_height_to_number(Data.SUPERHEROES_NAME_HEIGHT)
        for hero in list_with_cm:
            assert type(hero.get("height")) is float

    @allure.title("Вызов ошибки при передаче в функцию конвертации роста пустого списка")
    def test_convert_height_empty_list(self):
        with pytest.raises(ValueError) as exception:
            self.convert_height_to_number([])
        assert str(exception.value) == Messages.EMPTY_LIST_ERROR

    @pytest.mark.parametrize("height", ["100 cm", 100, None])
    def test_convert_height_wrong_data_type(self, height):
        allure.dynamic.title(f"Вызов ошибки при передаче в функцию конвертации роста данных некорректного типа "
                             f"({type(height).__name__})")
        with pytest.raises(TypeError) as exception:
            self.convert_height_to_number(height)
        assert str(exception.value) == Messages.WRONG_TYPE_ERROR


class TestTallestHero(Methods):

    @pytest.mark.parametrize("gender, work", Data.SUPERHEROES_GENDER_WORK)
    def test_tallest_hero(self, gender, work):
        allure.dynamic.title(f"Определение самого высокого супергероя, подходящего под критерии "
                             f"(пол - {gender}, наличие работы - {work})")
        tallest_superhero = self.find_tallest_superhero(gender, work)
        assert tallest_superhero.get("name") != ""
        assert tallest_superhero.get("height") != 0

    @allure.title("Вызов ошибки при передаче в функцию определения самого высокого супергероя пустой строки вместо пола")
    def test_tallest_hero_empty_gender(self):
        with pytest.raises(ValueError) as exception:
            self.find_tallest_superhero("", True)
        assert str(exception.value) == Messages.NO_SUPERHEROES_ERROR

    @pytest.mark.parametrize("gender, work", Data.SUPERHEROES_WRONG_DATA_TYPE)
    def test_tallest_hero_wrong_data_type(self, gender, work):
        allure.dynamic.title(f"Вызов ошибки при передаче в функцию определения самого высокого супергероя некорректного "
                             f"типа данных (пол - {type(gender).__name__}, наличие работы - {type(work).__name__})")
        with pytest.raises(TypeError) as exception:
            self.find_tallest_superhero(gender, work)
        assert str(exception.value) == Messages.WRONG_TYPE_ERROR
