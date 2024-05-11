from .interfaces import ContextBase, FileFactory

class CarbonTemplate:
    """
    Represents a template that can be rendered. 
    It consists of a list of file factories and a context.

    files: list[FileFactory] - List of file factories.
    context: ContextBase | dict - Context for the template.
    """
    files: list[FileFactory]
    context: ContextBase | dict

    def __init__(
            self,
            context: ContextBase | dict,
            files: list[FileFactory]):
        self.files = files
        self.context = context

    def render(self):
        if isinstance(self.context, dict):
            _context = self.context
        else:
            _context = self.context.generate()
            
        for factory in self.files:
            factory.render(_context)
