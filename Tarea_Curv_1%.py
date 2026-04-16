'''
Tarea Curv Tonxley
Aqui planeo como hacer la curv tonxley
Fecha: 2024-04-10
Autor: Victor Perez
''' 

#* Primero cargo los datos y calculo ton indidual en cada columna
import pandas as pd
df = pd.read_csv("data.txt", sep ="\t") # Aqui cargue los datos del modelo de bloques separados por el tabulador en un txt por medio de pandas
# Considero densidad de 2.7 ton/m3 y un bloque de 10x10x10 m3
df['Volumen*Densidad'] = 10*10*10*2.7 # Calculo el tonelaje individual de cada bloque multiplicando el volumen por la densidad obteniendo tons
b= 10*10*10*2.7
Gc = 1
#* Defino un rango de leyes
Gc_min= 0
d = Gc/20
#* Calcular los bloques que estan por encima de cda ley de corte y ley media
df['ley*ton'] = df['ley'] * df['Volumen*Densidad'] # Agregue una nueva columna que calcula ley * ton
i = 0
datos= [] # Una lista para crear un ndf
while i < 20:
   mineral = df[df['ley'] >= Gc_min] # actualizo el dataframe para que solo me deje los bloques que estan por encima de la ley de corte minima
   l = len(mineral) # cuento el numero de bloques que estan por encima de la ley de corte minima
   k = 0
   if l > 0:
     k = mineral['ley*ton'].sum() # sumo la ley*ton de los bloques que estan por encima de la ley de corte minima
     #* Nuevo data frame
     dic = {
        'Ley_Corte': Gc_min,
        'Tonelaje': l*b,
        'Ley_media': k/(l*b),
        }
   else:
        dic = {
            'Ley_Corte': Gc_min,
            'Tonelaje': 0,
            'Ley_media': 0,
            } 
   datos.append(dic)
   i = i + 1
   Gc_min = Gc_min + d

   #* Nuevo data frame
ndf = pd.DataFrame(datos)
print(ndf)

#* Plotear 
import matplotlib.pyplot as plt
plt.plot(ndf['Ley_Corte'], ndf['Tonelaje'])
plt.xlabel('Ley de Corte (%)')
plt.ylabel('Tonelaje (tons)')
plt1 = plt.twinx()
plt1.plot(ndf['Ley_Corte'], ndf['Ley_media'], color = 'red')
plt1.set_ylabel('Ley media (%)', color = 'red')
plt.title('Tonelaje vs Ley')
plt.grid()
plt.show()
print('Curva Tonxley Ploteada')