lista_alunos = []

def adiciona():
   op= input('digite 1 para adicionar aluno :')
   if op == '1' and op != None:
       lista_alunos.append(input('digite nome aluno : '))
       return adiciona()

adiciona()

print(lista_alunos)
