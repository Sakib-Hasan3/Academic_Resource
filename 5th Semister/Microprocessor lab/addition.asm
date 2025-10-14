
org 100h
jmp start

crlf   db 13,10,'$'
msg    db 'SUB result (AL) = $'

start:
    mov  al, 25h
    mov  bl, 17h
    sub  al, bl            ; AL = 0Eh

    mov  dx, offset msg
    mov  ah, 09h
    int  21h
    call print_hex_al
    call newline

    mov  ax, 4C00h
    int  21h

; helpers
newline: mov dx, offset crlf
         mov ah, 09h
         int 21h
         ret
print_hex_al:
    push ax
    mov  dl, al
    shr  dl, 4
    call print_hex_nib
    mov  dl, al
    and  dl, 0Fh
    call print_hex_nib
    pop  ax
    ret
print_hex_nib:
    add  dl, '0'
    cmp  dl, '9'
    jbe  short ph_out
    add  dl, 7
ph_out: mov  ah, 02h
        int  21h
        ret

