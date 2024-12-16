import time
import os
import psutil

def obtener_velocidad_red():
    net_stat_antes = psutil.net_io_counters()
    time.sleep(1)
    net_stat_despues = psutil.net_io_counters()
    bytes_descargados = net_stat_despues.bytes_recv - net_stat_antes.bytes_recv
    velocidad_kbps = bytes_descargados / 1024
    return velocidad_kbps

def apagar_computadora():
    print("Descarga completada o sin uso de red. Apagando la computadora...")
    if os.name == "nt": 
        os.system("shutdown /s /t 1")
