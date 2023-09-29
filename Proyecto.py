import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Definir el nombre del archivo de inventario
archivo_inventario = "Ventas.txt"

# Función para listar productos
def listar_productos():
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Código: {}, Nombre: {}, Existencia: {}, Proveedor: {}, Precio: {}".format(*row))

# Función para crear un nuevo producto
def crear_producto(codigo, nombre, existencia, proveedor, precio):
    with open(archivo_inventario, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([codigo, nombre, existencia, proveedor, precio])
    print("Producto creado con éxito.")

# Función para actualizar la existencia de un producto
def actualizar_existencia(codigo, nueva_existencia):
    inventario = []
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                row[2] = nueva_existencia
            inventario.append(row)

    with open(archivo_inventario, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(inventario)
    print("Existencia actualizada con éxito.")

# aca iria las otras funciones como eliminar que es el unico que falta y los otros requerimientos que piden
# 2. Control de clientes 
# 3. Control de ventas 





# Función para generar un reporte en formato CSV o excel
def generar_reporte_csv():
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        with open("reporte.csv", mode='w', newline='') as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["Código", "Nombre", "Existencia", "Proveedor", "Precio"])
            for row in reader:
                writer.writerow(row)
    print("Reporte CSV generado.")

# Funcion para mandar el reporte a un correo aca es donde tengo el 
# incoveniente que no encuentro que pueda hacer pero pueden tomar este ejemplo para empezar 
def enviar_correo_con_adjunto(destinatario, asunto, mensaje, archivo_adjunto):
    correo_emisor = '@gmail.com'
    contraseña_emisor = 'tucontraseña'

    msg = MIMEMultipart()
    msg['From'] = correo_emisor
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    with open(archivo_adjunto, "rb") as adjunto:
        part = MIMEApplication(adjunto.read(), Name="reporte.csv")
        part['Content-Disposition'] = f'attachment; filename="{archivo_adjunto}"'
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(correo_emisor, contraseña_emisor)
    server.sendmail(correo_emisor, destinatario, msg.as_string())
    server.quit()
    print("Correo enviado con éxito.")

# Ejemplo de uso lo cual es por la consolo 
while True:
    print("\nSistema de Ventas")
    print("1. Listar productos")
    print("2. Crear producto")
    print("3. Actualizar existencia")
    print("4. Generar reporte y enviar por correo")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        listar_productos()
    elif opcion == '2':
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        existencia = input("Ingrese la existencia del producto: ")
        proveedor = input("Ingrese el proveedor del producto: ")
        precio = input("Ingrese el precio del producto: ")
        crear_producto(codigo, nombre, existencia, proveedor, precio)
    elif opcion == '3':
        codigo = input("Ingrese el código del producto a actualizar: ")
        nueva_existencia = input("Ingrese la nueva existencia del producto: ")
        actualizar_existencia(codigo, nueva_existencia)
    elif opcion == '4':
        generar_reporte_csv()
        destinatario = input("Ingrese el correo del destinatario: ")
        asunto = "Reporte de inventario"
        mensaje = "Adjunto encontrarás el reporte de inventario."
        archivo_adjunto = "reporte.csv"
        enviar_correo_con_adjunto(destinatario, asunto, mensaje, archivo_adjunto)
    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")