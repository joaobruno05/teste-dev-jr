# Teste Desenvolvedor Júnior
<br>

## Challenge 1

Desenvolva um código permitindo ao usuário digitar os 3 lados de um triângulo. Baseado nos 3
valores digitados, deverá ser exibido se o triangulo é “inválido”, “equilátero”, “isósceles” ou
“escaleno”.
Regras:
- Um triângulo existe se, somente se, um de seus lados for maior que a diferença dos outros
dois lados, e menor que a soma dos outros dois lados.
- Um triangulo equilátero possui seus 3 lados com a mesma medida.
- Um triangulo isósceles possui dois de seus lados com a mesma medida.
- Um triangulo escaleno possui cada lado com uma medida diferente.
<br>

## Challenge 2

Desenvolva uma aplicação para exibir na tela, com o uso de recursividade, os 30 primeiros
resultados da “Sequência de Fibonacci”.
- Sequencia básica de Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
<br>

## Challenge 3
Considerando o diagrama de classes abaixo, temos um objeto “List&lt;Casa&gt; casas” que pode conter
N elementos. Exiba para o usuário o “Endereço”, “Metragem” e a quantidade de “Comodos”
apenas das casas que possuam pelo menos 1 comodo com numero par de janelas.

#### Casa
- +Endereço : string
- +Cor : string
- +Metragem : int
- +Comodos : List&lt;Comodo&gt;  

#### Comodo
- +Nome : string
- +Janelas : int
- +Portas : int

Considerações:
- No “Endereço” já vem preenchido o numero do imóvel e o tipo de logradouro.
- Exibir no seguinte formato: “Rua Castro Alves 550 – 10m² - 3 comodos.”
