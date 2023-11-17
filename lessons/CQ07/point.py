"""CQ07 Intro to Object Oriented Programming!"""

from __future__ import annotations


class Point:
    """This is my class to represent my Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Constructor."""
        self.x = x_init
        self.y = y_init
    
    def __str__(self) -> str:
        """Prints out points in a readable way!"""
        m_string: str = f"x: {self.x}; y: {self.y}"
        return m_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Returns a point multiplied my a factor."""
        p_string: Point = Point(self.x * factor, self.y * factor)
        return p_string
        
    def __add__(self, factor: int | float) -> Point:
        """Returns a point added by a factor."""
        a_string: Point = Point(self.x + factor, self.y + factor)
        return a_string
    
    def scale_by(self, factor: int) -> None:
        """Method belongs to Point class and mutates a Point."""
        self.x = self.x * factor
        self.y = self.y * factor
        
    def scale(self, factor: int) -> Point:
        """Method belongs to the Point Class and creates new Point."""
        new_coordinate: Point = Point(self.x * factor, self.y * factor)
        return new_coordinate