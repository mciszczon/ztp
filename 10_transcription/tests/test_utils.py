from utils.text_handler import TextHandler
from utils.converter import Converter


class TestTextHandler:

    def test_text_handler_creation(self, text_handler, our_father_russian):
        assert text_handler.source == our_father_russian

    def test_text_handler_words(self, text_handler):
        assert isinstance(text_handler.words, list)


class TestConverter:

    def test_converter_creation(self, text_handler, russian_rules, russian_constants, russian_lookups):
        converter = Converter(text_handler, russian_rules, russian_constants, russian_lookups)
        assert type(converter) == Converter
        assert type(converter.text_handler) == TextHandler
        assert type(converter.rules) == dict

    def test_converter_transpose(self, converter):
        assert converter._transpose('Аминь') == 'Aminʹ'
        assert converter._transpose('сущий') == 'suszczij'

    def test_converter_transposed(self, converter):
        assert type(converter.transposed) == str

    def test_converter_our_father(self, converter, our_father_russian, our_father_latin):
        assert converter.transposed == our_father_latin
