import datetime
import os
import sys

sys.path.append(os.getcwd())

#antena = os.path.split(os.getcwd())[-1]
antena = "modconica-pre-APUP"

nodo_tx = "meta"
nodo_rx = "si"
radio = 1
modo = "mesh"
mcs_bitrate = 0

fecha = datetime.date.today().isoformat()

# borramos 140 y 165 porque no generan resultados, al menos en ql-graciela-bbone -- testantena
canales = [36,40,44,56,60,64,100,104,112,116,120,128,132,149,153,161]
#36,40,44
txpower = 26
netperf_duration = 30
cantidad_mediciones = 15

try:
    from local_config import *
except:
    exit("Falta local_test_config.py en la carpeta local para configurar el experimento.")

