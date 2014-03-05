import json, sys
from db import db

def load_json(fname):
    productos = json.load(open(fname))

    table = db['productos_preciosa']

    for producto in productos:
        table.insert({
            'marca': producto['fields']['marca'],
            'descripcion': producto['fields']['descripcion'],
            'upc': producto['fields']['upc']
        })


if __name__ == '__main__':
    load_json(sys.argv[1])
