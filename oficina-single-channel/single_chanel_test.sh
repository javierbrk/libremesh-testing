#mesh_iface=wlan5-mesh
#ipv6address="fe80::ac40:41ff:fe1c:8452%${mesh_iface}"
mesh_iface=wlan5-peer1
ipv6address="fe80::aa40:41ff:fe1c:8452%${mesh_iface}"



ubus call network.wireless status
ubus call iwinfo devices

for i in $(seq 1 10); do
     echo "Iteration $i $ipv6address "
     iwinfo
     iwinfo $mesh_iface assoclist
     netperf -cC -D1 -H $ipv6address | awk '{print $5}' | grep -E '^[0-9]+(\.[0-9]+)?$' | awk '{print "Throughput:", $1}'
     iwinfo $mesh_iface assoclist
     iw dev $mesh_iface station dump
     iw dev wlan5-peer1 station dump | grep -E "rx|tx"
     cat /proc/interrupts
     echo "--------------------------------------"
     echo "--------------------------------------"
     sleep 1  # Optional: add a short delay between iterations
 done
