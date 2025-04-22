mesh_iface=wlan1-mesh
#ipv6address="fe80::ac40:41ff:fe1c:8452%${mesh_iface}"
#mesh_iface=wlan7-peer1
#ipv6address="fe80::c64b:d1ff:fec1:6d%${mesh_iface}"
ipv6address="fe80::c04b:d1ff:fec1:6d%${mesh_iface}"


ubus call network.wireless status
ubus call iwinfo devices

for i in $(seq 1 10); do
     echo "Iteration $i $ipv6address "
     iwinfo
     iwinfo $mesh_iface assoclist
     netperf -cC -D1 -H $ipv6address | awk '{print $5}' | grep -E '^[0-9]+(\.[0-9]+)?$' | awk '{print "Throughput:", $1}'
     iwinfo $mesh_iface assoclist
     iw dev $mesh_iface station dump
     cat /proc/interrupts
     echo "--------------------------------------"
     echo "--------------------------------------"
     sleep 1  # Optional: add a short delay between iterations
 done
