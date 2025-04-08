[[_TOC_]]

# MT7915E Performance Comparison: AP-UP vs Mesh Mode 40Mhz

## Overview of Configurations

### Configuration 1: AP-UP Mode
- File: `test_output_ap-up_7915.txt`
- Primary interface: `wlan7-peer1`
- Connection type: Access Point with uplink (AP-UP)
- Channel: 48 (5.240 GHz)
- HT Mode: HT40

### Configuration 2: Mesh Mode
- File: `test_output_7915.txt`
- Primary interface: `wlan1-mesh`
- Connection type: Mesh Point
- Channel: 48 (5.240 GHz)
- HT Mode: HT40

## Key Performance Metrics Comparison

| Metric | AP-UP Mode | Mesh Mode | Difference |
|--------|------------|-----------|------------|
| **Average Throughput** | 33.53 Mbps | 221.81 Mbps | +188.28 Mbps (+561%) |
| **Negotiated PHY Rate (Tx)** | 240-300 Mbps | 390-541.6 Mbps | +241.6 Mbps (+80%) |
| **Negotiated PHY Rate (Rx)** | 300 Mbps | 573.5 Mbps | +273.5 Mbps (+91%) |
| **Signal Strength** | -45 to -47 dBm | -43 to -47 dBm | Similar |
| **Modulation** | MCS 13-15, 40MHz | HE-MCS 8-11, 40MHz, HE-NSS 2 | Advanced in mesh mode |
| **Spatial Streams** | 2 spatial streams ?? | 2 spatial streams (HE-NSS 2) | - |
| **Guard Interval** | Not specified | Variable (HE-GI 0/1) | Adaptive in mesh mode |

## Detailed Analysis

### Throughput Performance

The mesh mode significantly outperforms the AP-UP mode, with an average throughput of 221.81 Mbps compared to only 33.53 Mbps in AP-UP mode. This represents a 561% improvement in real-world throughput.

Throughput over 10 iterations:

**AP-UP Mode:**
- Range: 33.31-33.72 Mbps
- Very consistent but low throughput
- Average: 33.53 Mbps

**Mesh Mode:**
- Range: 197.15-250.24 Mbps
- More variable but much higher throughput
- Average: 221.81 Mbps

### Connection Technology and Antenna Configuration

The most significant technical difference is the use of Wi-Fi 6/6E (802.11ax) features in mesh mode, particularly in how antenna chains are utilized:

1. **AP-UP Mode:**
   - Uses standard HT40 in 5GHz
   - Limited to older Wi-Fi 5 modulation schemes
   - MCS 13-15 with 40MHz channel
   - Although MCS 13-15 typically implies 2 spatial streams in Wi-Fi 5, the data suggests the connection is not effectively using multiple chains
   - No explicit spatial stream information is provided in the output
   - Guard interval is not adaptively managed

2. **Mesh Mode:**
   - Fully utilizes 802.11ax capabilities
   - Uses HE (High Efficiency) encoding
   - HE-MCS 8-11 modulation with 40MHz channel
   - Explicitly implements 2 spatial streams (HE-NSS 2)
   - Variable guard interval (HE-GI 0/1) for adaptive optimization
   - No Dual Carrier Modulation (HE-DCM 0)

### Signal Quality and Per-Chain Analysis

Both configurations provide detailed signal strength information that includes per-chain measurements:

**AP-UP Mode:**
- Primary signal strength: average -44.4 dBm (std dev 0.8)
- Chain 1: average -46.0 dBm (std dev 0.9)
- Chain 2: average -48.3 dBm (std dev 0.9)
- Chain imbalance: 2.3 dB average difference between chains
- Maximum chain difference: 3 dB
- Signal quality: 63-65/70 (consistently strong)

**Mesh Mode:**
- Primary signal strength: average -45.9 dBm (std dev 1.1)
- Chain 1: average -46.9 dBm (std dev 1.1)
- Chain 2: average -51.3 dBm (std dev 0.6)
- Chain imbalance: 4.4 dB average difference between chains
- Maximum chain difference: 6 dB
- Signal quality: 62-66/70 (consistently strong)

The per-chain analysis reveals interesting differences in how the two modes utilize the antenna chains:

1. AP-UP mode shows more balanced signal strength between the two chains, with an average difference of only 2.3 dB.
2. Mesh mode shows a more pronounced difference between the chains (4.4 dB average), with the second chain consistently receiving significantly weaker signals.
3. Despite the greater chain imbalance in mesh mode, it achieves much higher throughput, suggesting its 802.11ax capabilities are better at handling uneven signal distribution across chains.
4. The primary reported signal is stronger in AP-UP mode than in mesh mode on average, yet the throughput is much lower, further indicating that factors beyond raw signal strength (such as protocol efficiency and spatial stream utilization) are more significant determinants of performance.
The similar overall signal quality between modes confirms that the significant throughput difference is primarily due to protocol and configuration differences rather than signal conditions.

