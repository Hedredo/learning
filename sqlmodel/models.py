from sqlmodel import SQLModel, Field


class SuperHero(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}  # Default value

    # OBLIGATOIR
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Hero(
    SQLModel, table=True
):  # If table=True, the Class acts a Table Model. If False, it acts as a Data Model (explain later).
    # OPTIONNEL  : Modifie la config de la table.
    __table_args__ = {"extend_existing": False}  # Default value

    # OBLIGATOIRE : Déclarer les attributs de classes dont l'équivalent en table
    id: int | None = Field(
        default=None, primary_key=True
    )  # Il est recommandé de mettre None en default_value d'où int | None. La table elle-même va générer la clé INT
    name: str  # Use Python standard annotations
    secret_name: (
        str  # Not setting a default value here is interpreted by SQL as NOT NULL.
    )
    age: int | None = (
        None  # Setting None as default value is interpreted by SQL as NULL. This field could be "NULL"
    )

class MinusHero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
