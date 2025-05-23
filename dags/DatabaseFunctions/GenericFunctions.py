from configparser import ConfigParser
import os

db_dir = os.path.join(os.path.dirname(__file__), "database.ini")

db_ini = os.path.abspath(db_dir)

def config(filename=db_ini, section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return db