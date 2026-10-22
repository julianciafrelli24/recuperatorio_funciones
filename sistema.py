import utils
totales = []

for i in range(3):
    print("Compra", i + 1)

    precio = float(input("Ingrese el precio: "))
    canti = int(input("Ingrese la cantidad del producto:"))

    subtotal = utils.calcular_subtotal(precio, canti)
    total = utils.aplicar_descuento(subtotal)

    totales.append(total)

print("Importe final:", totales)
print("La suma de sus compras es de: $",totales)
