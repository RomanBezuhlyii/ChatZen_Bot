import json
from lj_girl_class import LJGirls

def write(filename,lj: LJGirls):
    with open(filename, "wb") as fh:
        json.dump(lj,fh)

def read(filename):
    with open(filename, "rb") as fh:
        return json.load(fh)