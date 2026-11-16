FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI:append = " file://platform-top.h file://bsp.cfg"

do_configure:append () {
                install ${UNPACKDIR}/platform-top.h ${S}/include/configs/
}
