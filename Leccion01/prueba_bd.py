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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  # %s es llamado placeholder o parametro posicional

            # llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()  # Para recuperar todos los registros de la consulta
            # registros = cursor.fetchone()  # Para recuperar un solo registro de la consulta
            for registro in registros:
                print(registro)

    conexion.close()
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