### Packet Handling Efficiency and Retransmissions

The mesh mode shows dramatically more efficient packet handling over 10 iterations:

**AP-UP Mode (10 iterations):**
- Initial Rx packets: 140,173
- Final Rx packets: 279,675
- Total Rx packets processed: 139,502
- Initial Tx packets: 261,088
- Final Tx packets: 530,384
- Total Tx packets processed: 269,296
- **Tx retries: 0** (consistently reported as 0 in all iterations)
- **Tx failed: 0** (consistently reported as 0 in all iterations)

**Mesh Mode (10 iterations):**
- Initial Rx packets: 42,461
- Final Rx packets: 77,681
- Total Rx packets processed: 35,220
- Initial Tx packets: 1,630,620
- Final Tx packets: 3,350,268
- Total Tx packets processed: 1,719,648
- **Tx retries: 0** (consistently reported as 0 in all iterations)
- **Tx failed: 0** (consistently reported as 0 in all iterations)

### Hardware Utilization and Interrupt Efficiency

The MT7915E chipset shows dramatically different interrupt patterns between the two modes:

**AP-UP Mode:**
- Initial MT7915E interrupts (INT 25): 312,501
- Final MT7915E interrupts (INT 25): 621,009
- Total interrupts during test: 308,508

**Mesh Mode:**
- Initial MT7915E interrupts (INT 25): 99,341
- Final MT7915E interrupts (INT 25): 146,377
- Total interrupts during test: 47,036

The AP-UP mode generated 6.56 times more interrupts than mesh mode while delivering significantly lower throughput. This suggests the mesh mode is much more efficient in its hardware utilization, with fewer CPU interrupts needed per unit of data transmitted.



Looking at both network test outputs you provided (`netperf_80_ap.txt` and `netperf_80_ap-up.txt`), I can see you're comparing Wi-Fi 6 (802.11ax) performance in two different configurations with the same MT7915E hardware. Let me analyze the key differences:

# Comparison of WiFi 6 Performance: Standard AP vs AP-UP Mode 80 Mhz

## Configuration Overview

| Parameter | Standard AP Mode | AP-UP Mode |
|-----------|-----------------|------------|
| Device | MT7915E | MT7915E |
| Mode | Client connected to AP | VLAN Master mode |
| Channel | 48 (5.240 GHz) | 48 (5.240 GHz) |
| Channel Width | HE80 (80MHz) | HE80 (80MHz) |
| Interface | wlan1-sta | wlan1-peer1 |

## Performance Differences

| Metric | Standard AP Mode | AP-UP Mode | Difference |
|--------|-----------------|------------|------------|
| **Average Throughput** | 374.95 Mbps | 127.97 Mbps | -65.9% |
| **PHY Rate (Tx)** | 907.4-1134.2 Mbps | 907.4-1020.6 Mbps | Similar rates |
| **Signal Strength** | -42 to -48 dBm | -42 to -47 dBm | Similar |
| **CPU Utilization** | ~58% send / ~41% receive | ~28% send / ~37% receive | Lower in AP-UP |

## Throughput Analysis

The most striking difference is in actual throughput:

- **Standard AP Mode**: Shows consistently high throughput between 343-389 Mbps
- **AP-UP Mode**: Shows dramatically lower throughput between 114-134 Mbps

Despite both configurations showing similar PHY rates and signal strengths, the AP-UP mode delivers about 1/3 of the throughput of the standard AP mode.

## Technical Observations

1. **Modulation Scheme**:
   - Both use HE-MCS (High Efficiency Modulation and Coding Scheme)
   - Both reach MCS 9-11 with 80MHz channels 
   - Both use 2 spatial streams (HE-NSS 2)

2. **RX Rate Differences**:
   - Standard AP mode shows consistent 1200.9 Mbps RX rate
   - AP-UP mode often shows "24.0 MBit/s" as RX rate despite having HE capability

3. **Packet Processing**:
   - AP-UP mode shows significant "rx drop misc" counts (10,000+)
   - Standard AP mode shows minimal "rx drop misc" counts

4. **CPU Interrupts**:
   - AP-UP mode shows significantly higher MT7915E interrupts (INT 29)
   - This suggests more driver/hardware interaction overhead in AP-UP mode

## Conclusion

The AP-UP mode configuration introduces significant overhead that dramatically reduces throughput (by approximately 66%) compared to standard AP mode. This occurs despite both configurations having similar physical layer capabilities, signal strengths, and modulation schemes.

The key bottleneck appears to be in the processing layer rather than the physical radio capabilities, with the AP-UP mode likely adding VLAN tagging and processing overhead that impacts performance. The regular pattern of packet drops and lower RX rate in AP-UP mode suggests protocol inefficiencies in this configuration.

For maximum performance, the standard AP mode is clearly superior for this hardware.