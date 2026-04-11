org 100h             ; Starting address for .COM file

mov ax, 13           ; Load decimal number 13 into AX
mov cx, 0            ; Clear CX register, will be used to count digits
mov bx, 2            ; Set divisor to 2 for binary conversion (divide by 2)

; Convert Decimal to Binary
convert_loop:
    xor dx, dx       ; Clear DX (remainder will be stored here)
    div bx           ; AX / 2, quotient in AX, remainder in DX (0 or 1)
    add dl, '0'      ; Convert remainder (0 or 1) to ASCII ('0' = 30h, '1' = 31h)
    push dx          ; Push remainder (ASCII) onto the stack
    inc cx           ; Increment digit counter
    cmp ax, 0        ; Check if quotient is 0 (we've processed all bits)
    jne convert_loop ; If quotient is not 0, continue the loop

; Print the result (binary digits stored in stack)
print_loop:
    pop dx           ; Pop the top digit from stack
    mov dl, dl       ; Move digit into DL for printing
    mov ah, 02h      ; DOS function to print a character
    int 21h          ; Print character in DL
    loop print_loop  ; Loop until all digits are printed

; Exit the program
mov ah, 4Ch          ; DOS function to exit program
int 21h
