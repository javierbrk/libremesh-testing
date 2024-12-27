# libremesh-testing
some test scripts and tools for libremesh networks testing 
[TOC]

### mediciones.py
the `mediciones.py` file synchronizes the channels (selected in local_config.py) for the chosen radio on 2 nodes to test the signal level between them.
It needs the file local_config.py in the specific test folder.

### netperfs.py
As above, `netperfs.py` get the local_config to perform performance tests for each channel tested.

### plot_mediciones.py
generates a graph representing signal for each chain, resultant signal and measured channel.

### plot_netperfs.py
generates a graph representing network performance and measured channel.