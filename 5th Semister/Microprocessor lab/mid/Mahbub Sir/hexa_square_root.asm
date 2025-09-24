org 100h             ; Starting address for .COM file

mov ax, 4h           ; Number to find square root of (4)
mov bx, 1h           ; Current guess

next_guess:
    mov ax, 4h       ; Reload number
    div bx           ; AX = number / guess (AX / BX)
    
    cmp ax, bx       ; Compare the guess with the new result
    je done          ; If equal, we're done (square root found)
    
    add bx, 1        ; Increment guess by 1
    jmp next_guess   ; Repeat the process

done:
    mov ax, bx       ; Move the result to AX (square root)

    ; Print the result (AX)
    call PrintNum    ; Call subroutine to print AX

    ; Exit program
    mov ah, 4Ch      ; DOS function 4Ch (Exit)
    int 21h

; Subroutine to print the number in AX
PrintNum:
    add ax, '0'      ; Convert number in AX to ASCII (48 = '0')
    mov dl, al       ; Move the result to DL
    mov ah, 02h      ; DOS function to print a character
    int 21h          ; Print character in DL
    ret
