from typing import TypedDict, List

from examples.domain import Example
from examples.repositories import ExamplesRepository


class ExampleDTO(TypedDict):
    description: str
    text: str
    tags: List[str]


class SearchDTO(TypedDict):
    description: str
    text: str
    tags: str


class AppService:

    def __init__(self, examples_repository: ExamplesRepository):
        self._examples_repository = examples_repository

    def create_example(self, dto: ExampleDTO) -> Example:
        example = Example.parse_obj(dto)
        created = self._examples_repository.create(example)
        return created

    def search_example(self, dto: SearchDTO):
        pass
