import math
import scipy.stats as st

def calculaVarianciaPopulacao(somatoria, variancia, indice, numero, desvio, temMedia, lado):
  if(temMedia == True):
    x = xCalcComMedia(somatoria, variancia)
  else:
    x = xCalcSemMedia(numero, desvio, variancia)
  print("x = {}".format(x))
  if(lado == False):
    x1 = st.chi2.ppf(1-indice/100, numero)
    if(x > x1):
        print("{} > {}".format(x, x1))
        return "xCalc pertence a RNR e rejeitamos H0."
    else:
        return "xCalc pertence a RC a esquerda e não rejeitamos H0."
  if(lado == True):
    x1 = st.chi2.ppf(1-indice/100, numero-1)
    if(x < x1):
      print("{} < {}".format(x, x1))
      return "xCalc pertence a RNR e não rejeitamos H0."
    else:
        return "xCalc pertence a RC a direita e rejeitamos H0."

def xCalcComMedia(somatoria, variancia):
  x = somatoria/variancia
  return x

def xCalcSemMedia(numero, desvio, variancia):
  x = (numero-1)*(desvio*desvio)/(variancia*variancia)
  return x

#Unilateral a esquerda
print(calculaVarianciaPopulacao(129000, 3600, 95, 26, 0, True, False))

#Unilateral a direita
print(calculaVarianciaPopulacao(0, 240, 5, 8, 300, False, True))