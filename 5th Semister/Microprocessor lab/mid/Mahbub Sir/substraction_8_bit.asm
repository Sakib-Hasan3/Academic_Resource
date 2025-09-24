org 100h             ; Starting address for .COM file

mov al, 25h          ; first BCD number
mov bl, 12h          ; second BCD number
sub al, bl           ; subtract

daa                  ; adjust for BCD

; Print the result (AL)
call PrintNum        ; Call subroutine to print AL

; Exit program
mov ah, 4Ch          ; DOS function to exit program
int 21h

; Subroutine to print the number in AL (converted to ASCII)
PrintNum:
    add al, '0'      ; Convert number in AL to ASCII (48 = '0')
    mov dl, al       ; Move the result to DL (for printing)
    mov ah, 02h      ; DOS function to print a character
    int 21h          ; Print character in DL
    ret
