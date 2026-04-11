  ; Program to print a message using ASCII codes
; Works in EMU8086 (Windows, DOS interrupts)

.model small
.stack 100h
.data
.code
main proc
    mov ax, @data
    mov ds, ax

    ; Print 'H' (ASCII 72)
    mov ah, 2          ; DOS function: print character
    mov dl, 72         ; ASCII code for 'H'
    int 21h

    ; Print 'E' (ASCII 69)
    mov dl, 69         ; 'E'
    int 21h

    ; Print 'L' (ASCII 76)
    mov dl, 76         ; 'L'
    int 21h

    ; Print 'L' again
    mov dl, 76
    int 21h

    ; Print 'O' (ASCII 79)
    mov dl, 79         ; 'O'
    int 21h

    ; Print newline (CR + LF = ASCII 13 and 10)
    mov dl, 13         ; Carriage Return
    int 21h
    mov dl, 10         ; Line Feed
    int 21h

    ; Exit program
    mov ah, 4Ch
    int 21h

main endp
end main
