N = int(input())

pizzas = []

for ing in range(N):
	ingredientes = []
	for i in range(3):
		ingredientes.append(input())
	pizzas.append(ingredientes)	

busca = input()
	
#print(pizzas)
cont = 0

for pizza in pizzas:
	if busca in pizza:
		cont+=1
		
print(cont)
