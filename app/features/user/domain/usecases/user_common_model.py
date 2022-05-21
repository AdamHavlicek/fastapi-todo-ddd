from pydantic import BaseModel, Field


class UserBaseModel(BaseModel):
    """
        UserBase common fields
    """
    email: str = Field(example='test@test.com')
