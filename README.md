# Performance Analysis of TCP Variants

## Description
This project analyzes the performance of various TCP variants using TCL scripts and Python utilities in NS2 simulations.

## Python Scripts

### `convert_trace_to_txt_files.py`
Converts NS2 trace files from `.tr` format to `.txt` for easier parsing.

### `index_tracefiles.py`
Reads trace files and converts them into CSV format with labeled columns, using Pandas.

## Folders

### General TCP Simulation
Contains TCL scripts and other resources for general TCP variant / TCP Tahoe simulations in NS2.

### TCP Reno and Vegas Simulation
Focused on simulations and analysis specific to TCP Reno and Vegas variants.

### Time-Driven Simulation of UDP
Contains TCL scripts to perform time-driven simulations for UDP protocols.

## Auxiliary Files

### `labelled_trace_file.csv`
A CSV file that contains indexed and labeled NS2 trace data.
