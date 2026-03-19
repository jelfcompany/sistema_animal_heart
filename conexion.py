import mysql.connector

try:
    mi_conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456" 
    )
    
    if mi_conexion.is_connected():
        mensajero = mi_conexion.cursor()
        
        mensajero.execute("CREATE DATABASE IF NOT EXISTS animal_heart_db")
        mensajero.execute("USE animal_heart_db")
        
        # El molde reparado
        consulta_tabla = """
        CREATE TABLE IF NOT EXISTS pacientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            especie VARCHAR(50),
            edad INT,
            peso FLOAT
        )
        """
        mensajero.execute(consulta_tabla)
        print("✅ Estructura de la clínica lista.")

        # ¡EL PRIMER PACIENTE! Llenamos la ficha médica
        consulta_insertar = "INSERT INTO pacientes (nombre, especie, edad, peso) VALUES (%s, %s, %s, %s)"
        datos_paciente = ("Odi", "Perro", 3, 15.5) 
        
        mensajero.execute(consulta_insertar, datos_paciente)
        
        # FIRMAMOS LA HISTORIA CLÍNICA 
        mi_conexion.commit()
        
        print("🎉 ¡Paciente registrado con éxito!")
        print(f"El ID asignado a {datos_paciente[0]} es: {mensajero.lastrowid}")

except mysql.connector.Error as error:
    print("Fallo en la Matrix. Error:", error)