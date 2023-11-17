"""Unit Testing EX06 Functions."""

__author__ = "730660951"

from exercises.ex06.dictionary import invert

from exercises.ex06.dictionary import favorite_color

from exercises.ex06.dictionary import count

from exercises.ex06.dictionary import alphabetizer

from exercises.ex06.dictionary import update_attendance

import pytest


def test_invert_1():
    """Test invert with one key and one corresponding value."""
    test_invert_dict: dict[str, str] = {"Batman": "Superman"}
    assert invert(test_invert_dict) == {"Superman": "Batman"}


def test_invert_2():
    """Test invert with two keys and two corresponding values."""
    test_invert_dict: dict[str, str] = {"Basketball": "Kobe", "Football": "Brady"}
    assert invert(test_invert_dict) == {"Kobe": "Basketball", "Brady": "Football"}
  

def test_invert_3():
    """Test invert with an empty dictionary should return {}."""
    # test_invert_dict: dict[str, str] = {}
    # assert invert(test_invert_dict) == {}
    with pytest.raises(KeyError):
        my_dictionary = {"Malcolm": "Akshar", "Andreas": "Akshar"}
        invert(my_dictionary)


def test_favorite_color_1():
    """Test favorite_color with a dictionary of 3 keys with 2 different colors."""
    test_color_dict: dict[str, str] = {"Malcolm": "blue", "Sam": "red", "Chap": "red"}
    assert favorite_color(test_color_dict) == "red"


def test_favorite_color_2():
    """Test favorite_color with a tie of colors."""
    test_color_dict: dict[str, str] = {"Malcolm": "blue", "Sam": "red", "Chap": "red", "Cyrus": "blue"}
    assert favorite_color(test_color_dict) == "blue"


def test_favorite_color_3():
    """Test favorite_color with an empty dictionary."""
    test_color_dict: dict[str, str] = {}
    assert favorite_color(test_color_dict) == ""


def test_count_1():
    """Test count if given a list with two different items in the list."""
    test_count_list: list[str] = {"Basketball", "Football"}
    assert count(test_count_list) == {"Basketball": 1, "Football": 1}


def test_count_2():
    """Test count with 3 different items in given list, two of which are the same item."""
    test_count_list: list[str] = {"Basketball", "Football", "Basketball"}
    assert count(test_count_list) == {"Basketball": 2, "Football": 1}


def test_count_3():
    """Test count with an empty list."""
    test_count_list: list[str] = {}
    assert count(test_count_list) == {}


def test_alphabetizer_1():
    """Test alphabetizer with a list that contains multiple words with uppercase first letters."""
    test_alphabetizer_list: list[str] = {"store", "Market", "Piano", "Giant"}
    assert alphabetizer(test_alphabetizer_list) == {"s": ["store"], "m": ["Market"], "p": ["Piano"], "g": ["Giant"]}


def test_alphabetizer_2():
    """Test alphabetizer with a list that contains multiple words with the same first letter."""
    test_alphabetizer_list: list[str] = {"store", "Market", "Piano", "Giant", "groceries", "matches"}
    assert alphabetizer(test_alphabetizer_list) == {"s": ["store"], "m": ["Market", "matches"], "p": ["Piano"], "g": ["Giant", "groceries"]}


def test_alphabetizer_3():
    """Test alphabetizer with an empty list."""
    test_alphabetizer_list: list[str] = {}
    assert alphabetizer(test_alphabetizer_list) == {"": []}


def test_update_attendance_1():
    """Test update_attendance with a given dictionary that adds multiple names into the dictionary under the same day."""
    test_attendence_log: dict[str, list[str]] = {"Monday": ["Cyrus", "CJ"], "Tuesday": ["Devin"]}
    test_attend_day: str = "Tuesday"
    test_attend_student: str = "Sam"
    assert update_attendance(test_attendence_log, test_attend_day, test_attend_student) == {"Monday": ["Cyrus", "CJ"], "Tuesday": ["Devin", "Sam"]}


def test_update_attendance_2():
    """Test update_attendance with a given dictionary that adds an additional day and names to dictionary."""
    test_attendence_log: dict[str, list[str]] = {"Monday": ["Cyrus", "CJ"], "Tuesday": ["Devin", "Sam"]}
    test_attend_day: str = "Wednesday"
    test_attend_student: str = "Andrew"
    assert update_attendance(test_attendence_log, test_attend_day, test_attend_student) == {"Monday": ["Cyrus", "CJ"], "Tuesday": ["Devin", "Sam"], "Wednesday": ["Andrew"]}


def test_update_attendance_3():
    """Test update_attendance with an empty dictionary."""
    test_attendence_log: dict[str, list[str]] = {}
    test_attend_day: str = ""
    test_attend_student: str = ""
    assert update_attendance(test_attendence_log, test_attend_day, test_attend_student) == {"", []}