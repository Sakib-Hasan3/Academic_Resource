org 100h          ; .COM program

jmp start         ; skip over data


; -------- DATA --------
N       dw 5              ; INPUT: change this to any small positive number
RESULT  dw ?              ; OUTPUT: will hold N! in binary

msgRes  db 'Result = ', '$'


; =====================================================
; factorial(n)
; parameter: n passed on stack at [BP+4]
; returns:  AX = n!
; =====================================================
factorial:
    push bp
    mov  bp, sp           ; set up stack frame

    mov  ax, [bp+4]       ; AX = n
    cmp  ax, 0
    jz   base_case        ; if n == 0 ? 1

    ; ---- recursive case: n * factorial(n-1) ----
    dec  ax               ; AX = n-1
    push ax               ; push (n-1) as argument
    call factorial        ; AX = factorial(n-1)

    mov  bx, [bp+4]       ; BX = original n
    mul  bx               ; AX = AX * BX
    jmp  fact_done

base_case:
    mov  ax, 1            ; 0! = 1

fact_done:
    pop  bp
    ret  2                ; remove 1 word parameter and return



; =====================================================
; print_dec:
; Prints AX as an unsigned decimal number using int 21h.
; Uses: AX (value), destroys BX, CX, DX (but restores them).
; =====================================================
print_dec:
    push bx
    push cx
    push dx

    cmp  ax, 0
    jne  pd_not_zero

    ; ----- AX == 0 -> print '0' -----
    mov  dl, '0'
    mov  ah, 2
    int  21h
    jmp  pd_done

pd_not_zero:
    xor  cx, cx           ; digit count = 0

pd_loop:
    xor  dx, dx           ; clear DX before DIV
    mov  bx, 10
    div  bx               ; AX = AX / 10, remainder in DX
    push dx               ; save remainder (digit)
    inc  cx               ; count digit
    cmp  ax, 0
    jne  pd_loop

    ; now print digits in reverse order
pd_print:
    pop  dx               ; low word: digit
    add  dl, '0'          ; convert 0..9 to '0'..'9'
    mov  ah, 2
    int  21h
    loop pd_print

pd_done:
    pop  dx
    pop  cx
    pop  bx
    ret



; ================== MAIN ==================
start:
    ; compute factorial(N)
    mov  ax, [N]          ; AX = N (input)
    push ax               ; pass as parameter
    call factorial        ; AX = N!
    mov  [RESULT], ax     ; store in memory

    ; print "Result = "
    mov  dx, offset msgRes
    mov  ah, 9
    int  21h

    ; print RESULT in decimal
    mov  ax, [RESULT]
    call print_dec

    ; new line
    mov  dl, 0Dh
    mov  ah, 2
    int  21h
    mov  dl, 0Ah
    mov  ah, 2
    int  21h

    ; exit to DOS
    mov  ah, 4Ch
    int  21h

end start
