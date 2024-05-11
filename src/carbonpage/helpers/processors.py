from typing import Type
from ..interfaces import Processor


class Get(Processor):
    """
    Get a value from the context.
    """
    def __init__(self, key: str):
        self.key = key

    def process(self, current, name: str, context: dict):
        return context.get(self.key)

class CLI(Processor):
    """
    Get a value from the command line, transforming it to the specified type. 
    Shows a prompt to the user.
    """
    dtype: Type
    prompt: str

    def __init__(self, dtype: Type, prompt: str):
        self.dtype = dtype
        self.prompt = prompt

    def process(self, current, name: str, context: dict):
        return self.dtype(input(self.prompt+" >> "))
    

class CamelCased(Processor):
    """
    Returns a camel cased string from a given context.
    """

    def __init__(self, force_str: bool = False):
        self.force_str = force_str

    def process(self, current, name: str, context: dict):
        value = current

        if not value:
            raise ValueError(f"Value {value} is empty.")

        if self.force_str:
            value = str(value) if not isinstance(value, str) else value
        
        return value.replace("_", " ").title().replace(" ", "")


class SnakeCased(Processor):
    """
    
    """

    def __init__(self, force_str: bool = False):
        self.force_str = force_str

    def process(self, current, name: str, context: dict):
        value = current

        if not value:
            raise ValueError(f"Value {value} is empty.")

        if self.force_str:
            value = str(value) if not isinstance(value, str) else value
        
        return value.lower().replace(" ", "_")
    