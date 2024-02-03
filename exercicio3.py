"""3 - Ler dois números, armazenando-os nas variáveis num1 e num2. Verificar se o valor de 
num1 é maior que o valor de num2 e, em caso positivo, trocar os conteúdos das variáveis. """

a = float(input("digite o valor do primeiro numero : "))
b = float(input("digite o valor do segundo numero : "))
if a>b :
    aux = a
    a = b
    b = aux 
    print("o numero é " , str(b) , str(a))

print('final')