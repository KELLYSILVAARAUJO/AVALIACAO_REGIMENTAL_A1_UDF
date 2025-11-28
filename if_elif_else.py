# USO DE ESTRUTURAS CONDICIONAIS USANDO: IF, ELIF E ELSE. 
# SIMULAÇÃO DE VERIFICAÇÃO DE IDADE PARA UM EVENTO AO QUAL É PERMITIDA A ENTRADA DE PESSOAS COM IDADE IGUAL OU MAIOR QUE 16 ANOS.

idade = int(input("Digite a sua idade: "))


# VERIFICANDO SE A IDADE É MENOR QUE 16 ANOS:
if idade < 16:
    print("Infelizmente, você não tem idade suficiente para participar desse evento!")

# VERIFICANDO SE A IDADE ESTÁ ENTRE 16 E 17 ANOS (MENOR QUE 18):
elif 16 <= idade < 18:
    print("Você pode participar do evento acompanhado(a) de um responsável que seja maior de idade!")

# O ELSE PEGA AUTOMATICAMENTE TODAS AS IDADES >= 18 ANOS.
else: 
    print("Olá! Será uma honra tê-lo(a) em nosso evento!")