org 100h            ; Starting address for .COM file

; Add two numbers
mov ax, 5           ; First number (5)
mov bx, 3           ; Second number (3)
add ax, bx          ; AX = AX + BX (5 + 3 = 8)

; Print Sum (convert to ASCII)
add ax, '0'         ; Convert result to ASCII ('8' = 56 in ASCII)
mov dl, al          ; Move the result into DL for printing
mov ah, 02h         ; DOS interrupt to print character
int 21h             ; Call DOS interrupt to print the character

; Fibonacci series
mov dx, 0           ; First Fibonacci number (0)
mov si, 1           ; Second Fibonacci number (1)
mov cx, 5           ; Fibonacci count (print 5 numbers)

print_fib:
    add dx, si       ; DX = DX + SI (next Fibonacci number)
    mov si, dx       ; Update SI with the last Fibonacci number
    add dx, '0'      ; Convert the Fibonacci number to ASCII
    mov dl, dl       ; Move the result into DL for printing
    int 21h          ; Print Fibonacci number
    loop print_fib   ; Repeat for 5 times

; Exit program
mov ah, 4Ch         ; DOS interrupt to terminate the program
int 21h
