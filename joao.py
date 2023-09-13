#> TASK 1:
#Crie um programa que leia dois números e mostre a soma entre eles.
print("\n//------------------------INICIO-------------------------//\n")
print("/--------------------------TASK1--------------------------/")
num1=input("Digite o primeiro numero:")
num2=input("Digite o segundo numero:")

nums=int(num1)
numss=int(num2)
soma= nums+ numss

print(f"A soma dos numeros são:{soma}")

#>TASK 2:
#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
print("\n/--------------------------TASK2--------------------------/")
numero=int(input("Digte seu numero:"))

sucessor = numero - 1
antecessor = numero + 1

print(f"Sucessor:{sucessor}")
print(f"Antecessor:{antecessor}")

#> TASK 3:
#Crie um algoritmo que leia um número e mostre o seu dobro e triplo.
print("\n/--------------------------TASK3--------------------------/")
numero=int(input("Digte seu numero:"))

dobro = numero * 2
triplo = numero * 3

print(f"dobro:{dobro}")
print(f"triplo:{triplo}")

#> TASK 4:
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print("\n/--------------------------TASK4--------------------------/")
nota1=int(input("Digte a nota um:"))
nota2=int(input("Digte a nota dois:"))
soma=(nota1+nota2)/2

print(f"A nota do aluno e:{soma}")

#> TASK 5:
#Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print("\n/--------------------------TASK5--------------------------/")
valor=int(input("Fale o valor em metros:"))

mult=valor*100
mult2=valor*1000

print(f"A nota do aluno e:{mult2}mm")
print(f"A nota do aluno e:{mult}cm")

#> TASK 6:
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
print("\n/--------------------------TASK6--------------------------/")
numero = int(input("Digite um número inteiro: "))
print("Tabuada de:", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)

#> TASK 7:
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos Dólares ela pode comprar. Considere `US$ 1.00` = `R$ 5.10`
print("\n/--------------------------TASK7--------------------------/")
valor_em_reais = float(input("Digite o valor em reais na sua carteira: R$ "))
taxa_de_conversao = 5.10
quantidade_de_dolares = valor_em_reais / taxa_de_conversao
print(f"Com R$ {valor_em_reais:.2f}, você pode comprar US$ {quantidade_de_dolares:.2f}.")

#> TASK 8:
#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
print("\n/--------------------------TASK8--------------------------/")
preco_original = float(input("Digite o preço do produto: R$ "))
desconto = 0.05 * preco_original
novo_preco = preco_original - desconto
print(f"O novo preço com 5% de desconto é: R$ {novo_preco:.2f}")
print("\n//--------------------------FIM--------------------------//\n")