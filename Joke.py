from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field

class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline of the joke")
    rating: Optional[int] = Field(description="How funny the joke is, from 1 to 10")