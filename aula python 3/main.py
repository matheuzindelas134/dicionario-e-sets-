#faca um programa que pede para o usuario inserir o nome de um aluno e a nota desse mesmo aluno e add ele a uma lista ate o usuario digitar "fim"
#entao mostre na tela o nome do aluno que obteve a melhor nota 

listas_alunos = []

while True:
    aluno = str(input("digite o nome do aluno: ")) 
    if aluno == "fim":
        break
    nota = float(input("digite a nota do aluno: "))
    listas_alunos.append([nome,nota])

maior_nota = 0
melhor_aluno = ""

for aluno in lista_alunos:
    if aluno[1] > maior_nota:
        maior_nota = aluno[1]
        melhor_aluno = aluno[0]

print(f"o melhor aluno foi {melhor_aluno},com a nota {melhor_nota}: ")