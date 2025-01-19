#!/usr/bin/env python3
"""
This module demonstrates a wide variety of Python features that you might want
to test with different linters. It includes (but is not limited to):

- Classes (including a very complicated one with lots of moving parts)
- Functions
- Pydantic models
- List comprehensions (including if/else within them)
- Generators
- For loops
- While loops
- Conditionals
- and/or statements
- Lines of various lengths (including very long ones)
- Functions with many arguments
- Imports
- Short lines
- Comments
- Docstrings
- Tuple unpacking
- Named tuples with many fields
- Decorators
- A "helper" function
- A class using Python 3.10+ structural pattern matching (match/case)
- Nested if/else statements
- Nested function calls within a single class
- Complex logic
"""
import math, sys
import sys, os, json  # multiple imports on one line to test linting
from pathlib import Path
from pydantic import BaseModel, validator
from collections import namedtuple

from typing import (
    Any,
    List,
    Tuple,
    Optional,
    Generator,
    Callable,
    Union,
    Dict,
    Literal,
    TypeVar,
    Type,
    cast,
    overload,
)

LONG_LINE_VAR = "This is a super super super super super super super super super super super super super super super super long string that might cause line-length linting issues in some tools, and is intentionally placed here to test that scenario."

# Short line (minimal statement)
x = 1

# Tuple unpacking
first_value, second_value = (10, 20)

# A named tuple with many fields
LargeRecord = namedtuple(
    "LargeRecord",
    [
        "id",
        "name",
        "address",
        "city",
        "state",
        "zip_code",
        "country",
        "phone_number",
        "email",
        "website",
    ],
)


class User(BaseModel):
    """
    A Pydantic model representing a user with some validation.
    """

    username: str
    age: int

    # We add a validator as an example
    @validator("age")
    def check_age(cls, v):
        """
        Check that the user age is a positive integer.
        """
        if v < 0:
            raise ValueError("Age must be positive.")
        return v


class Product(BaseModel):
    """
    Another Pydantic model for demonstration.
    """

    name: str
    price: float

    # Example of a class method referencing self
    def to_json(self) -> str:
        """Return the JSON representation of the Product object."""
        return json.dumps(self.dict())


class MyUtilityClass:
    """
    A normal Python class with a couple of methods.
    """

    def __init__(self, name: str, value: int):
        """
        Initialize the utility class with some attributes.
        """
        self.name = name
        self.value = value

    def process(self):
        """
        Process something based on value.
        """
        # For loop example
        result = []
        for i in range(self.value):
            # Conditionals with and/or (showing multiple logical operations)
            if (i % 2 == 0 and i < 10) or (i > 15 and i % 3 == 0):
                result.append(i)
        return result


# Decorator example
def debug_output(func: Callable) -> Callable:
    """
    A simple decorator that prints debug information before and after the function call.
    """

    def wrapper(*args, **kwargs):
        print(f"[DEBUG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result}")
        return result

    return wrapper


@debug_output
def helper_function(a, b):
    """
    A helper function that just returns the sum of a and b, but is decorated for debug output.
    """
    return a + b


# Generator example
def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    A generator function that yields Fibonacci numbers up to a limit.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def tuple_unpacking_example() -> Tuple[int, int, int]:
    """
    A function that returns a tuple of three integers.
    """
    return 10, 20, 30


def multiple_args_function(
    first: int | float,
    second: int | float,
    third: int | float,
    fourth: int | float,
    fifth: int | float,
    sixth: int | float,
    seventh: int | float,
    eigth: int | float = 1,
    ninth: int | float = 2,
    flag: Optional[Any] = None,
):
    """
    A function with many arguments to test linting tools that check for excessive arguments.
    This function doesn’t do anything particularly meaningful; it’s just to demonstrate
    the ability to handle many parameters.
    """
    return (
        first
        + second
        + third
        + fourth
        + fifth
        + sixth
        + seventh
        + eigth
        + ninth
        + (0 if flag is None else 1)
    )


def create_users(names, starting_age=0) -> List[User]:
    """
    Use a list comprehension to create User objects from a list of names.
    """
    return [
        User(username=name, age=(idx + starting_age)) for idx, name in enumerate(names)
    ]


class VeryComplicatedClass:
    """
    A very complicated class with case matching, nested if/else statements,
    nested function calls, and complex logic.
    """

    def __init__(self, config: dict):
        """
        Initialize with a configuration dictionary.
        """
        self.config = config
        self.internal_state = {}

    def _internal_helper(self, key: str, value: int) -> int:
        """
        A nested helper function to transform values, simulating complex logic.
        """
        # Let's do some nested if/else logic here
        if key == "multiply":
            if value > 10:
                return value * 2
            else:
                return value * 3
        elif key == "add":
            if value < 0:
                # Another nested if
                if abs(value) > 100:
                    return value + 200
                else:
                    return value + 50
            else:
                return value + 10
        else:
            return value

    def _another_internal_helper(self, text: str) -> str:
        """
        Another helper function that manipulates strings based on internal rules.
        """
        if "error" in text.lower():
            return text.upper()
        elif "success" in text.lower():
            return text.capitalize()
        else:
            return text[::-1]  # reverse the string

    def process_config(self):
        """
        Processes the config, storing computed values in internal_state.
        This demonstrates match/case (Python 3.10+) and nested function calls.
        """
        for key, value in self.config.items():
            match value:  # structural pattern matching
                case str() as string_val:
                    transformed = self._another_internal_helper(string_val)
                    self.internal_state[key] = transformed
                case int() as int_val:
                    result = self._internal_helper(key, int_val)
                    self.internal_state[key] = result
                case list() as list_val:
                    # nested if/else with further logic
                    if len(list_val) > 5:
                        self.internal_state[key] = [
                            elem * 2
                            for elem in list_val
                            if isinstance(elem, (int, float))
                        ]
                    else:
                        # Nested function call scenario
                        new_list = []
                        for elem in list_val:
                            if isinstance(elem, int):
                                new_list.append(self._internal_helper("multiply", elem))
                            elif isinstance(elem, str):
                                new_list.append(self._another_internal_helper(elem))
                            else:
                                new_list.append(elem)
                        self.internal_state[key] = new_list
                case dict() as dict_val:
                    # Even more complex nested logic
                    nested_result = {}
                    for d_key, d_value in dict_val.items():
                        if isinstance(d_value, int):
                            nested_result[d_key] = self._internal_helper("add", d_value)
                        elif isinstance(d_value, str):
                            nested_result[d_key] = self._another_internal_helper(
                                d_value
                            )
                        else:
                            nested_result[d_key] = d_value
                    self.internal_state[key] = nested_result
                case _:
                    # Catch-all for other types
                    self.internal_state[key] = value

    def show_state(self):
        """
        Prints the internal state after processing.
        """
        print("VeryComplicatedClass internal state:", self.internal_state)


