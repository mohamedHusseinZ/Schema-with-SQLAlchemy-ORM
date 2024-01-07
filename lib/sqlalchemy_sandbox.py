#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.decelarative import decelarative_base

Base = decelarative_base()

class students(Base):
    id = Column(Integer(), primary_key=true)
    name = Column(String)

    if __name__ ='__name__':
        engine = create_engine('sqlite3 ///school.db')
        Base.metadata.create_all(engine)