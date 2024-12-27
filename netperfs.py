#! /usr/bin/python3

import logging
import subprocess
import time
import test_config as cfg

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

logging.info("Iniciando")

nodos = [cfg.nodo_rx, cfg.nodo_tx]


for canal in cfg.canales:
    
    for nodo in nodos:
        cmd = """ssh root@{} "uci set wireless.radio{}.channel={}; 
                 uci set wireless.radio{}.txpower={}; uci changes;
                 uci commit wireless; sleep 3 && wifi &" """.format(nodo, cfg.radio, canal, cfg.radio, cfg.txpower)
        logging.info("ejecutando comando: {}".format(cmd))
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        print("salida: {}".format(proc)) #ex loggin.info
 
    time.sleep(45)
    
    netperf_file = open("{}_{}_{}--{}_ch{}_{}db_netperf.txt".format(cfg.antena, cfg.fecha, cfg.nodo_rx, cfg.nodo_tx, canal, cfg.txpower), "w+")

    cmd="""ipv6calc --action prefixmac2ipv6 --in prefix+mac --out ipv6addr fe80:: `ssh -A {} "iwinfo wlan{}-{} a | mac2bat | grep {} | bat2mac " | awk '{{print $1}}' ` """.format(cfg.nodo_tx, cfg.radio, cfg.modo,  cfg.nodo_rx.replace("-","_"))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")

    logging.info("ejecutando netperf: {}".format(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
    print("salida: {}".format(proc)) #ex loggin.info 

    fe80_nodo_rx=proc.stdout.replace("\n", "")
    print("la fe80 del nodo es " + fe80_nodo_rx)
    
    cmd = """ssh root@{} "netperf -cC -D1 -H {}%wlan{}-{} -l {}" """.format(cfg.nodo_tx, fe80_nodo_rx, cfg.radio, cfg.modo, cfg.netperf_duration)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
    print("salida: {}".format(proc)) #ex loggin.info
    netperf_file.write(proc.stdout)
    netperf_file.close()

        

