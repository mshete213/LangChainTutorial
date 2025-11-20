#pydantic is a library for data validation and typing
#pydantic is automatically installed with langchain

from typing import List

#base model is the base class for all pydantic models
#Field is a class that is used to define the fields of the model, default values, descriptions, other metadata
from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema for the response of the agent"""
    #source class was defined above, so we can use it here
    answer: str = Field(description="The agent's answer to the question")
    sources: List[Source] = Field(default_factory=list, description="The list of sources used to answer the question")


