"""We are going to work more with dictionaries!"""

__author__: str = "730561781"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values with each other"""
    result_dict: dict[str, str] = dict()
    for n in dictionary:
        if dictionary[n] in result_dict:
            raise KeyError(f"Key can't occur twice: {dictionary[n]}")
        result_dict[dictionary[n]] = n
    return result_dict


def count(stuff: list[str]) -> dict[str, int]:
    freq_stuff: dict[str, int] = dict()
    for thing in stuff:
        if thing in freq_stuff:
            freq_stuff[thing] += 1
        else:
            freq_stuff = 1
    return freq_stuff


def favorite_color(dict: dict[str, str]) -> str:
    clrs: list[str] = ()
    for clr in clrs:
        clrs.append(dict[clr])
    clr_count = count(clrs)
    mostfreq: int = 0
    fav: str = ""
    for clr in clr_count:
        if clr_count[clr] > mostfreq:
            fav = clr
            mostfreq = clr_count[clr]
    return fav


def bin_len(list: list[str]) -> dict[int, set[str]]:
    the_binned: dict[int, set[str]] = dict()
    for string in list:
        len = len(string)
        if len in the_binned:
            the_binned[len].add(string)
        else:
            the_binned[len] = {string}
    return the_binned
