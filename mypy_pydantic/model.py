from pydantic import BaseModel, Field

class Model(BaseModel):
    field: str = Field(alias="alias")

    class Config:
        allow_population_by_field_name = True


model_with_field_name = Model(field="")
model_with_alias = Model(alias="")
