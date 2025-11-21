
org 100h

jmp start              ; skip over data


; ------------ DATA ------------
NUM1    db 25h         ; example 8-bit numbers
NUM2    db 12h
RESULT  db ?           ; final 8-bit result
CFVAL   db ?           ; '0' or '1' for CF
ZFVAL   db ?           ; '0' or '1' for ZF

msgCF   db 0Dh,0Ah, 'CF = ', '$'
msgZF   db 0Dh,0Ah, 'ZF = ', '$'


; ------------ CODE ------------
start:

    ; 1) Load NUM1 and NUM2
    mov  al, NUM1       ; AL = NUM1
    mov  bl, NUM2       ; BL = NUM2

    ; 2) NUM1 - NUM2 using SBB (SUBB on 8086)
    clc                 ; ensure no borrow
    sbb  al, bl         ; AL = NUM1 - NUM2 - CF

    ; 3) Rotate result left through carry 3 times (ROL)
    rol  al, 1
    rol  al, 1
    rol  al, 1

    ; 4) Add rotated result with original NUM1 using ADC
    mov  bl, NUM1       ; BL = original NUM1
    adc  al, bl         ; AL = AL + NUM1 + CF

    ; 5) Logical right shift of final result by 2 bits (SHR)
    shr  al, 1
    shr  al, 1

    ; 6) Store final 8-bit result in RESULT
    mov  RESULT, al

    ; ---- capture CF and ZF AFTER all operations ----
    ; CF from last SHR, ZF from last SHR

    ; CF
    mov  dl, '1'
    jc   cf_is_one
    mov  dl, '0'
cf_is_one:
    mov  CFVAL, dl

    ; ZF
    mov  dl, '1'
    jz   zf_is_one
    mov  dl, '0'
zf_is_one:
    mov  ZFVAL, dl

    ; 7) Display CF and ZF using DOS interrupts

    ; print "CF = "
    mov  dx, offset msgCF
    mov  ah, 9
    int  21h

    ; print CF value ('0' or '1')
    mov  dl, CFVAL
    mov  ah, 2
    int  21h

    ; print "ZF = "
    mov  dx, offset msgZF
    mov  ah, 9
    int  21h

    ; print ZF value ('0' or '1')
    mov  dl, ZFVAL
    mov  ah, 2
    int  21h

    ; exit to DOS
    mov  ah, 4Ch
    int  21h

end start

