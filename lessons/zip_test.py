"""Test my zip function."""

__author__ = "730660951"

from lessons.zip import zip


def test_zip_empty() -> None:
    """Test zip([],[]) should return {}."""
    assert zip([], []) == {}


def test_zip_multiple_positives() -> None:
    """Test Zip with a list of multiple elements being positive keys."""
    assert zip(["Happy", "Friday"], [1, 2]) == {"Happy": 1, "Friday": 2}


def test_zip_one_negative() -> None:   
    """Zip with a list of one element being a negative key.""" 
    assert zip(["Hello"], [-1]) == {"Hello": -1}