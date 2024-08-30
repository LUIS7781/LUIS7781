     Iteradores e iterables   
    1. A  partir de una lista  vacia,  utilizar un ciclo while para cargar alli numeros numeros negativos  del 15al 1
    
    lista = [] # Crea   una lista  vacia 
    n = -15   # Inicializa  La variable  n  con el valor  -15 
    while n  < 0:  # Mientras  n sea  menor  que 0, se ejecuta el bucle 
     lista. append (n)  # Agrega  el valor  de n  a  la lista 
      n += 1  # Incrementar  el valor  de  n en 1  en cada  iteracion 
     print (lista)  #  Imprimie  La  lista  resultante 
[-15,  14, -13,-12 , -11, -10, -9, -8,- 7, -6, -5, -4,-3,-2.- 1] 
 

n = 0 # Incializa  La   variable n con  el valor  0 

while n < len (lista): # Miestras n sea  menor que  La Longgitud  de La Lista  se ejecuta el bucle 
  if lista [n] % 2 ==  0: # verifica si  el elemento en la posicion n de la lista es divible por 2 
      print (lista) [n] )   #  Imprime  el elemento si  cumple la  condicion'
  n  += 1  # Incrementa el valor  de n  1 en cada  iteracion  
  
for elementos in lista: # Itera  sobre cada  elementos  de la  Lista 
  if elementos % 2  == 0:  # verifica si  el elementos si  cumple  La condicion 


    for  elementos  in lista [:3]:  # Imprime  cada elemento  
      

      # La i,  e in enumererate (lista):  # Itera  sobre  la lista  y obtiene el elementos en cada  iteracion 
      print(i,  e)  # Imprime  el indice y el elemento  

   lista = [ 1, 2,5,7,8,10,13,14,15,17,20] 
    n= 1  # IniciaLiza  La variable n  con el valor 1 
      
    while n < =20:  # Mientras n  sea  menor  o igual  a 20,  se ejecuta el bucle 
        if    not (n  in  lista) :  # verifica  si  n no  esta presente  la lista 
          
        print (lista)   # Imprime la lista resultante 


    [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
  
  
  fibo = [0, 1]  # crea  una lista inicial  con los  primeros  dos numeros  de la  secuencia de fibonacci 

  n = + = 1  # Imprime  la lista  de lista   secuencia  de  Fibonacci 

 [0, 1,1,2,3,5,8,13.21,34,55,89,144.233,337,610,987, 1597, 2584, 4181, 10946,17711, 28657,463368, 75 
  025, 121393, 1964418,317811,514229] 


# la  funcion  sun para calcular  la suma  de los elementos  de la lista fibo.
sum(fibo)  

ni-1/ni   
ni2/ni-2  
ni-3/ni3  
ni-5/ni-4 

primeros = 15 # numero   de  elementos  que  se  imprimiran 
n = primeros - 5  #  valor  inicial de n  

while n  < primeros:  #  Mientras  n  sea  menor  que numero    de elementos  a imprimir, se ejecuta  el bucle 
  print (fibo) [n]  / fibo[n   - 1 ])    # Imprime el resultado  de la  division de los  elementos  consecutivos de la lista fibo 
  n += 1  # Incrementa  el valor   de  n en 1 en cada iteracion   

  1.61764705588235294   
1.1.6181818181818182
1.6181818181818182
1.6179775280898876
1.6180555555555556
1.6180257510729614

  
cadena=  `hola  Mundo. Esto una practica  del lenguaje  de programacion python^ 

for  i, c in  enumerate (cadena ):  # Itera  sobre  la cadena  y  obtiene  el  indice y el caracter en cada iteracion 
if  c ==  "n" :  # Verifica  si el caracter  es igual a "n" 
      print (i)  # Imprime  el  indice  correspodiente  al  caracter `n` 

7
21 
39
60
67
 
 dicc =  {  
    Cuidad  :  [Buenos Ai [res"  "Caracas" "" Bogota":     Lisboa:"  "Roma]
    "pais" : [" Argentina"  Venezuela"  Colombia"  portugal,  Italia]; 
     Continente : [ America,  America,  America, Europa,  Europa, ] 
 } 
 for  i  in  dicc:  # Itera  sobre   las claves  del diccionario 
         print (i )# Imprime cada clave 
  
  cadena =   Hola  mundo . Esto  es una  practica del lenguaje de programacion  pyton
  print(type)(cadena)   #  Imprime  el tipo  de dato de la varible  cadena  despues de  convertirla en una lista 

  <class  "str"> 
  <class   "list"> 

  recorre = inter (cadena)   #  (cadena)  # Crea un iterador a patir de la  cadena 
  largo = len(cadena)  #Obtiene la longit largoud  de la  cadena 
   for  i in range (0, largo):  # Itera sobre el rango  de  indices  desde  0 hasta  largo -1 
    print (next) (recorre))  # Imprime  el proximo  elementos  del  iterador 
    

    lis1= [  run, fly, sleep ]  
    list2=[ correr,   valar,  domir,]  
     lisz  =  zip (list1)  list2)  # comobina  los elementos  de list1  ylist2  en pares 
      print(type(lisz))  # Imprime el tipo  de dato lisz 
       print(list(lisz)  # convierte lisz en una  lista  y  la  imprime 
        



<class       zip
#  [( "run , correr), (fly,  volar), (sleep, domir )] 
   
   lis= [18,21,29,32,35,42,56,60,63,71,84,90,91, 100]  # Definicion de la Lista original 

                   
    lis2= [i for i in lis if i % 7== 0]  # comprension de lista para filtrar elementos divisibles por 7
    print (list2)  # Impresion de la  lista resultante 

    [21, 35, 42,56,63, 84,91] 
 ,
      lis = [[ 1,2,3,4], rojo verde, [True, False, False] [ uno, dos, tres ]] 

        type (lis) cantidad  =0  # Inicializacion  del  contador de  elementos 

         if type(elementos) == list:  # verificacion si el elementos es una  lista 
         cantidad  += len (elementos ) # si  es una   lista, se incrementa  el contador por la cantidad de elementos  en esa lista 
          else:  
          cantidad + = 1  # si  no es  lista, se incrementa el  contador  por 1, ya que se trata de un solo elementos 

          print( La  cantidad  += 1  # si  no es  una lista,  el contador por 1, ya que  se trata de un solo  elemento 
              for indice, elemento in enumerate(lis):  # Iteración sobre cada elemento de la lista 'lis' junto con su índice
    if type(elemento) != list:  # Verificación si el elemento no es una lista
        lis[indice] = [elemento]  # Si no es una lista, se reemplaza por una lista que contiene ese elemento

print(lis)  # Impresión de la lista modificada   
  
  for indice, elemento in enumerate(lis):  # Iteración sobre cada elemento de la lista 'lis' junto con su índice
    if type(elemento) != list:  # Verificación si el elemento no es una lista
        lis[indice] = [elemento]  # Si no es una lista, se reemplaza por una lista que contiene ese elemento

[[ 1,2,3,4,]  [ rojo ,[ verde],  [ True, False,  False] [uno, Dos , Tres]]  
 
         

        
     

    
