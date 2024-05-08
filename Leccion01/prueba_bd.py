import psycopg2


conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

# cursor = conexion.cursor()
# sentencia = 'SELECT * FROM persona'
# cursor.execute(sentencia)
# registros = cursor.fetchall()
# print(registros)
#
# cursor.close()
# conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada = input('Proporciona el id_persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
    conexion.close()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
