
org 100h

; -----------------------------
; Factorial calculation (unchanged)
; -----------------------------
mov ax, 1h       ; AX = result
mov cx, 5h       ; number to calculate factorial

count:
    mul cx       ; AX = AX * CX
    loop count   ; decrement CX and loop if CX != 0

; -----------------------------
; Print the result in decimal
; -----------------------------
call PrintAXDecimal

ret

;-----------------------------------
; PrintAXDecimal: prints AX as decimal
;-----------------------------------
PrintAXDecimal:
    push ax
    push bx
    push cx
    push dx

    mov cx, 0        ; digit counter
    mov bx, 10

ConvertLoop:
    mov dx, 0
    div bx           ; AX / 10 ? quotient in AX, remainder in DX
    push dx          ; save remainder
    inc cx
    cmp ax, 0
    jne ConvertLoop

PrintLoop:
    pop dx
    add dl, 30h      ; convert 0?9 ? ASCII
    mov ah, 02h
    int 21h
    loop PrintLoop

    pop dx
    pop cx
    pop bx
    pop ax
    ret

