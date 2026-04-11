include 'emu8086.inc'

org 100h

jmp start          ; jump over data to code

; ---------------- DATA ----------------

arrayA     db 10,20,30,40,50,60,70,80,90,100
lenA      equ 10

arrayB     db 'A','b','C','E','i','X','O','u','Z','a'
lenB      equ 10

vowels     db 'A','E','I','O','U'  ; vowel table
vowelCnt   db 0

; ---------------- CODE ----------------
start:

;------------------------------------------------
; STEP 1: REVERSE ARRAY A (no XCHG on same index)
;------------------------------------------------
    mov si, 0
    mov di, lenA - 1

rev_loop:
    cmp si, di
    jae rev_done                ; while (si < di)

    mov al, [arrayA + si]
    mov bl, [arrayA + di]
    mov [arrayA + si], bl
    mov [arrayA + di], al

    inc si
    dec di
    jmp rev_loop

rev_done:

;------------------------------------------------
; STEP 2: COUNT VOWELS IN ARRAY B USING REPNE
;         For each char in B, search in vowels[]
;------------------------------------------------
    mov byte ptr [vowelCnt], 0
    lea si, arrayB
    mov cx, lenB

    cld                          ; process forward

next_char:
    cmp cx, 0
    je  vowels_done

    lodsb                        ; AL = [SI], SI++
    push cx                      ; save outer counter

    lea di, vowels
    mov cx, 5                    ; 5 vowels
    repne scasb                  ; search AL in vowels[]
    jne not_vowel                ; not found -> not vowel

    inc byte ptr [vowelCnt]      ; found a vowel

not_vowel:
    pop cx
    dec cx
    jmp next_char

vowels_done:

;------------------------------------------------
; STEP 3 + 4:
;   For each number in reversed arrayA:
;       even -> double
;       odd  -> subtract 3
;   Stop when running sum > 200h
;------------------------------------------------
    mov ax, 0                    ; AX = sum
    mov si, 0                    ; index = 0

process_loop:
    cmp si, lenA
    jae process_done             ; end of array

    mov bl, [arrayA + si]

    test bl, 1
    jz  even_num                 ; if even

; odd -> subtract 3
    sub bl, 3
    jmp short store_val

even_num:
; even -> double
    add bl, bl

store_val:
    mov [arrayA + si], bl

    xor bh, bh                   ; BX = 00..BL
    mov bl, [arrayA + si]
    add ax, bx                   ; sum += value
    cmp ax, 0200h
    ja  process_done             ; stop when sum > 200h

    inc si
    jmp process_loop

process_done:

;------------------------------------------------
; STEP 5: DISPLAY RESULTS
;------------------------------------------------
    printn "Modified Array A:"
    mov si, 0

show_loop:
    cmp si, lenA
    jae show_done

    mov al, [arrayA + si]
    xor ah, ah                   ; AX = value (unsigned)
    call print_num_uns
    print " "

    inc si
    jmp show_loop

show_done:
    printn
    print "Vowel count = "
    mov al, [vowelCnt]
    xor ah, ah
    call print_num_uns
    printn

    mov ah, 4Ch
    int 21h

; --------- MACRO DEFINITIONS (EMU8086) ---------
DEFINE_PRINT_NUM_UNS

end start
