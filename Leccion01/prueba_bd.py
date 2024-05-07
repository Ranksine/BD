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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'  # %s es llamado placeholder o parametro posicional
            id_persona = input('Porporciona el valor id_persona: ')
            cursor.execute(sentencia, (id_persona,))
            # registros = cursor.fetchall  # Para recuperar todos los registros de la consulta
            registros = cursor.fetchone()  # Para recuperar un solo registro de la consulta

            print(registros)

    conexion.close()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