def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple = (1, 2, 3, "a")
    some_variable = {
        "long": "Long code lines should be wrapped within 79 characters.",
        "other": [
            math.pi,
            100,
            200,
            300,
            9876543210,
            "This is a long string that goes on",
        ],
        "more": {
            "inner": "This whole logical line should be wrapped.",
            some_tuple: [1, 20, 300, 40000, 500000000, 60000000000000000],
        },
    }
    return (some_tuple, some_variable)


def example2():
    return {"has_key() is deprecated": True}.has_key({"f": 2}.has_key(""))


class Example3(object):
    def __init__(self, bar):
        # Comments should have a space after the hash.
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)


def main():
    """
    Main function to demonstrate usage.
    """

    # Creating and validating Pydantic model instances
    user1 = User(username="Alice", age=30)
    user2 = User(username="Bob", age=25)

    product1 = Product(name="Widget", price=19.99)

    # Show JSON representation from a Pydantic model
    print("User 1:", user1.dict())
    print("User 2:", user2.dict())
    print("Product:", product1.to_json())

    # Demonstrate MyUtilityClass
    utility_instance = MyUtilityClass(name="UtilityTest", value=20)
    processed_values = utility_instance.process()
    print("Processed values:", processed_values)

    # Fibonacci generator usage
    fib_limit = 50
    fib_numbers = list(fibonacci_generator(fib_limit))
    print(f"Fibonacci numbers up to {fib_limit}:", fib_numbers)

    # Function with many arguments
    sum_of_args = multiple_args_function(1, 2, 3, 4, 5, 6, 7, 8)
    print("Sum of arguments (1-8 + defaults):", sum_of_args)

    # List comprehension with if/else
    big_list = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    numbers_with_sign = [number if number % 2 == 0 else -number for number in big_list]
    print("List with if/else in comprehension:", numbers_with_sign)

    # A complicated conditional with multiple and/or statements
    if (len(numbers_with_sign) > 10 and sum(numbers_with_sign) < 0) or (
        numbers_with_sign[0] == -1 and sum(numbers_with_sign) > 100
    ):
        print("A complicated condition is met!")
    else:
        print("A complicated condition is not met!")

    # Nested function calls and min/max usage
    print(min(numbers_with_sign, numbers_with_sign, len(fib_numbers)))

    # List of Pydantic Users via list comprehension
    user_list = create_users(["Charlie", "Diana", "Eve"], starting_age=20)
    for idx, u in enumerate(user_list):
        print(f"User #{idx}: {u.username}, age {u.age}")

    # Demonstrate while loop
    count = 0
    while count < 3:
        print(f"While loop count: {count}")
        count += 1

    # Testing a helper function that uses a decorator
    helper_result = helper_function(10, 20)
    print("Helper function result:", helper_result)

    # Testing the existence of an OS environment variable (simple conditional usage)
    if "HOME" in os.environ:
        print("HOME environment variable is set.")
    else:
        print("HOME environment variable is not set.")

    # Checking some path existence with Path from pathlib
    home_path = Path(os.environ.get("HOME", "/tmp"))
    if home_path.exists():
        print("Home path exists:", home_path)
    else:
        print("Home path does not exist:", home_path)

    # Demonstrate creating and printing a named tuple
    record = LargeRecord(
        id=1,
        name="John Doe",
        address="123 Main St",
        city="Springfield",
        state="State",
        zip_code="12345",
        country="USA",
        phone_number="555-1234",
        email="john@example.com",
        website="www.example.com",
    )
    print("Named tuple record:", record)

    # Use our VeryComplicatedClass
    complex_config = {
        "multiply": 12,
        "add": -20,
        "textData": "This might be an error message",
        "listData": [5, "hello", 3.14, -2, 10],
        "anotherList": [1, 2, 3, 4, 5, 6, 7],
        "nestedDict": {"innerInt": 5, "innerText": "SUCCESS CASE", "ignored": 3.1415},
        "unhandledType": set([1, 2, 3]),
    }

    complicated_instance = VeryComplicatedClass(complex_config)
    complicated_instance.process_config()
    complicated_instance.show_state()

    # Just a final print to show off the super long variable
    print(LONG_LINE_VAR)

    # Tuple unpacking example
    first_variable, second_interger, third_number = tuple_unpacking_example()
    print("Tuple unpacking example:", first_variable, second_interger, third_number)


if __name__ == "__main__":
    main()
