from typing import Any, Dict, List

from elasticsearch import Elasticsearch
from pydantic import BaseModel

from examples.domain import Example


class SearchQuery(BaseModel):
    description: str = ""
    text: str = ""
    tags: List[str] = []


# TODO: use elasticsearch_dsl
class ExamplesRepository:
    index_name = "examples"

    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    def create(self, example: Example) -> Example:
        self.es_client.index(index=self.index_name, body=example.json())
        return example

    def get_by_id(self, id_: str) -> Example:
        response = self.es_client.get(index=self.index_name, id=id_)
        return Example.parse_obj(response["_source"])

    def search(self, query: SearchQuery) -> List[Example]:
        response = self.es_client.search(index=self.index_name, body=self._build_query(query))
        return list(map(Example.parse_obj, response["hits"]["hits"]))

    @staticmethod
    def _build_query(query: SearchQuery) -> Dict[str, Any]:
        should_conditions = []

        if query.text:
            should_conditions.append({"match": {"text": query.text}})
        if query.description:
            should_conditions.append({"match": {"description": query.description}})
        if query.tags:
            should_conditions.append({"terms_set": {"tags": query.tags}})

        return {
            "query": {
                "bool": {
                    "should": should_conditions
                }
            }
        }
