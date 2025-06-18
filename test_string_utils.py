# import pytest
# from string_utils import StringUtils

# class TestStringUtils:
#     utils = StringUtils()

#     # Тесты для capitilize
#     def test_capitilize_positive(self):
#         assert self.utils.capitilize("skypro") == "Skypro"
#         assert self.utils.capitilize("hello world") == "Hello world"
#         assert self.utils.capitilize("123") == "123"
#         assert self.utils.capitilize("тест") == "Тест"

#     def test_capitilize_negative(self):
#         assert self.utils.capitilize("") == ""
#         assert self.utils.capitilize(" ") == " "
#         with pytest.raises(AttributeError):
#             self.utils.capitilize(None)

#     # Тесты для trim
#     def test_trim_positive(self):
#         assert self.utils.trim("   skypro") == "skypro"
#         assert self.utils.trim("  hello  ") == "hello  "
#         assert self.utils.trim("\ttest") == "\ttest"
#         assert self.utils.trim("   04 апреля 2023") == "04 апреля 2023"

#     def test_trim_negative(self):
#         assert self.utils.trim("") == ""
#         assert self.utils.trim(" ") == ""
#         with pytest.raises(AttributeError):
#             self.utils.trim(None)

#     # Тесты для to_list
#     def test_to_list_positive(self):
#         assert self.utils.to_list("a,b,c") == ["a", "b", "c"]
#         assert self.utils.to_list("1:2:3", ":") == ["1", "2", "3"]
#         assert self.utils.to_list("apple orange banana", " ") == ["apple", "orange", "banana"]

#     def test_to_list_negative(self):
#         assert self.utils.to_list("") == []
#         assert self.utils.to_list(" ") == []
#         with pytest.raises(AttributeError):
#             self.utils.to_list(None)

#     # Тесты для contains
#     def test_contains_positive(self):
#         assert self.utils.contains("SkyPro", "S") is True
#         assert self.utils.contains("SkyPro", "Pro") is True
#         assert self.utils.contains("12345", "34") is True

#     def test_contains_negative(self):
#         assert self.utils.contains("SkyPro", "s") is False
#         assert self.utils.contains("", "a") is False
#         assert self.utils.contains(" ", " ") is True
#         with pytest.raises(AttributeError):
#             self.utils.contains(None, "a")

#     # Тесты для delete_symbol
#     def test_delete_symbol_positive(self):
#         assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
#         assert self.utils.delete_symbol("Hello World", "o") == "Hell Wrld"
#         assert self.utils.delete_symbol("123123", "2") == "1313"

#     def test_delete_symbol_negative(self):
#         assert self.utils.delete_symbol("", "a") == ""
#         assert self.utils.delete_symbol(" ", " ") == ""
#         with pytest.raises(AttributeError):
#             self.utils.delete_symbol(None, "a")

#     # Тесты для starts_with
#     def test_starts_with_positive(self):
#         assert self.utils.starts_with("SkyPro", "S") is True
#         assert self.utils.starts_with("12345", "1") is True
#         assert self.utils.starts_with(" Hello", " ") is True

#     def test_starts_with_negative(self):
#         assert self.utils.starts_with("SkyPro", "s") is False
#         assert self.utils.starts_with("", "a") is False
#         with pytest.raises(AttributeError):
#             self.utils.starts_with(None, "a")

#     # Тесты для end_with
#     def test_end_with_positive(self):
#         assert self.utils.end_with("SkyPro", "o") is True
#         assert self.utils.end_with("12345", "5") is True
#         assert self.utils.end_with("Hello ", " ") is True

#     def test_end_with_negative(self):
#         assert self.utils.end_with("SkyPro", "O") is False
#         assert self.utils.end_with("", "a") is False
#         with pytest.raises(AttributeError):
#             self.utils.end_with(None, "a")

#     # Тесты для is_empty
#     def test_is_empty_positive(self):
#         assert self.utils.is_empty("") is True
#         assert self.utils.is_empty(" ") is True
#         assert self.utils.is_empty("  ") is True

#     def test_is_empty_negative(self):
#         assert self.utils.is_empty("SkyPro") is False
#         assert self.utils.is_empty("  hello  ") is False
#         with pytest.raises(AttributeError):
#             self.utils.is_empty(None)

#     # Тесты для list_to_string
#     def test_list_to_string_positive(self):
#         assert self.utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
#         assert self.utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
#         assert self.utils.list_to_string(["a", "b", "c"], "-") == "a-b-c"

#     def test_list_to_string_negative(self):
#         assert self.utils.list_to_string([]) == ""
#         with pytest.raises(AttributeError):
#             self.utils.list_to_string(None)


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