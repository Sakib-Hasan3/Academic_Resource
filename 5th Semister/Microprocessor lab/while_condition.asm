.DATA
    i   DW 5          ; loop counter (start at 5)
    spc DB ' ', '$'   ; space for printing (not strictly needed here)

.CODE
MAIN PROC
    ; --- set DS to our data segment ---
    mov ax, @DATA
    mov ds, ax

    ; i -> CX (use CX as the loop counter)
    mov cx, i

WHILE_START:
    cmp cx, 0
    jle WHILE_END     ; while (i > 0)

    ; print the value in CX (single digit only 0..9)
    mov ax, cx        ; copy i
    and ax, 0FFh      ; keep low byte (defensive)
    add al, '0'       ; make ASCII
    mov dl, al
    mov ah, 2         ; DOS: print char in DL
    int 21h

    ; print a space
    mov dl, ' '
    mov ah, 2
    int 21h

    dec cx            ; i--
    jmp WHILE_START

WHILE_END:
    ; newline (CR LF) so the DOS prompt starts on next line
    mov dl, 13        ; CR
    mov ah, 2
    int 21h
    mov dl, 10        ; LF
    mov ah, 2
    int 21h

    ; exit
    mov ah, 4Ch
    int 21h
MAIN ENDP
END MAIN
