'''                      VECTORES Y MATRICES

NUMPY ES UNA BIBLIOTECA DE PYTHON QUE PROVEE HERRAMIENTAS CON ARREGLOS MELTIDIMENSIONALES COMO VECTORES Y MATRICES.
Se usa import para importar la libreria, usar 'import math as m' lo que hace es importar math y ademas abreviarla
como m.

Una matris en python no es mas que una matris anidada o una lista con listas. para llamar los valores de aquella lista
se llama como list[0][0].

'''
import numpy as np
import matplotlib.pyplot as plt


# SINGLE POINT

'''ax = plt.axes(projection="3d")
ax.scatter(3, 5 , 7)
plt.show() MUESTRA UN PUNTO DENTRO DE UN PLANO 3D'''

# SCATTER PLOTS
'''ax = plt.axes(projection="3d")
x_data = numpy.random.randint(0, 100, (500,))
y_data = numpy.random.randint(0, 100, (500,))
z_data = numpy.random.randint(0, 100, (500,))
ax.scatter(x_data, y_data, z_data)
plt.show() CREA MUCHOS PUNTOS ALEATORIOS'''

# Grafica de lineas

''' ax = plt.axes(projection="3d")
x_data = numpy.arange(0, 50, 0.1)
y_data = numpy.arange(0, 50, 0.1)
z_data = numpy.tan(x_data) * numpy.sqrt(y_data)
ax.plot(x_data, y_data, z_data)
plt.show() '''

# GRAFICA 3D

ax = plt.axes(projection="3d")
x_data = np.arange(-3, 3, 0.1) # RANGO MAPA DE X
y_data = np.arange(-3, 3, 0.1) # RANGO MAPA DE Y
X, Y = np.meshgrid(x_data, y_data) # NO SÉ
Z = np.sqrt(X) * np.tan(Y) # FORMA DE LA GRAFICA
ax.plot_surface(X, Y, Z, cmap="plasma")
ax.view_init(azim=0, elev=90) # ELEVACION
plt.show() # GRAFICAR 3D MIO

# GRAFICA 3D JUANFE

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# X = np.arange(-5, 5, 1.5)
# Y = np.arange(-5, 5, 1.5)
# X, Y = np.meshgrid(X, Y)
# R = np.sin(X**5 + Y**2)
# Z = np.sin(R)

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
# plt.show() 