# Performance Comparison: AP-UP Mode vs Other Modes (AP, 802.11s)

**TL;DR:**  
AP-UP mode shows a significant performance loss compared to AP and Mesh modes.
It also generates more driver interrupts during the same test runs.
Packet captures shows the same number of beacons in AP-UP and classic AP mode (10 per second).
remote_capture_netperf.pcap equivalent files show some estrange sequences witch differ from the same file in classic AP mode. APuP mode appears to have "[TCP ACKed unseen segment]" flags, also shows numerous acknowledgements in sequence from the same device, with occasional Clear-to-send frames. You can find `.pcap` files in the corresponding folders.
You can find `.pcap` files in the corresponding folders.


# Stres tests
Ten runs of netperf and several commands after and before are summarized for different scenarios. 
Netperf was run from router 1 to router 2 using only the wifi link.

## Comparisons for 40 MHz Channels (HE40)
### Performance Comparison in HE40

| Mode        | Average Throughput | Value Range    | Stability      |
|-------------|--------------------|----------------|----------------|
| AP-UP HE40  | ~78 Mbps           | 73–81 Mbps     | Medium         |
| Mesh HE40   | ~220 Mbps          | 197–250 Mbps   | Medium–High    |

### MCS Characteristics in HE40

| Mode        | Common MCS         | Transmission Rates     | NSS |
|-------------|--------------------|-------------------------|-----|
| AP-UP HE40  | 8–10               | 390.0–487.4 Mbps        | 2   |
| Mesh HE40   | 9–11               | 433.3–541.6 Mbps        | 2   |

### Interrupt Analysis in HE40

| Mode        | Total IRQ (mt7915e) * | IRQ per Test Iteration | Efficiency (Mbps/1000 IRQ) |
|-------------|---------------------|-------------------------|-----------------------------|
| AP-UP HE40  | 4,561,565 → 4,757,132 | ~19,550               | ~4.0                        |
| Mesh HE40   | 99,341 → 146,377    | ~5,203                  | ~42.3                       |

*output of cat /proc/interrupts, values for wifi module driver interrupts at the beginning and at the end of the tests runs. 

### netperf reported CPU Utilization in HE40

| Mode        | Recv % | Send % | Recv Service Demand (us/KB) | Send Service Demand (us/KB) |
|-------------|--------|--------|------------------------------|------------------------------|
| AP-UP HE40  | 32–39% | 17–24% | 139–155                      | 70–100                       |
| Mesh HE40   | ~39%   | ~57%   | ~35                          | ~51                          |

---

## Comparisons for 80 MHz Channels (HE80)

### Performance Comparison in HE80

| Mode         | Average Throughput | Value Range     | Stability |
|--------------|--------------------|------------------|------------|
| AP-UP HE80   | ~130 Mbps          | 114–135 Mbps     | Medium     |
| Clasic AP HE80  | ~375 Mbps          | 343–389 Mbps     | High       |

### MCS Characteristics in HE80

| Mode         | Common MCS         | Transmission Rates       | NSS |
|--------------|--------------------|---------------------------|-----|
| AP-UP HE80   | 9–10               | 907.4–1020.6 Mbps         | 2   |
| Clasic AP HE80  | 9–11               | 907.4–1134.2 Mbps         | 2   |

### Interrupt Analysis in HE80

| Mode         | Total IRQ (mt7915e) | IRQ per Iteration | Efficiency (Mbps/1000 IRQ) |
|--------------|---------------------|--------------------|-----------------------------|
| AP-UP HE80   | 3,782,992 → 3,955,714 | 17,272            | ~7.4                        |
| Clasic AP HE80  | 1,404,809 → 1,525,959 | ~12,115           | ~30.9                       |

### CPU Utilization in HE80

| Mode         | Recv % | Send % | Recv Service Demand (us/KB) | Send Service Demand (us/KB) |
|--------------|--------|--------|------------------------------|------------------------------|
| AP-UP HE80   | 34–42% | 26–29% | 90–101                       | 65–80                        |
| Clasic AP HE80  | 40–43% | 56–60% | 35–38                        | 49–53                        |

---

## `top` Command Output while the system is iddle 
top shows similar output for both AP-UP and classic AP mode 
### Output of top for AP-UP

```
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
```
### In classic AP mode

```
Mem: 105732K used, 143192K free, 588K shrd, 0K buff, 31304K cached
CPU:   1% usr   2% sys   0% nic  96% idle   0% io   0% irq   0% sirq
Mem: 105732K used, 143192K free, 588K shrd, 0K buff, 31304K cached
CPU:   0% usr   0% sys   0% nic  98% idle   0% io   0% irq   0% sirq
Load average: 0.06 0.08 0.03 2/127 23149
  PID  PPID USER     STAT   VSZ %VSZ %CPU COMMAND
 1509  1474 network  S     4940   2%   0% /usr/sbin/hostapd -s -g /var/run/hostapd/global
  757     2 root     SW       0   0%   0% [napi/phy0-7]
22938  4411 root     R     1420   1%   0% top
 1728     1 root     S     4504   2%   0% shared-state-async peer
22311     2 root     IW       0   0%   0% [kworker/u8:1-ph]

```

# Flent run ap-up
Flent was run in AP-UP mode twice and the results are in the folder

```
flent rrul -p all_scaled -l 60 -H 10.13.60.237 -t text-to-be-included-in-plot -o filename.png
traceroute 10.13.60.237 
traceroute to 10.13.60.237 (10.13.60.237), 30 hops max, 60 byte packets
 1  LiMe-10194f (10.13.25.79)  0.536 ms  0.887 ms  0.764 ms
 2  LiMe-103ced.thisnode.info (10.13.60.237)  3.091 ms  2.935 ms  3.096 ms
```
