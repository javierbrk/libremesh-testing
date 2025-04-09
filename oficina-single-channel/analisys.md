## Comparativas para canales de 40 MHz (HE40)

### Comparación de rendimiento en HE40

| Modo | Throughput promedio | Rango de valores | Estabilidad |
|------|---------------------|------------------|-------------|
| AP-UP HE40 | ~78 Mbps | 73-81 Mbps | Media |
| Mesh HE40 | ~220 Mbps | 197-250 Mbps | Media-Alta |

### Características de MCS en HE40

| Modo | MCS común | Tasas de transmisión | NSS |
|------|-----------|----------------------|-----|
| AP-UP HE40 | 8-10 | 390.0-487.4 Mbps | 2 |
| Mesh HE40 | 9-11 | 433.3-541.6 Mbps | 2 |

### Análisis de interrupciones en HE40

| Modo | IRQ mt7915e (total) | IRQ/iteración | Eficiencia (Mbps/1000 IRQ) |
|------|---------------------|---------------|----------------------------|
| AP-UP HE40 | 4,561,565 → 4,757,132 | ~19,550 | ~4.0 |
| Mesh HE40 | 99,341 → 146,377 | ~5,203 | ~42.3 |

### Utilización de CPU en HE40

| Modo | Recv % | Send % | Service Demand Recv (us/KB) | Service Demand Send (us/KB) |
|------|--------|--------|----------------------------|----------------------------|
| AP-UP HE40 | 32-39% | 17-24% | 139-155 | 70-100 |
| Mesh HE40 | ~39% | ~57% | ~35 | ~51 |

## Comparativas para canales de 80 MHz (HE80)

### Comparación de rendimiento en HE80

| Modo | Throughput promedio | Rango de valores | Estabilidad |
|------|---------------------|------------------|-------------|
| AP-UP HE80 | ~130 Mbps | 114-135 Mbps | Media |
| Cliente HE80 | ~375 Mbps | 343-389 Mbps | Alta |

### Características de MCS en HE80

| Modo | MCS común | Tasas de transmisión | NSS |
|------|-----------|----------------------|-----|
| AP-UP HE80 | 9-10 | 907.4-1020.6 Mbps | 2 |
| Cliente HE80 | 9-11 | 907.4-1134.2 Mbps | 2 |

### Análisis de interrupciones en HE80

| Modo | IRQ mt7915e (total) | IRQ/iteración | Eficiencia (Mbps/1000 IRQ) |
|------|---------------------|---------------|----------------------------|
| AP-UP HE80 | [No disponible en los logs] | ~17,000-19,000* | ~7.1* |
| Cliente HE80 | 1,404,809 → 1,525,959 | ~12,115 | ~30.9 |

*Estimado basado en la diferencia proporcional observada en HE40

### Utilización de CPU en HE80

| Modo | Recv % | Send % | Service Demand Recv (us/KB) | Service Demand Send (us/KB) |
|------|--------|--------|----------------------------|----------------------------|
| AP-UP HE80 | 34-42% | 26-29% | 90-101 | 65-80 |
| Cliente HE80 | 40-43% | 56-60% | 35-38 | 49-53 |


## top output in ap-up
Mem: 105080K used, 143844K free, 528K shrd, 0K buff, 31336K cached
CPU:   0% usr   0% sys   0% nic  98% idle   0% io   0% irq   0% sirq
Load average: 0.34 0.33 0.18 2/112 25767
  PID  PPID USER     STAT   VSZ %VSZ %CPU COMMAND
Mem: 105252K used, 143672K free, 528K shrd, 0K buff, 31336K cached
CPU:   1% usr   1% sys   0% nic  97% idle   0% io   0% irq   0% sirq
Load average: 0.31 0.32 0.18 2/110 25780
  PID  PPID USER     STAT   VSZ %VSZ %CPU COMMAND
 1478  1449 network  S     4824   2%   0% /usr/sbin/hostapd -s -g /var/run/hostapd/global
  748     2 root     SW       0   0%   0% [napi/phy0-7]
14605     1 root     S     5120   2%   0% shared-state-async peer



# Fluen run ap-up
jjorge@leon:~$ flent rrul -p all_scaled -l 60 -H 10.13.60.237 -t text-to-be-included-in-plot -o filename.png
traceroute 10.13.60.237 
traceroute to 10.13.60.237 (10.13.60.237), 30 hops max, 60 byte packets
 1  LiMe-10194f (10.13.25.79)  0.536 ms  0.887 ms  0.764 ms
 2  LiMe-103ced.thisnode.info (10.13.60.237)  3.091 ms  2.935 ms  3.096 ms

