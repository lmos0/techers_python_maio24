#Recursão é uma técnica na qual uma função chama a si mesma, a fim de solucionar um problema

repetir = 0

def fatorial(n):
    global repetir
    repetir +=1
    #Caso base é o modo de operação padrão normal do bloco de código
    if n == 0 or n == 1:
        return 1
     #Caso recursivo: a condição na qual a função precisa chamar a si mesma
    else:
        return n * fatorial(n-1)
    


   
recursao = fatorial(5)
print(repetir)

#### Ordem de entrada na Pilha
#fatorial(5) => ser interrompida => 'fatorial(4) 
#fatorial(4) => ser interrompida => fatorial(3)
#fatorial(3) => ser interrompida => fatorial(2)
#fatorial(2) => ser interrompida => fatorial(1)


#Ordem de saída da pilha
#fatorial(1) => ser concluida => retornar 1 (caso base)
#fatorial(2) => ser concluída => 2*1 = 2
#fatorial(3) => ser concluída =>  3*2 = 6
#fatorial(4) => ser concluída => 4 * 6 = 24
#fatorial(5) => ser concluida 5*24 - 129

