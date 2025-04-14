"""Unit test for our dictionary.py"""

__author__: str = "730561781"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len

def test_invert(dic) -> None:
    assert invert({"day": "night", "hi": "bye"}) == {"night": "day", "bye":"hi"}
    assert invert({"true": "false"}) == {"false": "true"}

    # edge case 
    


def test_count():


def test_favorite_color():

def test_bin_len():


with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    test_invert(my_dictionary)
