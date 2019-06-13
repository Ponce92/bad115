from django.db      import connection
from main.models    import *

def getRoles():
    '''Funcion que retorna los roles que pueden ser editador por la aplicacion y
        por los usuarios de dicha aplicacion '''


