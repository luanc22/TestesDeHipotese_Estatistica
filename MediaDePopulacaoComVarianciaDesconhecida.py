import math
import scipy.stats as st

def calculaHipoteseDesc(xbarra, media, desvio, numero, indice, bilateral, lado):
  t = tCalc(xbarra, media, desvio, numero)
  if (bilateral == True):
    z1 = st.t.ppf(1-(indice/100)/2,numero-1)
    z2 = -z1
    print("t = {}".format(t))
    if(t < z1 or t > z2):     
      print("{} > {}".format(t, z2))
      return "tCalc pertence a RNR e não rejeitamos H0."
    else:
      return "tCalc pertence a RC e rejeitamos H0."
  else:
    z1 = st.t.ppf(1-(indice/100),numero-1)
    print("t = {}".format(t))
    if(lado == False):
      z1 = -z1;
      if(t < z1 and lado == False):
        print("{} < {}".format(t, z1))
        return "zCalc pertence RC a esquerda e rejeitamos H0."
      else:
        print("{} > {}".format(t, z1))
        return "tCalc pertence a RNR com RC a esquerda e não rejeitamos H0."
    if(lado == True):
      if(t > z1 and lado == True):
        print("{} > {}".format(t, z1))
        return "tCalc pertence a RC a direita e rejeitamos H0."
      else:
        print("{} < {}".format(t, z1))
        return "tCalc pertence a RNR com RC a direita e não rejeitamos H0."
  

def tCalc(xbarra, media, desvio, numero):
  return (xbarra-media)/(math.sqrt((desvio*desvio)/numero))

def calculaVariancia(numero, somatoria, somatoriaquadrado):
  s = math.sqrt((1/(numero-1))*(somatoriaquadrado - ((somatoria*somatoria)/numero)))
  return s

def calculaSomatoria(valor):
  somatoria = 0
  i = 0
  while(i < len(valor)):
    somatoria = somatoria + valor
    i = i + 1
  print("somatoria = {}".format(somatoria))
  return somatoria

def calculaSomatoriaQuadrado(valor):
  somatoria = 0
  i = 0
  while(i < len(valor)):
    somatoria = somatoria + (valor*valor)
    i = i + 1
  print("somatoria = {}".format(somatoria))
  return somatoria

# Bilateral
print(calculaHipoteseDesc(1070, 1120, 125, 8, 0.5, True, False))

# Unilateral a esquerda
desvio = calculaVariancia(25, 950, 36106)
xbarra = 950/25
print(calculaHipoteseDesc(xbarra, 40, desvio, 25, 5, False, False))

#Unilateral a direita
print(calculaHipoteseDesc(1.004, 1, 0.003, 10, 10, False, True))