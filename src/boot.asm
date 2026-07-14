section .multiboot_header
header_start:
    dd 0x1badb002
    dd 0x0
    dd (0x1badb002 + 0x0)
header_end:

global start
section .text
bits 32
start :
    cli
    hlt
.loop:
    jmp .loop