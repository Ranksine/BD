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
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@gmail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@gmail.com', 2),
            )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
    conexion.close()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
