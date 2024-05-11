from typing import Protocol, Type, Any, Callable


class Processor(Protocol):
    """
    Returns a processed value from a given context.
    """

    def process(self, current: Any, name: str, context: dict = None) -> Any:
        """
        Process the value and return the result.

        Args:
            current (Any): The current value.
            name (str): The key to process.
            context (dict): The context to use.
        
        Returns:
            Any: The processed value.
        """
        pass


class FileFactory(Protocol):
    """
    Creates a file from a given template and context.
    """
    def render(self, context: dict):
        pass


class ContextBase(Protocol):
    """
    Returns a context. Lets you define a context for a given template.
    """

    def generate(self) -> dict:
        pass


class TemplateEngine(Protocol):
    """
    Template engine interface. Allows you to use your preferred template engine by
    hiding the implementation details.
    """

    def render_string(self, content: str, context: dict) -> str:
        pass

    def render_template(self, template: str, context: dict) -> str:
        pass