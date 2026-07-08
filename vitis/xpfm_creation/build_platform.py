import vitis
import argparse
import os

parser = argparse.ArgumentParser(
    description="Script to create a fixed Vitis platform (.xpfm)"
)

parser.add_argument("--rootdir", type=str, dest="rootdir",  
                    help="root path for this whole project")

args = parser.parse_args()

rootdir=args.rootdir

print("Rootdir: ",rootdir)

#exit()

client = vitis.create_client()
client.set_workspace(path=rootdir + "/vitis/build/workspace/")


advanced_options = client.create_advanced_options_dict(user_dtsi=rootdir + "/sources/meta-user/recipes-bsp/device-tree/files/system-user-vitis.dtsi",dt_overlay="0")

platform = client.create_platform_component(name = "versal-generic-xcve2302_platform",hw_design = rootdir + "/vivado-hw/ve2302_platform_2026_1.xsa",os = "linux",cpu = "psv_cortexa72",domain_name = "linux_psv_cortexa72",advanced_options = advanced_options)

platform = client.get_component(name="versal-generic-xcve2302_platform")
domain = platform.get_domain(name="linux_psv_cortexa72")

status = domain.set_bif(path=rootdir + "/build/tmp/deploy/images/versal-generic-xcve2302/boot.bin-extracted/bootgen.bif")

status = domain.set_boot_dir(path=rootdir + "/build/tmp/deploy/images/versal-generic-xcve2302")

status = domain.set_qemu_data(path=rootdir + "/vitis/xpfm_creation/src/a72")

domain = platform.add_domain(cpu = "ai_engine",os = "aie_runtime",name = "aiengine",display_name = "aiengine")

status = platform.build()
