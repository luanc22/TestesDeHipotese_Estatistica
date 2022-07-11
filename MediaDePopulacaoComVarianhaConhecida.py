# Código Padrão
import math
import scipy.stats as st

def calculaHipotese(xbarra, media, variancia, numero, indice, bilateral, lado):
  z = zCalc(xbarra, media, variancia, numero)
  if (bilateral == True):
    z1 = st.norm.ppf(1-(indice/100)/2)
    z2 = -z1
    print("z = {}".format(z))
    if(z > z2 or z < z1):     
      print("{} < {} < {}".format(z2, z, z1))
      return "zCalc pertence a RNR e não rejeitamos H0."
    else:
      print("{} > {} > {}".format(z2, z, z1))
      return "zCalc pertence a RC e rejeitamos H0."
  else:
    z1 = st.norm.ppf(1-(indice/100)) 
    print("z = {}".format(z))
    if(lado == False):
      z1 = -z1;
      if(z > z1 ):
        print("{} > {}".format(z, z1))
        return "zCalc pertence a RNR com RC a esquerda e não rejeitamos H0."
      else:
        print("{} < {}".format(z, z1))
        return "zCalc pertence a RNR com RC a esquerda e rejeitamos H0."
    if(lado == True):
      if(z > z1 and lado == True):
        print("{} > {}".format(z, z1))
        return "zCalc pertence RC a direita e rejeitamos H0."
      else:
        print("{} < {}".format(z, z1))
        return "zCalc pertence a RNR com RC a direita e não rejeitamos H0."



def zCalc(xbarra, media, variancia, numero):
  return (xbarra-media)/(math.sqrt(variancia/numero))

# Bilateral
print(calculaHipotese(43, 45, 36, 16, 10, True, False))

# Unilateral a esquerda
print(calculaHipotese(25.3, 26, 5.86, 10, 5, False, False))

#Unilateral a direita
print(calculaHipotese(210, 206, 144, 30, 10, False, True))