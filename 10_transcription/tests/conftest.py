import pytest
from functools import partial
from utils.text_handler import TextHandler
from utils.converter import Converter
from rules.russian_cyryllic.russian_cyryllic import russian_cyryllic


"""
Allows automatically injecting fixtures to a class test children.
https://hackebrot.github.io/pytest-tricks/fixtures_as_class_attributes/
"""

def _inject(cls, names):
    @pytest.fixture(autouse=True)
    def auto_injector_fixture(self, request):
        for name in names:
            setattr(self, name, request.getfixturevalue(name))

    cls.__auto_injector_fixture = auto_injector_fixture
    return cls

def auto_inject(*names):
    return partial(_inject, names=names)


""" Fixtures """

@pytest.fixture
def our_father_russian():
    return (
        "Молитва Господня."
        "Отче наш, сущий на небесах!"
        "да святится имя Твое;"
        "да приидет Царствие Твое;"
        "да будет воля Твоя и на земле, как на небе;"
        "хлеб наш насущный дай нам на сей день;"
        "и прости нам долги наши,"
        "как и мы прощаем должникам нашим;"
        "и не введи нас в искушение,"
        "но избавь нас от лукавого. Аминь."
    )

@pytest.fixture
def our_father_latin():
    return (
        "Molitwa Gospodnia."
        "Otcze nasz, suszczij na niebiesach!"
        "da swiatitsia imia Twoje;"
        "da priidiet Carstwije Twoje;"
        "da budiet wola Twoja i na ziemle, kak na niebie;"
        "chleb nasz nasuszcznyj daj nam na siej dienʹ;"
        "i prosti nam dołgi naszy,"
        "kak i my proszczajem dołżnikam naszym;"
        "i nie wwiedi nas w iskuszenije,"
        "no izbawʹ nas ot łukawogo. Aminʹ."
    )

@pytest.fixture
def text_handler(our_father_russian):
    return TextHandler(our_father_russian)

@pytest.fixture
def russian_rules():
    return russian_cyryllic

@pytest.fixture
def converter(text_handler, russian_rules):
    return Converter(text_handler, russian_rules)
