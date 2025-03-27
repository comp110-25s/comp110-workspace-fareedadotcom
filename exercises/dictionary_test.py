"""Unit test for our dictionary.py"""

__author__: str = "730561781"

with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)
