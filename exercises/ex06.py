"""Dictionary related utility functions."""

__author__ = "730660951"

# Define your functions below


def invert(given: dict[str, str]) -> dict[str, str]:
    """Keys of input list become the values of the output list and vice versa."""
    inverted: dict[str, str] = dict()
    for keys in given:
        if given[keys] in inverted:
            raise KeyError("More than one of same key!")
        inverted[given[keys]] = keys
    return inverted


def favorite_color(color: dict[str, str]) -> str:
    """Returns str with most frequent color."""
    fav: str = ""
    count: dict[str, int] = dict()
    for elem in color:
        if color[elem] in count:
            count[color[elem]] += 1
        else:
            count[color[elem]] = 1
    max: int = 0
    for colors in count:
        if count[colors] > max:
            max = count[colors]
            fav = colors
    return fav


def count(given: list[str]) -> dict[str, int]:
    """Values are the number of times each given value is present."""
    x: dict[str,int] = dict()
    for idx in given:
        if idx in x:
            x[given[idx]] += 1
        else:
            x[given[idx]] = 1
    return x


def alphabetizer(given: list[str]) -> dict[str, list[str]]:
    """Keys are first letter in given word, value is random word starting with that letter."""
    letter_dict: dict[str, list[str]] = dict()
    for word in given:
        if word in letter_dict:
            letter_dict[word[0]].append(word)
        else:
            letter_dict[word[0]] = [word]
    return letter_dict
 

def update_attendance(inp_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Mutate by adding names on same day to the dict and return dict."""
    attendance_log: dict[str, list[str]] = inp_log
    if day in attendance_log:
        inp_log[day].append(student)
    else:
        inp_log[day] = [student]
    return attendance_log