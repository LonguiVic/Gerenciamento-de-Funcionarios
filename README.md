# Gerenciamento-de-Funcionarios

Este é um programa de gerenciamento de funcionários, que classifica os funcionários com base em diferentes critérios. O programa é baseado nos seguintes conjuntos de dados:

-funcionarios: um conjunto que contém os nomes de todos os funcionários da empresa.

-turno_dia: um conjunto que contém os funcionários que trabalham no turno diurno.

-turno_noite: um conjunto que contém os funcionários que trabalham no turno noturno.

-possuem_carro: um conjunto que contém os funcionários que possuem um carro.

Como usar:

-Clone ou faça o download deste repositório.

-Execute o arquivo gerenciamento_funcionarios.py em um ambiente Python.

-O programa irá calcular e exibir três listas:

-lista_carro_noite: uma lista dos funcionários que trabalham no turno noturno e possuem um carro.

-lista_carro_dia: uma lista dos funcionários que trabalham no turno diurno e possuem um carro.

-sem_carro: uma lista dos funcionários que não possuem um carro.

-Os resultados serão impressos no console.

Exemplo:

funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}

turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}

turno_noite = {'Pedro', 'Sophia', 'Bruno'}

possuem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista_carro_noite = ['Bruno']

lista_carro_dia = ['Marcos', 'Alice', 'Melissa']

sem_carro = ['Sophia', 'Ana', 'Pedro']

print(f"Funcionários no turno noturno que possuem carro: {lista_carro_noite}")

print(f"Funcionários no turno diurno que possuem carro: {lista_carro_dia}")

print(f"Funcionários que não possuem carro: {sem_carro}")

Notas:

-Certifique-se de ter o Python instalado em seu sistema.

-Este projeto é apenas um exemplo básico de gerenciamento de funcionários e pode ser adaptado para atender a requisitos específicos.

-Sinta-se à vontade para personalizar ou aprimorar este código de acordo com suas necessidades.
