import mysql.connector

try:
    # 1. Conectamos al servidor general (sin nombrar el archivero aún)
    mi_conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456"  
    )
    
    if mi_conexion.is_connected():
        mensajero = mi_conexion.cursor()
        
        # 2. Creamos el archivero 
        mensajero.execute("CREATE DATABASE IF NOT EXISTS animal_heart_db")
        print("✅ Archivero 'animal_heart_db' creado en el portátil.")
        
        # 3. Le decimos al mensajero que ENTRE a ese archivero
        mensajero.execute("USE animal_heart_db")
        
        # 4. Diseñamos la tabla de pacientes
        consulta_sql = """
        CREATE TABLE IF NOT EXISTS pacientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            especie VARCHAR(50),
            edad INT,
            peso FLOAT
        )
        """
        
        # 5. Mandamos a construir la tabla
        mensajero.execute(consulta_sql)
        print("✅ Tabla 'pacientes' creada y lista para recibir peluditos.")
        print("🎉 ¡Entorno del portátil sincronizado al 100%!")

except mysql.connector.Error as error:
    print("Fallo en la Matrix. Error:", error)