from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base


engine = create_engine("sqlite:///./database/dev.sqlite")
session = Session(engine)
Base.metadata.create_all(engine)
