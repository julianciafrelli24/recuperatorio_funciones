def calcular_subtotal(precio, canti):
    subtotal = precio * canti
    return subtotal

def aplicar_descuento(subtotal):
    if subtotal >= 20000:
        subtotal = subtotal * 0.90
    return subtotal