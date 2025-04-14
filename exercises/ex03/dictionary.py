"""We are going to work more with dictionaries!"""

__author__: str = "730561781"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values with each other"""
    result_dict: dict[str, str] = dict()
    for n in dictionary:
        if dictionary[n] in result_dict:
            raise KeyError("Key can't occur twice")
        result_dict[dictionary[n]] = n
    return result_dict


def count(stuff: list[str]) -> dict[str, int]:
    """Counts frequency of individual things in our 'stuff' or list"""
    freq_stuff: dict[str, int] = dict()
    for thing in stuff:
        if thing in freq_stuff:
            freq_stuff[thing] += 1
        else:
            freq_stuff[thing] = 1
    return freq_stuff


def favorite_color(dictnry: dict[str, str]) -> str:
    """Determines fav colour from dictionary"""
    freq_colours: dict[str, int] = {}

    for name in dictnry:
        # check the value and that to dictionary
        current_color = dictnry[name]
        if current_color in freq_colours:
            freq_colours[current_color] += 1
        else:
            freq_colours[current_color] = 1

    mostfreq: int = 0
    fav: str = ""

    for clr in freq_colours:
        if freq_colours[clr] > mostfreq:
            fav = clr
            mostfreq = freq_colours[clr]
    return fav


def bin_len(listy: list[str]) -> dict[int, set[str]]:
    """Bins certain strings into a compiled dictionary"""
    the_binned: dict[int, set[str]] = dict()
    for string in listy:
        length = len(string)
        if length in the_binned:
            the_binned[length].add(string)
        else:
            the_binned[length] = {string}
    return the_binned
