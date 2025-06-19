# Исправленные тесты с параметризацией:
import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

class TestStringUtils:
    # Тесты для capitilize
    @pytest.mark.parametrize('string, expected', [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("123", "123"),
        ("тест", "Тест"),
        ("", ""),
        (" ", " "),
    ])
    def test_capitilize(self, utils, string, expected):
        assert utils.capitilize(string) == expected

    def test_capitilize_none(self, utils):
        with pytest.raises(AttributeError):
            utils.capitilize(None)

    # Тесты для trim
    @pytest.mark.parametrize('string, expected', [
        ("   skypro", "skypro"),
        ("  hello  ", "hello  "),
        ("   04 апреля 2023", "04 апреля 2023"),
        ("", ""),
        (" ", ""),
        ("\ttext", "\ttext"),  # Демонстрация известного бага
    ])
    def test_trim(self, utils, string, expected):
        assert utils.trim(string) == expected

    def test_trim_none(self, utils):
        with pytest.raises(AttributeError):
            utils.trim(None)

    # Тесты для to_list
    @pytest.mark.parametrize('string, delimeter, expected', [
        ("a,b,c", ",", ["a", "b", "c"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("apple orange banana", " ", ["apple", "orange", "banana"]),
        ("", ",", []),
        (" ", ",", []),
    ])
    def test_to_list(self, utils, string, delimeter, expected):
        assert utils.to_list(string, delimeter) == expected

    def test_to_list_none(self, utils):
        with pytest.raises(AttributeError):
            utils.to_list(None)

    # Тесты для contains
    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "S", True),
        ("SkyPro", "Pro", True),
        ("12345", "34", True),
        ("SkyPro", "s", False),
        ("", "a", False),
        (" ", " ", True),
    ])
    def test_contains(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    def test_contains_none(self, utils):
        with pytest.raises(AttributeError):
            utils.contains(None, "a")

    # Тесты для delete_symbol
    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "k", "SyPro"),
        ("Hello World", "o", "Hell Wrld"),
        ("123123", "2", "1313"),
        ("", "a", ""),
        (" ", " ", ""),
    ])
    def test_delete_symbol(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_symbol_none(self, utils):
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    # Тесты для starts_with
    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "S", True),
        ("12345", "1", True),
        (" Hello", " ", True),
        ("SkyPro", "s", False),
        ("", "a", False),
    ])
    def test_starts_with(self, utils, string, symbol, expected):
        assert utils.starts_with(string, symbol) == expected

    def test_starts_with_none(self, utils):
        with pytest.raises(AttributeError):
            utils.starts_with(None, "a")

    # Тесты для end_with
    @pytest.mark.parametrize('string, symbol, expected', [
        ("SkyPro", "o", True),
        ("12345", "5", True),
        ("Hello ", " ", True),
        ("SkyPro", "O", False),
        ("", "a", False),
    ])
    def test_end_with(self, utils, string, symbol, expected):
        assert utils.end_with(string, symbol) == expected

    def test_end_with_none(self, utils):
        with pytest.raises(AttributeError):
            utils.end_with(None, "a")

    # Тесты для is_empty
    @pytest.mark.parametrize('string, expected', [
        ("", True),
        (" ", True),
        ("  ", True),
        ("SkyPro", False),
        ("  hello  ", False),
    ])
    def test_is_empty(self, utils, string, expected):
        assert utils.is_empty(string) == expected

    def test_is_empty_none(self, utils):
        with pytest.raises(AttributeError):
            utils.is_empty(None)

    # Тесты для list_to_string
    @pytest.mark.parametrize('lst, joiner, expected', [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["a", "b", "c"], "-", "a-b-c"),
        ([], ", ", ""),
    ])
    def test_list_to_string(self, utils, lst, joiner, expected):
        assert utils.list_to_string(lst, joiner) == expected

    def test_list_to_string_none(self, utils):
        with pytest.raises(AttributeError):
            utils.list_to_string(None)
