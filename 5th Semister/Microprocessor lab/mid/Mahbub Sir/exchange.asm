org 100h          ; Origin for COM file


mov ax, 1h        ; Load AX with 1
mov bx, 2h        ; Load BX with 2

xchg ax, bx       ; Exchange AX and BX

; ----------------------------
; Display AX
; ----------------------------
mov cl, al        ; Copy AX (lower 8 bits) to CL
call print_num
mov dl, 13        ; New line
mov ah, 02h
int 21h
mov dl, 10
mov ah, 02h
int 21h

; ----------------------------
; Display BX
; ----------------------------
mov cl, bl        ; Copy BX (lower 8 bits) to CL
call print_num
mov dl, 13        ; New line
mov ah, 02h
int 21h
mov dl, 10
mov ah, 02h
int 21h

ret                ; End program

; ----------------------------
; Subroutine: print_num
; Prints single-digit number in CL
; ----------------------------
print_num:
    add cl, '0'    ; Convert number 0-9 to ASCII
    mov dl, cl
    mov ah, 02h    ; DOS print character function
    int 21h
    ret
