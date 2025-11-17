from interfaces.input_handler import pedir_numero, pedir_entero
from data.materiales import materiales_base, material_opciones
from data.consejos import consejos_obra
from data.proveedores import proveedores
from core.calculos import calcular_materiales, calcular_costos
from core.tiempo import calcular_tiempo
from reports.graficas import plot_costos
import pandas as pd

print("Bienvenido al analisis EMA para tu obra 🏗️")

metros_cuadrados = pedir_numero("Ingresa los metros cuadrados de la obra: ")
tipo_obra = input("Tipo de obra (muro, piso, losa, cimentación, castillo, aplanado, techumbre, barda): ").lower()
trabajadores = pedir_entero("¿Cuántos trabajadores estarán en obra?: ")

# Selección de materiales
materiales = materiales_base.get(tipo_obra, {"cemento (kg)": 15, "arena (kg)": 25})
materiales_seleccionados = {}
for mat in materiales:
    opciones = list(material_opciones[mat].keys())
    print(f"\nMaterial {mat}:")
    for i, opc in enumerate(opciones, 1):
        print(f"{i}. {opc}")
    eleccion = pedir_entero("Elige número: ")
    materiales_seleccionados[mat] = opciones[eleccion - 1]

materiales_finales = calcular_materiales(materiales, metros_cuadrados)
costos_base, calidades, rendimiento_score = calcular_costos(materiales_finales, material_opciones, materiales_seleccionados)

costo_total = sum(costos_base.values())
calidad_promedio = round(sum(calidades.values())/len(calidades),2)

# Costos por proveedor
costos_proveedores = {prov: round(costo_total * factor,2) for prov, factor in proveedores.items()}
df_proveedores = pd.DataFrame({"Proveedor": list(costos_proveedores.keys()), "Costo total ($)": list(costos_proveedores.values())})
print("\n=================== COMPARATIVA DE PROVEEDORES ===================")
print(df_proveedores)

# Tiempo estimado
semanas, dias, meses = calcular_tiempo(len(materiales_finales), trabajadores)

# Tabla final
df = pd.DataFrame({
    "Material": list(materiales_finales.keys()),
    "Tipo": list(materiales_seleccionados.values()),
    "Cantidad total": list(materiales_finales.values()),
    "Costo ($)": [round(v,2) for v in costos_base.values()],
    "Calidad (1-10)": list(calidades.values()),
    "Rendimiento": [round(v,2) for v in rendimiento_score.values()]
})
print("\n=============== TABLA FINAL DE MATERIALES ===============")
print(df)

print(f"\nCosto total base: ${costo_total} MXN")
print(f"Tiempo estimado: {dias} días ({semanas} semanas | {meses} meses)")
print(f"Calidad promedio del proyecto: {calidad_promedio}/10")

# Gráfica de costos
plot_costos(df)

# Consejos
print("\n=================== CONSEJOS PARA TU OBRA ===================")
for c in consejos_obra.get(tipo_obra, ["Tipo de obra no reconocido, sin consejos específicos."]):
    print(f"- {c}")
