#!/usr/bin/python

# GENERATOR PASSWD project by kaleth
# Ultima modificacion 08 de Marzo de 2025
# Script Modificado por (K4ledcb@gmail.com) 

import sys, math
from time import time, localtime, strftime

########################### CONFIGURACION #########################

LONGITUD = 4
ALFABETO = "abcdefghijklmnopqrstuvwxyz0123456789_-."

####################################################################

########################## FUNCIONES ###############################
def getVariacionesConRepeticion(ALFABETO , LONGITUD):
  sumatorio = 0
  for i in range(LONGITUD):
    producto = 1
    for j in range(i+1):
      producto = producto * len(ALFABETO)
    sumatorio = sumatorio + producto
  return sumatorio

def eventoPalabraGenerada(palabra):
  print palabra

####################################################################

##################### VARS AUXILIARES ##############################
DEBUG = True
VERBOSE = True
variacionesConRepeticion = getVariacionesConRepeticion(ALFABETO , LONGITUD)
inicioReloj = time()
cont = 0
progreso = 0
####################################################################

while LONGITUD > 0:
  try:
    contadores = []                                                                                                                                                                      
    for i in range(LONGITUD):
      contadores.append(0)

    fin = False
    while not fin:
      if DEBUG == True:
        palabra=[]														                                              
        for i in range(LONGITUD):
          palabra.append(ALFABETO[contadores[i]])						
 eventoPalabraGenerada("".join(palabra))							

      if VERBOSE == True:
        if (cont % 600000 == 0) and (cont != 0):
            progreso = cont*100.0/variacionesConRepeticion              
              progreso = round(progreso , 2)
                finReloj = time() - inicioReloj                             
   velocidad = cont / finReloj                                   
          velocidad = round(velocidad , 2)
            estimado = finReloj * variacionesConRepeticion / cont         
              restante = estimado - finReloj                                
   restante = restante / 60 / 60                                
            restante = round(restante , 2)
             sys.stderr.write(str(progreso)+"% - Quedan "+str(restante)+" horas. La velocidad es de "+str(velocidad)+" palabras/seg\n")

      cont = cont + 1
  actual = LONGITUD - 1                                             
      contadores[actual] = contadores[actual] + 1                      

      while(contadores[actual] == len(ALFABETO)) and not fin:          
        if(actual == 0):
          fin = True                                                  
        else:
           contadores[actual] = 0                                      
              actual = actual - 1
      contadores[actual] = contadores[actual] + 1                  

    LONGITUD = LONGITUD - 1                                            

  except KeyboardInterrupt:
    sys.stderr.write("Interrumpido por el usuario\n")
    fin = True                                                         
    LONGITUD = 0

if VERBOSE == True:
  sys.stderr.write("Terminado al "+str(progreso)+"% - Realizadas "+str(cont)+" combinaciones de "+str(variacionesConRepeticion)+"\n")


