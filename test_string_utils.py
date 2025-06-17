import pytest
from string_utils import StringUtils

class TestStringUtils:
    utils = StringUtils()

    # Тесты для capitilize
    def test_capitilize_positive(self):
        assert self.utils.capitilize("skypro") == "Skypro"
        assert self.utils.capitilize("hello world") == "Hello world"
        assert self.utils.capitilize("123") == "123"
        assert self.utils.capitilize("тест") == "Тест"

    def test_capitilize_negative(self):
        assert self.utils.capitilize("") == ""
        assert self.utils.capitilize(" ") == " "
        with pytest.raises(AttributeError):
            self.utils.capitilize(None)

    # Тесты для trim
    def test_trim_positive(self):
        assert self.utils.trim("   skypro") == "skypro"
        assert self.utils.trim("  hello  ") == "hello  "
        assert self.utils.trim("\ttest") == "\ttest"
        assert self.utils.trim("   04 апреля 2023") == "04 апреля 2023"

    def test_trim_negative(self):
        assert self.utils.trim("") == ""
        assert self.utils.trim(" ") == ""
        with pytest.raises(AttributeError):
            self.utils.trim(None)

    # Тесты для to_list
    def test_to_list_positive(self):
        assert self.utils.to_list("a,b,c") == ["a", "b", "c"]
        assert self.utils.to_list("1:2:3", ":") == ["1", "2", "3"]
        assert self.utils.to_list("apple orange banana", " ") == ["apple", "orange", "banana"]

    def test_to_list_negative(self):
        assert self.utils.to_list("") == []
        assert self.utils.to_list(" ") == []
        with pytest.raises(AttributeError):
            self.utils.to_list(None)

    # Тесты для contains
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True
        assert self.utils.contains("SkyPro", "Pro") is True
        assert self.utils.contains("12345", "34") is True

    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "s") is False
        assert self.utils.contains("", "a") is False
        assert self.utils.contains(" ", " ") is True
        with pytest.raises(AttributeError):
            self.utils.contains(None, "a")

    # Тесты для delete_symbol
    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.utils.delete_symbol("Hello World", "o") == "Hell Wrld"
        assert self.utils.delete_symbol("123123", "2") == "1313"

    def test_delete_symbol_negative(self):
        assert self.utils.delete_symbol("", "a") == ""
        assert self.utils.delete_symbol(" ", " ") == ""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(None, "a")

    # Тесты для starts_with
    def test_starts_with_positive(self):
        assert self.utils.starts_with("SkyPro", "S") is True
        assert self.utils.starts_with("12345", "1") is True
        assert self.utils.starts_with(" Hello", " ") is True

    def test_starts_with_negative(self):
        assert self.utils.starts_with("SkyPro", "s") is False
        assert self.utils.starts_with("", "a") is False
        with pytest.raises(AttributeError):
            self.utils.starts_with(None, "a")

    # Тесты для end_with
    def test_end_with_positive(self):
        assert self.utils.end_with("SkyPro", "o") is True
        assert self.utils.end_with("12345", "5") is True
        assert self.utils.end_with("Hello ", " ") is True

    def test_end_with_negative(self):
        assert self.utils.end_with("SkyPro", "O") is False
        assert self.utils.end_with("", "a") is False
        with pytest.raises(AttributeError):
            self.utils.end_with(None, "a")

    # Тесты для is_empty
    def test_is_empty_positive(self):
        assert self.utils.is_empty("") is True
        assert self.utils.is_empty(" ") is True
        assert self.utils.is_empty("  ") is True

    def test_is_empty_negative(self):
        assert self.utils.is_empty("SkyPro") is False
        assert self.utils.is_empty("  hello  ") is False
        with pytest.raises(AttributeError):
            self.utils.is_empty(None)

    # Тесты для list_to_string
    def test_list_to_string_positive(self):
        assert self.utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert self.utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert self.utils.list_to_string(["a", "b", "c"], "-") == "a-b-c"

    def test_list_to_string_negative(self):
        assert self.utils.list_to_string([]) == ""
        with pytest.raises(AttributeError):
            self.utils.list_to_string(None)