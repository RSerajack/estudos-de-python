#Percorrendo uma lista com um laço
#Crie um programa que tem uma lista de números e retorna para o usuário qual número é ou não primo. O programa deve conter um laço e percorre a lista.
#Use a seguinte lista no exemplo: [1, 2, 5, 10, 16, 17, 21, 22, 23, 54, 30]

lista_num = [1, 2, 5, 10, 16, 17, 21, 22, 23, 54, 30];

for num in lista_num:
	cont = 0
	for i in range(2, num):
		if(num%i==0): cont+=1;
	if(cont>0): print("Primo");
	else: print("Não primo");

#Saídado programa:
#Primo
#Primo
#Primo
#Não primo
#Não primo
#Primo
#Não primo
#Não primo
#Primo
#Não primo
#Não primo
