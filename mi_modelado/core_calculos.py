def calcular_materiales(materiales_base, metros_cuadrados):
    return {mat: round(cant * metros_cuadrados,2) for mat, cant in materiales_base.items()}

def calcular_costos(materiales_finales, material_opciones, materiales_seleccionados):
    costos = {}
    calidades = {}
    rendimiento = {}
    for mat, cant in materiales_finales.items():
        tipo = materiales_seleccionados[mat]
        info = material_opciones[mat][tipo]
        costos[mat] = cant * info["precio"]
        calidades[mat] = info["calidad"]
        rendimiento[mat] = info["calidad"]/info["precio"]
    return costos, calidades, rendimiento
