#Martinez Almanza Anahi
#Montes Rubio Yasmin
"""

 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
"""
def gPrimo(N):
        """ Comprobar si n es primo"""
        def esPrimo(R):
                if R <= 1:
                        return False
                
                for i in range(2,R):
                        if R % i == 0:
                                return False
                return True

        R = 0
        while(R <= N):
                if esPrimo(R):
                        yield R
                R += 1

a = gPrimo(10)
z = [e for e in a]
print(z)
#[2,3,5,7]

"""
Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
def genBadaBoom(N):
	R=1
	while R <= N:
		Bada = R % 3 == 0
		Boom = R % 5 == 0
		if Bada and Boom:
			yield "BadaBoom!!"
		elif Bada:
			yield "Bada"
		elif Boom:
			yield "Boom"
		else:
			yield R
		R = R + 1

a = genBadaBoom(10)
z = [e for e in a]
print(z)
#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]

"""
Combinaciones <Comprensión de listas> 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
A = ['camisa roja','camisa negra','camisa azul','camisa morada','camisa cafe']
B = ['pantalon negro','pantalon azul','pantalon cafe oscuro','pantalon crema']
D = ['cinturon','tirantes','lentes','fedora']

C = [[a,b,d] for a in A for b in B for d in D ]
print (C)
print(len(C))
"""
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
"""
N = [ c for c in C if c[2]=='fedora']
print(N)
print(len(N))

"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
from functools import reduce


lis = ["""There's a hole in my heart, in my life, in my
     way And it's filled with regret and all I did, to push you away
    If there's still a place in your life, in your heart for me
    I would do anything, so don't ask me to leave
    I've got a hole in my soul where you use to be
    You're the thorn in my heart and you're killing me
    I wish I could go back and do it all differently
    I wish that I'd treated you differently
    'Cause now there's a hole in my soul where you use to be"""]


def contar(e, l):
    v = 0
    for i in l:
        if e == i:
            v += 1
    return v + 1

def unicos(l):
    co = []
    c = []
    n = []
    if not l:
        return []
    p = l[0]
    for i in p:
        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)

    for a in c:
        co.append(contar(a, n))
    v = reduce(lambda a,b: a + b, co)
    print('Probabilidad: 1 /',v)
    letras = list(zip(c, co))
    print('Lista de letras que existen y cuantas veces se repite\n',letras)
  
    return letras

s = unicos(lis)
f = filter(lambda a: a[1] == 1, s)
d = list(f)
print('\nLetra(s) con menos aparicion en el texto')
print('\n',d)
