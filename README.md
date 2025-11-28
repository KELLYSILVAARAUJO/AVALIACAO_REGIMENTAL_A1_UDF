# AVALIACAO_REGIMENTAL_A1_UDF 
# 🐍 Projeto de Fundamentos em Python:
Este projeto consiste em quatro arquivos que demonstram conceitos essenciais da linguagem Python: estruturas de repetição, estruturas condicionais, listas e dicionários.
# ARQUIVO: if_elif_else.py - Estruturas Condicionais
Este script demonstra como usar as estruturas if, elif e else para gerenciar diferentes cenários de decisão (lógica de exclusão mútua).

⚙️ Lógica Implementada
O sistema verifica a idade do usuário para permitir ou restringir a entrada em um evento:
if	- Idade menor que 16 acesso negado.
elif - Idade entre 16 e 17 acesso permitido, mas acompanhado de um responsável.
else - Idade maior ou igual a 18 acesso liberado (cobre todos os outros casos).

🔑 Argumentos
idade: Valor inteiro (int) capturado via input().

# ARQUIVO: for_while.py - Estruturas de Repetição
Este script resolve o seguinte problema — imprimir números pares de 1 a 100 — usando as duas principais formas de laço em Python.

🔄 Implementação com for
A abordagem mais utilizada, utilizando a função range(1, 101) para gerar a sequência e um if para aplicar a condição de paridade (numero % 2 == 0).

🔄 Implementação com while
Requer inicialização (numero = 1), a condição de continuação (while numero <= 100) e o incremento manual (numero += 1) para evitar um loop infinito.

🔑 Conceitos
Paridade: Verificada pelo operador de módulo (%), que retorna o resto da divisão. Se resto == 0, o número é par.


# ARQUIVO: listas.py - Listas
O script demonstra o armazenamento de dados estruturados em uma lista e a busca eficiente do valor máximo.

📋 Estrutura de Dados
alunos = []: Uma lista é usada para armazenar todos os registros.

(nome, nota): Cada registro é armazenado como uma tupla, garantindo que o nome e a nota permaneçam juntos e imutáveis.

🔑 Requisito
Entrada Dinâmica: O loop while True coleta dados indefinidamente, parando apenas quando o usuário digita um nome vazio ("").

# ARQUIVO: dicionarios.py - Sistema de Cadastro com dict()
Este script implementa um sistema interativo simples para gerenciar produtos, utilizando o dicionário como a principal estrutura de armazenamento.

🔑 Uso Correto de dict()
O armazenamento segue o padrão chave-valor:

Chave (Key): O nome do produto (nome).

Valor (Value): O preço do produto (preco).

O dicionário é inicializado com produtos = dict().

🛒 Inserção e Recuperação
Inserção: É realizada diretamente pela sintaxe produtos[nome] = preco.

Recuperação (Listagem): É feita iterando sobre o dicionário usando o método .items(), que fornece acesso simultâneo à chave (nome) e ao valor (preco).

🛠️ Estrutura
O código é organizado em funções (inserir_produto, listar_produtos) e um Menu Interativo com while True para uma experiência de usuário funcional.
