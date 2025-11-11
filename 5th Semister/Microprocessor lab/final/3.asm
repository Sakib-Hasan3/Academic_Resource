include 'emu8086.inc'     ; only used for scan_num (input)

org 100h                  ; COM program

jmp start                 ; skip over data to code

; -------- DATA --------
msgPrompt db 'Enter a number (-128..127): $'
msgHigh   db 0Dh,0Ah, 'HIGH VALUE$'
msgNeg    db 0Dh,0Ah, 'NEGATIVE VALUE$'
msgMed    db 0Dh,0Ah, 'MEDIUM RANGE$'

; -------- CODE --------
start:

    ; ----- show prompt -----
    mov dx, offset msgPrompt
    mov ah, 9            ; DOS: print string until '$'
    int 21h

    ; ----- read signed integer -----
    ; scan_num puts the result in CX (signed)
    call scan_num
    mov ax, cx           ; use AX for comparisons

    ; ----- if x > 50 -----
    cmp ax, 50
    jg  HIGH_LABEL       ; signed greater than

    ; ----- else if x < 0 -----
    cmp ax, 0
    jl  NEG_LABEL        ; signed less than

    ; ----- else -----
    jmp MED_LABEL


HIGH_LABEL:
    mov dx, offset msgHigh
    mov ah, 9
    int 21h
    jmp DONE

NEG_LABEL:
    mov dx, offset msgNeg
    mov ah, 9
    int 21h
    jmp DONE

MED_LABEL:
    mov dx, offset msgMed
    mov ah, 9
    int 21h

DONE:
    mov ah, 4Ch          ; terminate program
    int 21h


; needed for scan_num macro
DEFINE_SCAN_NUM

end start
