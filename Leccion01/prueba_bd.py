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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@gmail.com')
            cursor.execute(sentencia, valores)
            # conexion.commit()  # commit guarda los cambios en la base de datos cuando no se usa el with
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
    conexion.close()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
