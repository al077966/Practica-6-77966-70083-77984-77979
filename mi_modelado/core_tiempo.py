def calcular_tiempo(materiales_count, trabajadores):
    base = materiales_count * 0.6
    factor = max(0.20, 1 - trabajadores * 0.12)
    semanas = base * factor
    return round(semanas,2), round(semanas*7), round(semanas/4,2)
