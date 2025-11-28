# CRIANDO UMA LISTA PARA ARMAZENAR NOMES E NOTAS DE ALUNOS, EXIBINDO A MAIOR NOTA NO FINAL
alunos = []

print("Digite o nome e a nota dos alunos.")
print("Para encerrar, pressione ENTER sem digitar um nome.\n")

while True:
    nome = input("Nome: ")
    if nome == "":
        break  # Sai do loop se o nome for vazio
    nota = float(input("Nota: "))
    alunos.append((nome, nota))  # Armazena como uma tupla (nome, nota)

# Verifica se a lista não está vazia
if alunos:
    # Encontra o(a) aluno(a) com a maior nota usando a função max()
    maior_nota = max(alunos, key=lambda p: p[1])
    print(f"\nO(A) aluno(a) com maior nota é {maior_nota[0]}, com {maior_nota[1]}.")
else:
    print("\nNenhuma aluno foi cadastrado.")