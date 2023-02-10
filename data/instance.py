from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base


engine = create_engine("sqlite:///./data/db/dev.sqlite?check_same_thread=False")
Base.metadata.create_all(engine)
session = Session(engine)
