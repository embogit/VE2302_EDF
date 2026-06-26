# VE2302_EDF

EDF flow for Tria VE2302 evaluation board. This is based on original meta-user and FPGA design from Tria, which have been modified to support newer Vivado versions, SDT and platform generation.

## Usage

The script will automatically detect Vivado version and use matching EDF version. EDF has some version dependencies especially in lopper (2025.2 lopper does not work with 2026.06 EDF and version matching is currently needed).

Usage: build_edf [OPTIONS]

Options:
  -insecure              Insecure download mode not checking certificates
  -platform              Build full platform imagage and SDK
  -sstate <value>        Override SSTATE_CACHE location
  -mirror <value>        Override SOURCE_MIRROR location
  -clean                 Cleans HW + SW build results
  -clean_hw              Cleans HW build
  -clean_sw              Cleans SW build
  -h, --help             Help text

Example:
build_edf -platform -sstate /storage/sstate

## Cloning

** Remember to use git clone --recursive to get HW submodule cloned. **
