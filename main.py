from data import api
from ui import interfaz, filtrar_datos


if __name__ == '__main__':
    limite_registros, nombredepartamento = interfaz.menu()
    datos = api.get_data(limite_registros, nombredepartamento)
    filtrar_datos = filtar_datos.filter_columns(datos)
    print(filtrar_datos)
