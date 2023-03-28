opcion = int(input("""
1 - Convertir pesos argentinos a dolares.
2 - Convertir euros a dolares.
3 - convertir libras a dolares.
"""))
if opcion == 1:
  pesos = input('Cuantos pesos argentinos quieres convertir?: ')
  pesos = float(pesos)
  valor_dolar = 295
  dolar = pesos / valor_dolar
  dolar = round(dolar, 2)
  print(f'{pesos} pesos argentinos a dolares son: ${dolar}')

elif opcion == 2:
  euros = input('Cuantos euros quieres convertir?: ')
  euros = float(euros)
  valor_dolar1 = 1.0042
  valor_euro = euros / valor_dolar1
  valor_euro = round(valor_euro, 2)
  print(f'{euros} euros a dolares son: ${valor_euro}')
elif opcion == 3:
  libras = input('Cuantas libras quieres convertir?: ')
  libras = float(libras)
  valor_dolar2 = 0.845
  valor_libra = libras / valor_dolar2
  valor_libra = round(valor_libra, 2)
  print(f'{libras} libras a dolares son: ${valor_libra}')
else:
  print('Eliga una opcion correcta!')