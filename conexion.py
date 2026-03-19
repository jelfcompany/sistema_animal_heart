import mysql.connector

try:
    mi_conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456" 
    )
    
    if mi_conexion.is_connected():
        mensajero = mi_conexion.cursor()
        mensajero.execute("USE animal_heart_db")
        
        print("\n--- 🐾 RECEPCIÓN DE ANIMAL HEART 🐾 ---")
        
        # 1. El programa te hace preguntas y guarda tus respuestas en variables
        nombre_ingresado = input("Escribe el nombre del paciente: ")
        especie_ingresada = input("¿Qué animal es? (Ej. Perro, Gato): ")
        
        # Usamos int() y float() para convertir el texto en números reales
        edad_ingresada = int(input("¿Cuántos años tiene? (Solo números): "))
        peso_ingresado = float(input("¿Cuánto pesa en kg? (Ej. 4.5): "))
        
        # 2. Preparamos la orden para MySQL
        consulta_insertar = "INSERT INTO pacientes (nombre, especie, edad, peso) VALUES (%s, %s, %s, %s)"
        
        # 3. Empaquetamos TUS respuestas
        datos_paciente = (nombre_ingresado, especie_ingresada, edad_ingresada, peso_ingresado) 
        
        # 4. Enviamos y firmamos
        mensajero.execute(consulta_insertar, datos_paciente)
        mi_conexion.commit()
        
        print(f"\n🎉 ¡Excelente! {nombre_ingresado} ha sido registrado con éxito en la base de datos.")

except mysql.connector.Error as error:
    print("Fallo en la Matrix. Error:", error)
except ValueError:
    print("⚠️ Error: Por favor, en la edad y el peso ingresa ÚNICAMENTE números, no letras.")