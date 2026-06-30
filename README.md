# VE2302_EDF

EDF flow for Tria VE2302 evaluation board. This is based on original meta-user and FPGA design from Tria, which have been modified to support newer Vivado versions, SDT and platform generation.

## Usage

The script will automatically detect Vivado version and use matching EDF version. EDF has some version dependencies especially in lopper (2025.2 lopper does not work with 2026.06 EDF and version matching is currently needed).

Usage: build_edf [OPTIONS]  
  
Options:  
~~~
  -insecure              Insecure download mode not checking certificates  
  -platform              Build full platform imagage and SDK  
  -sstate <value>        Override SSTATE_CACHE location  
  -mirror <value>        Override SOURCE_MIRROR location  
  -clean                 Cleans HW + SW build results  
  -clean_hw              Cleans HW build  
  -clean_sw              Cleans SW build  
  -h, --help             Help text  
~~~
  
Example:  
~~~
build_edf -platform -sstate /storage/sstate  
~~~

## Cloning

Remember to use **git clone --recursive** to get HW submodule cloned.

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

I do part of the devleopment at home machine without Vivado, so I might break sometimes things. I'll try to fix them ASAP :) And this is not official Avnet/Tria tree, altough I work as dedicated AMD FAE at Avnet. I just hope this helps people with VE2302 board/SOM or just porting their own custom board to EDF. At least I have learned a lot while doing this. If this really becomes more popular I promise to do changes in branches, test compile, use tags for releases etc. And I'm morer than happy to accept improvements...

### Todo

* Porting https://github.com/Xilinx/Vitis-Tutorials/tree/2025.2/Vitis_System_Design/Design_Tutorials/01-Versal_Custom_Thin_Platform_Extensible_System to VE2302 (started to do this already)
* Cleanup of Vivado build, probably not that complex Makefile magic is needed
* Versal-AI port (this is not trivial as 6.2 still relies on Petalinux and memory controller setup for this is very tricky)
