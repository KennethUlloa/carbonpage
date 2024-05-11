from typing import Type
from jinja2 import Environment, FileSystemLoader
from carbonpage.templates import CarbonTemplate
from carbonpage.helpers.contexts import ProcessedContext
from carbonpage.helpers.factories import TemplateFactory
from carbonpage.helpers.processors import CamelCased, Get, SnakeCased, CLI


# Templates folder
TEMPLATES_FOLDER="templates"


_env = Environment(loader=FileSystemLoader(TEMPLATES_FOLDER))

class JinjaEngine:
    def render_template(self, template_name: str, context: dict) -> str:
        template = _env.get_template(template_name)
        return template.render(**context)
    
    def render_string(self, content: str, context: dict) -> str:
        template = _env.from_string(content)
        return template.render(**context)

_engine = JinjaEngine()

def file(path: str, template: str = None, content: str = "") -> TemplateFactory:
    return TemplateFactory(
        engine=_engine,
        path=path,
        template=template,
        content=content
    )


TEMPLATES = {
    "module": {
        "context": ProcessedContext(
            processed={
                "module_name": [
                    CLI(str, "Enter the module name"),
                    SnakeCased()
                    ],
                "cc_name": [
                    Get("module_name"),
                    CamelCased()
                ]
            }
        ),
        "files": [
            file(
                path="test/src/{{ module_name }}/entities/{{ module_name }}.py",
            ),
            file(
                path="test/src/{{ module_name }}/ports/repository.py",
            ),
            file(
                path="test/src/{{ module_name }}/usecases/dto.py",
            ),
            file(
                path="test/src/{{ module_name }}/adapters/repository.py",
            ),
            file(
                path="test/src/{{ module_name }}/controller.py",
            ),
        ]
    }
}