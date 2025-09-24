org 100h             ; Starting address for .COM file

mov ax, 16h          ; Number to find square root of
mov cx, 0h           ; Result (square root)
mov bx, 1h           ; Current guess

next_guess:
    mov dx, 0h
    mov ax, 16h      ; Reload number
    div bx           ; AX = number / guess (AX / BX)

    add ax, bx       ; AX = guess + (number / guess)
    shr ax, 1        ; AX = (guess + (number / guess)) / 2
    cmp ax, cx       ; Compare new guess with previous guess
    je done          ; If equal, we're done
    mov cx, ax       ; Update result
    inc bx           ; Increment guess
    jmp next_guess

done:
    mov ax, cx       ; Move result to AX (square root)

    ; Print the result (AX)
    call PrintNum    ; Call subroutine to print AX

    ; Exit program
    mov ah, 4Ch      ; DOS function 4Ch (Exit)
    int 21h

; Subroutine to print the number in AX
PrintNum:
    ; Handle the case for printing numbers
    ; AX should contain a value between 0 and 9 for single digit printing
    add ax, '0'      ; Convert number in AX to ASCII (48 = '0')
    mov dl, al       ; Move the result to DL
    mov ah, 02h      ; DOS function to print a character
    int 21h          ; Print character in DL
    ret
