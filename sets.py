# Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

# Lista1 = Funcionários que tem carro e trabalham a noite
# Lista2 = Funcionários que tem carro e trabalham durante o dia
# Lista3 = Funcionários que não tem carro

funcionarios = {'Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
possuem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista_carro_noite = []
lista_carro_dia = []
sem_carro = []

set_carro_noite = turno_noite.intersection(possuem_carro)
print(list(set_carro_noite))

set_carro_dia = turno_dia.intersection(possuem_carro)
print(list(set_carro_dia))

set_sem_carro = funcionarios.symmetric_difference(possuem_carro)
print(list(set_sem_carro))
