; senha???
; Você foi chamado para desenvolver uma fechadura
; eletronica com o processador Z01.
;
; O cliente pediu para a fechadura ter a funcionalidades a seguir:
;
; A senha é definida pelo valor salvo em RAM[0]
; O usuário insere uma senha pelas chaves (SW) da placa.
; Em caso da senha estar correta: acender o LED[0]
; Em caso da senha estar errada: acender todos os LEDs
; O sistema deve ficar em loop verificando se o usuário digitou a senha correta/ errada (configurou as chaves corretamente)


loop:


    leaw $21185, %A

    movw (%A), %D

    leaw $0, %A

    subw %D, (%A), %D

    leaw $certo, %A

    je %D

    nop



errado:

    leaw $6, %A

    movw %A, %D

    leaw $21184, %A

    movw %D, (%A)

    leaw $end, %A

    jmp

    nop



certo:

    leaw $21184, %A

    movw $1, (%A)

    leaw $end, %A

    jmp

    nop



end:

