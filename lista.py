#contar-sumar-promediar
import random
tam=int(input("ingrese valor"))
vec=[]
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)
cont_p=0
cont_i =0
suma_p=0
suma_i=0
for i in range(len (vec)):
    if vec[i]%2==0:
        print(vec[i],'par')
        cont_p+=1
        suma_p+=vec[i]
    else:
        print(vec[i],'ímpar')
        cont_i+=1
        suma_i+=vec[i]
print("pares",cont_p,"impares",cont_i)        
print("impar",suma_i, "pares",suma_p)
print("su promedio")