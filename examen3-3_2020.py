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
A = ['roja','negra','azul','morada','cafe']
B = ['negro','azul','cafe oscuro','crema']
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
