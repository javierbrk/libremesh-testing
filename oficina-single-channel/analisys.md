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

