from sqlmodel import SQLModel, Field


class SuperHero(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}  # Default value

    # OBLIGATOIR
    id: int | None = Field(default=None, primary_key=True)
    name: str
