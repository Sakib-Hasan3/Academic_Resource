.DATA
    a DW 5
    b DW 5
    result DB ?    ; store as byte since we will print a char

.CODE
MAIN PROC
    MOV AX, a
    MOV BX, b
    CMP AX, BX
    JE EQUAL

    ; else part
    MOV result, '0'   ; ASCII code for 0
    JMP END_IF

EQUAL:
    ; if part
    MOV result, '1'   ; ASCII code for 1

END_IF:
    ; Print result
    MOV DL, result    ; load result into DL
    MOV AH, 2         ; DOS print char function
    INT 21H           ; print it

    ; Exit program
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
