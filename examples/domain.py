from typing import Optional, List

from pydantic import BaseModel


class Example(BaseModel):
    id: Optional[int]
    description: str
    text: str
    tags: List[str] = []
