import pymysql

print("=== INICIO DE SESIÓN ===")

try:
    # Intentamos la conexión con pymysql
    conexion = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",  # Pon "12345" si configuraste contraseña
        database="servicios_tecnicos",
        connect_timeout=3
    )

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    with conexion.cursor() as cursor:
        sql = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()

        if resultado:
            print("Inicio de sesión correcto")
            print(f"Bienvenido, {resultado[1]}")
        else:
            print("Usuario o contraseña incorrectos")

    conexion.close()

except Exception as err:
    print(f"\n❌ Error al conectar con la base de datos: {err}")