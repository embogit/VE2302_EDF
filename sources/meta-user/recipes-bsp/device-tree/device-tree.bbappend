FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI:append = " file://system-conf.dtsi"
SRC_URI:append = " file://system-user.dtsi"

require ${@'device-tree-sdt.inc' if d.getVar('SYSTEM_DTFILE') != '' else ''}
