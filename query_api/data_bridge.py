# Module to bridge API with ORM
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://cantor:navigational@localhost/cantor_proto')
Session = sessionmaker(bind=engine)
session = Session()

def text_query(text):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Dir_path: ", dir_path)
    print("Files: ", os.listdir())
    with open('query_api/ex1.geojson', 'r') as geofile:
        ex_geojson = json.load(geofile)
    return ex_geojson

def test_query(text):
    result = session.execute(text);
    session.commit()
    return {"Test":result.keys()[0]}
