'''
Una empresa que se dedica a fabricar bicicletas, produce de lunes a sábado en nfábricas ubicadas en diferentes lugares del país.
Se solicita guardar en una matriz la cantidad de bicicletas fabricadas por cada una de sus fábricas durante una semana.
Cada columna representa el día de la semana (Lunes columna0, Martes columna1, etc.) y cada fila representa cada una de sus fábricas.
El número de fábrica coincide con el número de fila+1 (a continuación se presenta un ejemplo).

Se solicita crear al menos una función para cada ítem:
a.Generar al azar (entre 1 y 6) la cantidad de fábricas y simular la cantidad de bicicletas fabricadas para cada día,
considerando que la capacidad máxima de fabricación es de N unidades y puede suceder que la cantidad sea cero.N se solicita por teclado.
Considerando que los sábados se trabaja al 50% de la producción, por lo que debe asignar la mitad entera del valor creado al azar.

b.¿Cuál es el día menos productivo y a qué día/s y fábrica/s pertenece?

c.Se solicita pasar todas las cantidades fabricadas de la triangular inferior a una lista.

d.Ordenar las cantidades fabricadas de la lista anterior utilizando sort en una determinada rebanada, recibir por parámetro desde y hasta.
Por omisión, ordenar la lista completa. 
'''
import random
#DICCIONARIOS AUX
diccDias={0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",4:"Viernes",5:"Sabado"}
diccFabricas={0:"Fabrica 1",1:"Fabrica 2",2:"Fabrica 3",3:"Fabrica 4",4:"Fabrica 5",5:"Fabrica 6"}

#FUNCIONES
'''FUNCION PARA VALIDAR QUE UN NUMERO CUMPLA CON UNA CONDICION'''
def ValidarUnicaCondicionMIN(Cond):
    '''
    pre: Se recibe una condicion minima (valor minimo que limita al valor recibido) y un valor.
    pos: Se devuelve el valor el cual se confirmo que es mayor a la condicion.
    '''
    iValor=int(input("Ingrese un valor:"))
    while iValor<Cond:
        iValor=int(input("Error- Se ingreso un numero invalido, vuelva a intentarlo:"))
    return iValor
def ValidarUnicaCondicionMAX(Cond,Min=1):
    '''
    pre: Se recibe una condicion maxima (valor maximo que limita al valor recibido) y un valor.
    pos: Se devuelve el valor el cual se confirmo que es menor a la condicion.
    '''
    iValor=int(input("Ingrese un valor:"))
    while iValor>Cond or iValor<Min:
        iValor=int(input("Error- Se ingreso un numero invalido, vuelva a intentarlo:"))
    return iValor

'''FUNCION PARA CREAR UNA MATRIZ RECURSIVA'''
def crearMatrizRecursiva(iFilas,iColumnas,iF=0,iC=1,Matriz=[[0]]):
    '''
    Objetivo: Crea una matriz llena de ceros utilizando recursividad. 
    Pre: Recibe el numero de filas/columnas que se desea que contenga la matriz, el numero de fila sobre la cual se van a agregar columnas
    (en el caso de que no se indique es cero) y una matriz (en el caso de que no se indique, se crea una matriz vacia).
    Pos: Se devuelve la matriz de FilasxColumnas, rellena de ceros.
    '''
    if iColumnas==0 or iFilas==0: #Retorna una matriz vacia si no se indica cantidad de filas o columnas.
        Matriz=[]
    if iC<iColumnas and iFilas!=0: #En este primer caso, la fila sobre la cual se esta iterando, aun no tiene la cantidad de columnas pedidas
                                #por el usuario.../Caso recursivo
        Matriz[iF].append(0) #Se agrega una columna a la fila sobre la cual se esta iterando.
        crearMatrizRecursiva(iFilas,iColumnas,iF,iC+1,Matriz) #Se vuelve a llamar a la funcion.
    elif iC==iColumnas and len(Matriz)<iFilas:#Si la no se dio la condicion anterior, la cantidad de columnas es igual a la pedida
                                                        #por el usuario y la cantidad de filas aun es menor a la de la condicion, entonces...
                                                        #/Caso recursivo.
        Matriz.append([0]) #Agrega una nueva fila.
        iF+=1 #Se suma uno al contador de filas.
        crearMatrizRecursiva(iFilas,iColumnas,iF,1,Matriz) #Se vuelve a llamar a la funcion.
    #Si no se da ninguna de las condiciones anteriores, se retorna la matriz de filasxcolumnas (especificadas por el usuario)
    #rellena de ceros. /Caso base.
    return Matriz
    
'''CARGAR UNA MATRIZ CON NUMEROS ALEATORIOS --> RECURSIVO'''
def cargarMatrizAleatorios(Matriz,iMin,iMax,iC=0,iF=0):
    '''
    Objetivo: Llenar una matriz utilizando recursividad. 
    Pre: Recibe la matriz a llenar de numeros aleatorios, un minimo de valor aleatorio a generar y un maximo. Ademas, recibe un valor de
    columna (iC) y uno de fila (iF) que determinan la posicion a rellenar, y si no se brinda un valor, se les asigna el 0.
    Pos: Se carga la matriz con numeros aleatorios.
    Se debe importar para usar esta funcion, el modulo "random".
    '''
    if len(Matriz)>iF and len(Matriz[iF])>iC:
        iNum=random.randint(iMin,iMax)
        Matriz[iF][iC]=iNum
        cargarMatrizAleatorios(Matriz,iMin,iMax,iC+1,iF)
    elif len(Matriz)>iF and len(Matriz[iF])==iC:
        iF=iF+1
        iC=0
        cargarMatrizAleatorios(Matriz,iMin,iMax,iC,iF)

'''FUNCION PARA BUSCAR MINIMO'''
def BuscarMinimo(Matriz,f=0):
    '''
    pre: Recibe una matriz y un numero de fila (si no lo recibe es 0).
    pos: Busca de forma recursiva, los valores minimos de cada fila a partir de la fila que se le pasa por parametro, devolviendo el minimo
    valor que se encuentre dentro de esas filas.
    '''
    CantFilas=len(Matriz)
    if f!=CantFilas: #Caso recursivo, siempre que la cantidad de filas sea distinta a la recibida por parametro.
       iValor= min(Matriz[f])
       iMinRecursivo=BuscarMinimo(Matriz,(f+1))
       if iValor>iMinRecursivo: #Compara el minimo que trae de las filas recursivas con el de esta fila y se queda con el minimo. 
           iValor=iMinRecursivo
    else: #Caso base -> Devuelve el maximo valor de la fila anterior, que al compararlo siempre sera mayor que el minimo y no se tendra en cuenta. 
        iValor= max(Matriz[(f-1)])
    
    return iValor

'''FUNCION PARA MOSTRAR MATRICES--> RECURSIVO'''
def MostrarMatriz(Matriz,iF=0,iC=0):
    '''
    Objetivo: Muestra una matriz con recursividad.
    Pre: Se recibe una matriz, y los parametros iF e iC que indican las filas y columnas sobre las cuales se itera (Estos ultimos dos parametros no deben
    modificarse, por lo que no se ingresan cuando se llama a la funcion).
    pos: Se muestra la matriz de forma ordenada.
    '''
    iFilas=len(Matriz)
    iColumnas=len(Matriz[0])
    if iF<iFilas:
        if iC<iColumnas:
            print(f'{Matriz[iF][iC]:4d}', end="")
            MostrarMatriz(Matriz,iF,iC+1)
        else:
            print()
            iC=0
            iF=iF+1
            MostrarMatriz(Matriz,iF,iC)
        
'''FUNCION PARA BUSCAR EL VALOR MINIMO DENTRO DE UNA LISTA Y LAS POSICIONES EN LAS QUE SE UBICA --> TIENE BAJO ACOPLAMIENTO
ASI QUE CONVIENE REVISAR ANTES DE VOLVERLA A UTILIZAR EN OTRO PROGRAMA (ME COSTO MUCHO ESTA PARTE'''
def BuscarMinimoPosicion(iLista,iValor,Fila,Fabricas,Dias): #Esta adaptado para trabajar con cada fila de la matriz como si fuera una lista
    '''
    pre:Se recibe una lista.
    pos:Se devuelve cual es el valor minimo y en que posiciones se ubica.
    '''
    iTotalCant=len(iLista)
    iMin=iValor
    iPosMin=[]
    for i in range(iTotalCant):
        iMenorAux=iLista[Fila][i] #Evalua cual es el numero que esta en cada posicion de la lista
        if iMin==iMenorAux: #Si mi numero minimo igual que el numero de la posicion i de mi lista....
                iPosMin.append(i)
    if len(iPosMin)>0:
        print("La fabrica", Fabricas[Fila], "fabrico esa cantidad de bicicletas el/los dia/s:")
        for i in range(len(iPosMin)):
            NumAux=iPosMin[i]
            print(Dias[NumAux])

'''FUNCION QUE DEVUELVE LOS ELEMENTOS DE LA TRIANGULAR INFERIOR DE UNA MATRIZ CUADRADA EN UNA LISTA'''
def TriangularMatriz(Matriz,iF=1,iC=0,Elementos=[]):
    '''
    Objetivo: Guarda en una lista los datos de la triangular inferior de una matriz, usando recursividad.
    Pre: Recibe una matriz a sumar los elementos de su triangular inferior y datos necesarios para la recursividad, pero que no se deben ingresar
    como parametros.
    Pos: Devuelve una lista con todos los elementos de la matriz inferior de la matriz.
    Error: En el caso de que no sea cuadrada (no se pueda triangular) se retornara la lista vacia.     
    '''
    iFilas =len(Matriz)
    iColumnas=len(Matriz[0])
    if iFilas!=iColumnas:
        Elementos=[]
    elif iF<iFilas:
        Elementos.append(Matriz[iF][iC])
        if iF==(iC+1):
            iC=0
            TriangularMatriz(Matriz,iF+1,iC,Elementos)
        else:
            TriangularMatriz(Matriz,iF,iC+1,Elementos)            
    return Elementos

'''FUNCION QUE ORDENA UNA LISTA CON SLICES'''
def OrdenarSlices(Lista,iInicio=0,iFin=0):
    '''
    Objetivo: Ordena una lista desde el ingreso como inicio, hasta el ingreso como fin.
    Pre: Se ingresa como parametro la lista a ordenar, el indicador de donde debe comenzar a ordenar y el indicador de donde debe dejar de ordenar.
    ->Si iInicio e iFin, se omiten, se ordenara toda la lista.
    Pos: La salida o parte de ella, ordenada.
    '''
    if iFin==0:
        iFin= len(Lista)
    Lista=Lista[iInicio:iFin]
    Lista.sort()
    return Lista
        
#PROGRAMA PRINCIPAL
def main():
    print("Hola! Ingrese el numero de fabricas de la empresa (Entre 1 y 6)")
    nFabricas= ValidarUnicaCondicionMAX(6)
    print()
    print("Cual es el numero maximo de bicicletas que una fabrica puede fabricar (Mayor a 0)")
    N=ValidarUnicaCondicionMIN(0)
    mPrincipal=crearMatrizRecursiva(nFabricas,6)
    cargarMatrizAleatorios(mPrincipal,0,N)
    #Division de los sabados
    for f in range(len(mPrincipal)):
        iValor=mPrincipal[f][5]
        mPrincipal[f][5]=iValor//2
    print()
    print("Matriz de dias (columnas(Lunes a Sabado)) y fabricas (filas):")
    MostrarMatriz(mPrincipal)
    #print(mPrincipal)
    print()
    iMin=BuscarMinimo(mPrincipal)
    print("Numero minimo de bicicletas fabricadas en un mismo dia por una misma fabrica:",iMin)
    print()
    for f in range(len(mPrincipal)):
        BuscarMinimoPosicion(mPrincipal,iMin,f,diccFabricas,diccDias)
    Elementos=TriangularMatriz(mPrincipal)
    if len(Elementos)==0:
        print("La matriz no era cuadrada asi que no se pudo triangular.")
    else:
        print("La lista de los elementos de la matriz triangular inferior es",Elementos)
        print("Dicha lista ordenada quedaria", OrdenarSlices(Elementos))
    
if __name__=="__main__":
    main()