"""Class to store a message (operator overload, union types , default parameters)."""

class Email: 

    to: str
    message: str
    important: bool # Is the message important?

    def __init__(self, recipient: str | int, message_txt: str = "", importance_flag: bool = False):
        """Contructor of my email."""
        self.to = recipient
        self.message = message_txt
        self.important = importance_flag
    
    def __str__(self) -> str:
        """Make email print as a valid string instead of where it is located in computer space."""
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int):
        """Multiply email with a factor."""
        self.message *= factor

email_to_chiara: Email = Email("chiara", "You are a great TA!", False)
# email_to_chiara * 100
print(email_to_chiara)
email_to_lauren: Email = Email(123)
print(email_to_lauren)

