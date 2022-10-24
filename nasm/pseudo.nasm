;-------------------------------------
; pseudo.nasm
; Leita o README.md para detalhes
;-------------------------------------
; if ( RAM[0] < 2 || RAM[1] == 0 ):
;     RAM[5] = RAM[5] + 1
; else
;     RAM5[5] = RAM[5] - 1
;-------------------------------------

    leaw $0, %A
    movw (%A), %D
    leaw $2, %A
    subw %D, %A, %D
    leaw $else, %A
    jge %D
    nop
    leaw $1, %A
    movw (%A), %D
    leaw $else, %A
    jne %D
    nop
if:
    leaw $5, %A
    movw (%A), %D
    incw %D
    movw %D, (%A)
    leaw $end, %A
    jmp
    nop
else:
    leaw $5, %A
    movw (%A), %D
    decw %D
    movw %D, (%A)
    leaw $end, %A
end:
