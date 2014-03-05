import sys
from db import db

QUERY_TMPL = """
select descripcion, similarity(descripcion, '%s') as sml
from productos_preciosa
where descripcion %%%% '%s'
order by sml desc limit 10
"""

def sml(q):
    return db.query(QUERY_TMPL % (q, q))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print >>sys.stderr, "Uso: %s <busqueda>" % sys.argv[0]
        exit(1)

    print "Productos similares a `%s`: " % sys.argv[1]
    print
    for producto in sml(sys.argv[1]):
        print "%s\t\t%.4f" % (producto['descripcion'], producto['sml'])
    print
