
#? Importamos las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#! Definimos las funciones: f, g, h y p
#? f
def f(x):
    #* Dibujará la primera curva del corazón
    return np.sqrt(1 - (x - 1)**2)

#? g
def g(x):
    #* Dibujará la curva opuesta a f(x)
    return np.where(((-x - 1)**2 <= 1), np.sqrt(1 - (-x - 1)**2), np.nan)

#? h
def h(x):
    #* Dibujará la linea que se une a la otra mitad de corazón
    y = np.sqrt(x / 2)
    return np.where((x >= 0) & (x <= 2) & (y <= 1), (-5 / 2) * np.sqrt(1 - y), np.nan)

#? p
def p(x):
    #* Dibujará la linea opuesta a h(x)
    y = np.sqrt(-x / 2)
    return np.where((x >= -2) & (x <= 0) & (y <= 1), (-5 / 2) * np.sqrt(1 - y), np.nan)


#? Definimos los intervalos
x_val = np.linspace(0, 2, 1000) #todo para positivo
x_val_neg = np.linspace(-2, 0, 1000) #todo para negativo

#? Calculamos las funciones en el intervalo
f_val = f(x_val) #todo dibujado de izquierda a derecha
h_val = h(x_val) #todo dibujado de izquierda a derecha
g_val = g(x_val_neg) #todo dibujado de derecha a izquierda
p_val = p(x_val_neg)#todo dibujado de derecha a izquierda

#? Usamos matplotlib para graficar nuestras funciones
plt.figure(figsize=(10, 6))#! Lienzo

#? Muestra la primer curva
plt.plot(x_val, f_val, label='f(x) = sqrt(1 - (x - 1)^2)', color='r')

#? Muestra la segunda curva
plt.plot(x_val_neg, g_val, label='g(x) = sqrt(1 - (-x - 1)^2)', color='r')

#? Muestra la primer linea
plt.plot(x_val, h_val, label='h(x) = (-5/2) * sqrt(1 - sqrt(x/2))', color='r')

#? Muestra la segunda linea
plt.plot(x_val_neg, p_val, label='p(x) = (-5/2) * sqrt(1 - sqrt(-x/2))', color='r')


plt.xlabel('x') #! Eje (x)
plt.ylabel('y') #! Eje (y)
plt.title('Corazoncito para mi noviecita') #! Titulo
plt.grid(True) #! Maya para controlar valores 
plt.show() #! Mostramos
