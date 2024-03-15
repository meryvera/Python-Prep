#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 1
print(a)


# 2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))# In[3]:





# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(a))




# 4) Crear una variable que contenga tu nombre

# In[2]:
name = 'mery'




# 5) Crear una variable que contenga un número complejo

# In[3]:
complex(5j)




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(complex(5j)))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416



# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
v_string = 'True'
v_boolean = True




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(v_string))
print(type(v_boolean))




# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

n_suma = 5 + 4.9
print(n_suma)


# 11) Realizar una operación de suma de números complejos

# In[2]:
n_complex = complex(4 + 3j) + complex(3 + 2j)
print(n_complex)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
suma_random = -4/5 + complex(3 + 2j)
print(suma_random)



# 13) Realizar una operación de multiplicación

# In[5]:
n_multiplicacion = 5 * 4




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

n_potencia = 2 **8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

n_coc = 27 / 4
print(n_coc)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(int(n_coc))




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

print(27 % 4)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:





# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

n_alfanumerico = 'hola' + 'mundo'
print(n_alfanumerico)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
2 == '2'

# False, porque el primer 2 es un número entero y el segundo es un string


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
str(2)=='2'




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a_error = float('3,8')
# error porque el separador de decimales es el punto y no la coma
# error porque no se puede convertir string a float si el string tiene más de un punto decimal
# lo correcto es a_error_2 = int('3')


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

x = 3
x -= 1
print(x)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
n_binario = 1 << 2
print(n_binario)

# retorna 4 en sistema decimal, porque en binario es 0001 y al correr 2 posiciones a la izquierda queda 0100 que es 4 en decimal

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print(2 + '2')
# porque ambos operandos no son del mismo tipo, uno es entero y el otro es string




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
n_valido = 2 + int('2')
print(n_valido)


# %%
