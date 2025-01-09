#! /usr/bin/python3
# sudo apt install ipv6calc

import logging
import subprocess
import time
import test_config as cfg

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

logging.info("Iniciando")

nodos = [cfg.nodo_rx, cfg.nodo_tx]



def wait_for_hosts():
    cmd = 'while ! ping -c 1 -n -w 1 {0}; do sleep 1; echo .; done'.format(cfg.nodo_tx)
    logging.info("ejecutando comando: {}".format(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

    cmd = """ssh root@{0} 'while ! ping -c 1 -n -w 1 {1}; do sleep 1; echo .; done'""".format(cfg.nodo_tx,cfg.nodo_rx)
    logging.info("ejecutando comando: {}".format(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)

wait_for_hosts()


for canal in cfg.canales:
    
    for nodo in nodos:
        cmd = """ssh root@{} "uci set wireless.radio{}.channel={}; 
                 uci set wireless.radio{}.txpower={}; uci changes;
                 uci commit wireless; sleep 4 && wifi &" """.format(nodo, cfg.radio, canal, cfg.radio, cfg.txpower)
        logging.info("ejecutando comando: {}".format(cmd))
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        print("salida: {}".format(proc)) #ex loggin.info
 
    time.sleep(45)
    #wait for tx host 
    wait_for_hosts()

    if cfg.modo == "apup":
    #find interfeces
        cfg.nodo_rx_if=""
        cmd = """ssh root@{0} 'for iface in $(iw dev | grep "Interface wlan{1}-peer" | awk "{{print \$2}}"); do if iwinfo $iface assoc | mac2bat | grep -iq "{2}"; then echo "$iface"; break; fi; done'""".format(cfg.nodo_rx, cfg.radio,cfg.nodo_tx.replace("-","_"))    
        logging.info("ejecutando comando: {}".format(cmd))
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
        cfg.nodo_rx_if=proc.stdout.replace("\n", "")
        cmd = """ssh root@{0} 'for iface in $(iw dev | grep "Interface wlan{1}-peer" | awk "{{print \$2}}"); do if iwinfo $iface assoc | mac2bat | grep -iq "{2}"; then echo "$iface"; break; fi; done'""".format(cfg.nodo_tx, cfg.radio,cfg.nodo_rx.replace("-","_"))    
        logging.info("ejecutando comando: {}".format(cmd))
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
        cfg.nodo_tx_if=proc.stdout.replace("\n", "")


    
    netperf_file = open("{}_{}_{}--{}_ch{}_{}db_netperf.txt".format(cfg.antena, cfg.fecha, cfg.nodo_rx, cfg.nodo_tx, canal, cfg.txpower), "w+")

    if cfg.modo == "apup":
        cmd="""ipv6calc --action prefixmac2ipv6 --in prefix+mac --out ipv6addr fe80:: `ssh -A {} "iwinfo {} a | mac2bat | grep {} | bat2mac " | awk '{{print $1}}' ` """.format(cfg.nodo_tx, cfg.nodo_tx_if,  cfg.nodo_rx.replace("-","_"))
    else:
        cmd="""ipv6calc --action prefixmac2ipv6 --in prefix+mac --out ipv6addr fe80:: `ssh -A {} "iwinfo wlan{}-{} a | mac2bat | grep {} | bat2mac " | awk '{{print $1}}' ` """.format(cfg.nodo_tx, cfg.radio, cfg.modo,  cfg.nodo_rx.replace("-","_"))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")

    logging.info("ejecutando netperf: {}".format(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
    print("salida: {}".format(proc)) #ex loggin.info 

    cfg.fe80_nodo_rx=proc.stdout.replace("\n", "")
    print("la fe80 del nodo es " + cfg.fe80_nodo_rx)
    
    if cfg.modo == "apup":
        cmd = """ssh root@{} "netperf -cC -D1 -H {}%{} -l {}" """.format(cfg.nodo_tx, cfg.fe80_nodo_rx,  cfg.nodo_tx_if, cfg.netperf_duration)
    else:
        cmd = """ssh root@{} "netperf -cC -D1 -H {}%wlan{}-{} -l {}" """.format(cfg.nodo_tx, cfg.fe80_nodo_rx, cfg.radio, cfg.modo, cfg.netperf_duration)
    print (cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
    print("salida: {}".format(proc)) #ex loggin.info
    netperf_file.write(proc.stdout)
    netperf_file.close()

        

