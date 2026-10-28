import numpy as np
import matplotlib.pyplot as plt
# Arath Valenzuela NC:0148 (28/10/26)
no_lista = [1,2,3,17,48]
calificacion_ml = [20,30,80,100,90]
calificacion_va = [70,90,60,90,100]
plt.plot(no_lista, calificacion_ml, label="Calificaciones de Machine Learning")
plt.plot(no_lista, calificacion_va, label="Calificaciones de Vision Artificial")
plt.title("Calificaciones de las materias (NC:0148)")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")
plt.legend()
plt.show()

print("Hecho por Arath Valenzuela")
print("--------+NC:0148+---------")