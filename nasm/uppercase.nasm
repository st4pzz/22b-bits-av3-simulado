;-------------------------------------
; uppercase.nasm
; Leita o README.md para informacòes
;-------------------------------------


leaw $8, %A
movw %A, %D
leaw $0, %A
movw %D, (%A)

BEGIN:
; é zero?
    leaw $0, %A
    movw (%A), %A
    movw (%A), %D
    leaw $END, %A
    je
    nop

; é menor que a (97)?
    leaw $0, %A
    movw (%A), %A
    movw (%A), %D
    leaw $97, %A
    subw %D, %A, %D
    leaw $INC, %A
    jl
    nop

; é menor que 122?
    leaw $0, %A
    movw (%A), %A
    movw (%A), %D
    leaw $122, %A
    subw %D, %A, %D
    leaw $INC, %A
    jg
    nop

; é UPPER
    leaw $0, %A
    movw (%A), %A
    movw (%A), %D
    leaw $32, %A
    subw %D, %A, %D
    leaw $0, %A
    movw (%A), %A
    movw %D, (%A)

INC:
    leaw $0, %A
    movw (%A), %D
    addw %D, $1, (%A)

LOOP:
    leaw $BEGIN, %A
    jmp
    nop

END:
