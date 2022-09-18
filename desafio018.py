import desafio014
import random

alunos = desafio014.lista_alunos
random.shuffle(alunos)
print('o embaralhado', alunos)
print('aluno sorteado : ', alunos[random.randrange(len(alunos))])