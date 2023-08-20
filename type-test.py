from typing import Annotated, Union


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(age: int, name: str | None = None):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: dict[str, float]):
    for item in items:
        print(item)


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.n


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"


print(get_full_name("john", "doe"))
