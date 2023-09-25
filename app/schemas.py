from datetime import datetime
from typing import List
from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    id: str | None = None
    title: str
    content = str
    categories: str | None = None
    published: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_model = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListNote(BaseModel):
    status: str
    results: int
    notes: List[NoteBaseSchema]
