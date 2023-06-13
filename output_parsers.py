from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of a person")
    facts: List[str] = Field(description="Interesting facts about a person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest a person"
    )
    ice_breakers: List[str] = Field(
        description="Ice breakers to open a conversation with a person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
