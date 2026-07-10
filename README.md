# VE2302_EDF

EDF flow for Tria VE2302 evaluation board. This is based on original meta-user and FPGA design from Tria, which have been modified to support newer Vivado versions, SDT and platform generation.

## Usage

### EDF flow

The script will automatically detect Vivado version and use matching EDF version. EDF has some version dependencies especially in lopper (2025.2 lopper does not work with 2026.06 EDF and version matching is currently needed).

Usage: build_edf [OPTIONS]  
  
Options:  
~~~
  -insecure              Insecure download mode not checking certificates  
  -platform              Build full platform imagage and SDK  
  -sstate <value>        Override SSTATE_CACHE location  
  -mirror <value>        Override SOURCE_MIRROR location  
  -clean                 Cleans HW + SW build artifacts  
  -clean_hw              Cleans only HW build  
  -clean_sw              Cleans only SW build  
  -h, --help             This help text  
~~~
  
Example:  
~~~
build_edf -platform -sstate /storage/sstate  
~~~

### Vitis example

(This is under work, the public files are little behind of my local copy, see TODO section)

The example script will compile one of the AMD examples using HLS, RTL and AIE kernels (https://github.com/Xilinx/Vitis-Tutorials/tree/2025.2/Vitis_System_Design/Design_Tutorials/01-Versal_Custom_Thin_Platform_Extensible_System) to this EDF Linux platform just as a proof of concept to verify platform functionality as extendable platform. The compilation will be via a very simple script which should be easy to replicate. 

Usage: build_vitis [OPTIONS]  
  
Options:  
~~~
  -clean                 Cleans build artifacts 
  -h, --help             Help text  
~~~

## Cloning & updates

Remember to use **git clone --recursive** to get HW submodule cloned at the beginning. And use **git pull --recurse-submodules** to update the submodules automatically

## Tips

### Initial setup

You need to setup git for repo to work

~~~
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
~~~

Also you need to install repo
~~~
curl https://storage.googleapis.com/git-repo-downloads/repo > repo
chmod a+x repo
sudo mv repo /usr/bin
~~~

### Vitis linking

Linking will fail unless the VE2302 board files are copied to .../Xilinx/2026.1/data/xhub/boards/XilinxBoardStore/boards/Xilinx directory. vpl does not seem to honor Vivado_init.tcl or vivado parameters given to v++ linker.


### QEMU

QEMU should boot up with command `runqemu versal-generic-xcve2302 nographic serial` (remember to source edf-init-build-env)


### repo not working behind firewall

Add this to the beginning of repo command (added it after the initial imports starting from line 30)

~~~
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
~~~

### If the build is broken

I do part of the development at home machine without Vivado, so I might break sometimes things. I'll try to fix them ASAP :) And this is not official Avnet/Tria tree, altough I work as dedicated AMD FAE at Avnet. I just hope this helps people with VE2302 board/SOM or just porting their own custom board to EDF. At least I have learned a lot while doing this. If this really becomes more popular I promise to do changes in branches, test compile, use tags for releases etc. And I'm morer than happy to accept improvements...

### Building with Ubuntu 24.04

Build with Ubuntu 24.04 will fail unless apparmor protection is changed, just execute `sudo apparmor_parser -R /etc/apparmor.d/unprivileged_userns` 

### Todo

* Porting https://github.com/Xilinx/Vitis-Tutorials/tree/2025.2/Vitis_System_Design/Design_Tutorials/01-Versal_Custom_Thin_Platform_Extensible_System to VE2302
   * Platform creation (done)
   * Compile HLS kernels (done)
   * Add AI engine (done)
   * Link design (done)
   * Cross compiled Linux executables
   * Package
   * HW-test
   * Cleanup the script (started)
* Cleanup of Vivado build, probably not that complex Makefile magic is needed
* Versal-AI port (this is not trivial as 6.2 still relies on Petalinux and memory controller setup for this is very tricky)
