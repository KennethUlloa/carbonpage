from ..interfaces import TemplateEngine, FileFactory


class TemplateFactory:
    """
    FileFactory implementation using a template engine passed as parameter.

    The template engine should implement the `TemplateEngine` protocol.
    """
    path: str
    template: str
    content: str
    engine: TemplateEngine

    def __init__(self, engine: TemplateEngine, path: str, template: str = None, content: str = ""):
        self.engine = engine
        self.path = path
        self.template = template
        self.content = content
    
    def render(self, context: dict):
        import os

        filename = self.engine.render_string(self.path, context)

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        _content = self.content

        if not self.template:
            _content = self.engine.render_string(self.content, context)
        
        else:
            _content = self.engine.render_template(self.template, context)

        with open(filename, "w") as f:
            f.write(_content)
