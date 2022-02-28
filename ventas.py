from collections import namedtuple
import datetime


Detalle = namedtuple("servicio",("folio", "fecha", "nombrecliente", "monto")) #En esta parte del codigo te pide los datos del cliente 
lista_detalle = list()


cliente = input("Cliente al que se le realizó el servicio: ") 
while True:
    try:
        fecha_str = input("Fecha del servicio en formato (dd/mm/aaaa): ") #En esta parte te da la otra fecha del servicio
        fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
    except ValueError:
        print("El valor de la fecha que fue proporcionado no puede ser procesado")
        continue
     except Exception:
        print("Se ha presentado una excepción")
        break
    else 
    monto = float(input("Indique el monto para este servicio: ")) #aqui se indica el monto para el servicio
                detalle = Detalle(clave, monto)
                lista_detalle.append(detalle)
                else
                print(f"\nEl monto del servicio antes de impuestos es de ${monto}")
            print("El listado de la venta es: ")
            print(f"\nVenta realizada a {cliente} con fecha de {fecha}")
            print("-" * 55)
            print("Clave del artículo\tmonto")
            for detalle in lista_detalle:
                print(f"{detalle.clave_articulo}\t\t\t\t\t${detalle.precio_monto}")
            print("-" * 55)

        sumtotal = df_lista_detalle _["total"].sum() #En esta parte se realiza lo que viene siendo el iva 
        iva = sumtotal * .16
        totaliva = sumtotal + iva
        print(SEPARADOR)
        print(f"Total : ${sumtotal}")
        print(f"Total + IVA : ${totaliva}")
