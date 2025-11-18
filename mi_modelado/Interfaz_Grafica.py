import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# =============================
# FUNCIONES AUXILIARES
# =============================
def cargar_icono(ruta, size=(28,28)):
    try:
        img = Image.open(ruta).convert("RGBA").resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return tk.PhotoImage(width=size[0], height=size[1])

def mostrar_dataframe_en_frame(frame, df):
    for widget in frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings', height=10)
    tree.pack(fill="both", expand=True, padx=5, pady=5)
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

def mostrar_graficas(frame, df, dias, semanas, meses, clima):
    for widget in frame.winfo_children():
        widget.destroy()

    fig, axs = plt.subplots(1,2, figsize=(10,4))

    # Grafica 1: costos por material
    colores_material = {
        "Cemento":"#ff7043",
        "Arena":"#42a5f5",
        "Grava":"#7e57c2",
        "Acero":"#26a69a",
        "Ladrillo":"#ef5350"
    }
    axs[0].bar(df["Material"], df["Costo ($)"], color=[colores_material[m] for m in df["Material"]])
    axs[0].set_title("Comparativa de precios por material")
    axs[0].set_ylabel("Costo ($)")
    axs[0].tick_params(axis='x', rotation=45)

    # Grafica 2: tiempo estimado
    colores_tiempo = {"sol":"#ffb74d","lluvia":"#64b5f6","frio":"#90a4ae","calor":"#f06292"}
    color = colores_tiempo.get(clima,"#81c784")
    axs[1].bar(["Días", "Semanas", "Meses"], [dias, semanas, meses], color=color)
    axs[1].set_title("Tiempo estimado del proyecto")

    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# =============================
# VENTANA PRINCIPAL
# =============================
root = tk.Tk()
root.title("Analizador EMA Dinámico 🏗️")
root.geometry("1350x950")
root.configure(bg="#e0f2f1")

# ICONO
icono_start = cargar_icono("start.png")

# TITULO
titulo = tk.Label(root, text="Bienvenido al Análisis EMA Dinámico 🏗️",
                  font=("Arial", 26, "bold"), fg="darkgreen", bg="#e0f2f1")
titulo.pack(pady=10)

# FRAME DE BOTONES DE SECCIONES
frame_botones = tk.Frame(root, bg="#e0f2f1")
frame_botones.pack(fill="x", padx=10, pady=5)

# =============================
# FRAMES POR SECCIÓN
# =============================
frames = {}
colores = {
    "Materiales":"#f57c00",
    "Proveedores":"#0288d1",
    "Consejos":"#7b1fa2",
    "Gráficas":"#2e7d32"
}

for sec in colores:
    f = tk.Frame(root, bg=colores[sec])
    frames[sec] = f
    f.pack(fill="both", expand=True)
    f.pack_forget()

active_button = None
def mostrar_frame(nombre):
    global active_button
    for f in frames.values():
        f.pack_forget()
    frames[nombre].pack(fill="both", expand=True)
    for btn in botones_secciones:
        btn.configure(relief="raised")
    active_button.configure(relief="sunken")

# Botones de navegación
botones_secciones = []
for sec in frames:
    btn = tk.Button(frame_botones, text=sec, bg=colores[sec], fg="white", font=("Arial",12,"bold"))
    btn.pack(side="left", padx=5)
    btn.configure(command=lambda s=sec, b=btn: [mostrar_frame(s), set_active(b)])
    botones_secciones.append(btn)

def set_active(btn):
    global active_button
    active_button = btn

# =============================
# FRAME DE ENTRADAS
# =============================
frame_entrada = tk.LabelFrame(root, text="Datos de la Obra", font=("Arial",16,"bold"),
                              fg="white", bg="#00695c", padx=10, pady=10)
frame_entrada.pack(fill="x", padx=10, pady=10)

tk.Label(frame_entrada, text="Metros cuadrados:", bg="#00695c", fg="white", font=("Arial",12)).grid(row=0, column=0, sticky="w")
metros_cuadrados_entry = tk.Entry(frame_entrada)
metros_cuadrados_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(frame_entrada, text="Tipo de obra (residencial/comercial/industrial):", bg="#00695c", fg="white", font=("Arial",12)).grid(row=1, column=0, sticky="w")
tipo_obra_entry = tk.Entry(frame_entrada)
tipo_obra_entry.grid(row=1, column=1, pady=5, padx=5)

tk.Label(frame_entrada, text="Trabajadores:", bg="#00695c", fg="white", font=("Arial",12)).grid(row=2, column=0, sticky="w")
trabajadores_entry = tk.Entry(frame_entrada)
trabajadores_entry.grid(row=2, column=1, pady=5, padx=5)

tk.Label(frame_entrada, text="Clima (sol/lluvia/frio/calor):", bg="#00695c", fg="white", font=("Arial",12)).grid(row=3, column=0, sticky="w")
clima_entry = tk.Entry(frame_entrada)
clima_entry.grid(row=3, column=1, pady=5, padx=5)

# =============================
# FUNCION CALCULO COMPLETA DINAMICA
# =============================
def calcular():
    metros_cuadrados = float(metros_cuadrados_entry.get())
    tipo_obra = tipo_obra_entry.get().lower()
    trabajadores = int(trabajadores_entry.get())
    clima = clima_entry.get().lower()

    # Comparativa de materiales (valores dinámicos)
    materiales_base = {
        "Cemento": {"unidad":"kg", "costo_unit":10},
        "Arena": {"unidad":"m3", "costo_unit":5},
        "Grava": {"unidad":"m3", "costo_unit":8},
        "Acero": {"unidad":"kg", "costo_unit":15},
        "Ladrillo": {"unidad":"pieza", "costo_unit":12}
    }

    df_materiales = pd.DataFrame(columns=["Material","Unidad","Cantidad total","Proveedor recomendado","Costo ($)","Cantidad diaria estimada"])

    for mat, info in materiales_base.items():
        cantidad_total = round(metros_cuadrados * (1 + len(mat)*0.1),2)
        costo_total = round(cantidad_total * info["costo_unit"],2)
        cantidad_diaria = max(1, round(trabajadores * 0.5 * (1 if tipo_obra!="comercial" else 1.5),2))
        proveedor = "Proveedor "+mat
        df_materiales = pd.concat([df_materiales, pd.DataFrame([[
            mat, info["unidad"], cantidad_total, proveedor, costo_total, cantidad_diaria
        ]], columns=df_materiales.columns)], ignore_index=True)

    # Proveedores
    df_proveedores = pd.DataFrame({
        "Proveedor": ["Cemex","Home Depot","Construrama"],
        "Costo total ($)": [df_materiales["Costo ($)"].sum(),
                            df_materiales["Costo ($)"].sum()*1.1,
                            df_materiales["Costo ($)"].sum()*0.95],
        "Tiempo entrega (días)": [max(1,metros_cuadrados/50), max(2,metros_cuadrados/40), max(1,metros_cuadrados/60)],
        "Comentarios": ["Entrega rápida","Precios un poco altos","Recomendado para grandes obras"]
    })

    # Consejos adaptativos
    consejos = [
        "Revisa estructura antes de iniciar",
        "Mantén los materiales protegidos de la humedad",
        "Usa niveles y herramientas calibradas",
        "Aplica correctamente normas de seguridad",
        "Planifica el cronograma por fases",
        "Capacita a los trabajadores en medidas de seguridad"
    ]

    for mat in df_materiales["Material"]:
        cantidad = df_materiales.loc[df_materiales['Material']==mat,'Cantidad total'].values[0]
        if mat.lower() == "cemento":
            consejos.append(f"Cemento: {cantidad} kg, evita mezclar con exceso de agua")
        elif mat.lower() == "arena":
            consejos.append(f"Arena: {cantidad} m3, asegúrate que esté limpia")
        elif mat.lower() == "grava":
            consejos.append(f"Grava: {cantidad} m3, tamaño adecuado")
        elif mat.lower() == "acero":
            consejos.append(f"Acero: {cantidad} kg, protege de oxidación")
        elif mat.lower() == "ladrillo":
            consejos.append(f"Ladrillo: {cantidad} piezas, evita lluvia antes de colocarlos")

    # Consejos por clima
    clima_dict = {
        "lluvia":"protege materiales y evita trabajar en exteriores durante lluvias fuertes",
        "sol":"hidrata al personal y protege materiales del calor",
        "frio":"evita que el agua de mezcla se congele y protege a los trabajadores",
        "calor":"realiza trabajos en horarios frescos y mantén sombra para el personal"
    }
    if clima in clima_dict:
        consejos.append("Clima: "+clima_dict[clima])

    # Consejos según tipo de obra
    tipo_dict = {
        "residencial":"verifica normativas locales y espacio limitado",
        "comercial":"prioriza planificación de logística y seguridad",
        "industrial":"refuerza control de materiales pesados y seguridad"
    }
    if tipo_obra in tipo_dict:
        consejos.append("Tipo de obra: "+tipo_dict[tipo_obra])

    # Tiempo estimado dinámico
    dias = round(metros_cuadrados/2 + len(tipo_obra)*3,2)
    semanas = round(dias/7,2)
    meses = round(semanas/4,2)

    # Mostrar resultados dinámicos
    mostrar_dataframe_en_frame(frames["Materiales"], df_materiales)
    mostrar_dataframe_en_frame(frames["Proveedores"], df_proveedores)

    for widget in frames["Consejos"].winfo_children():
        widget.destroy()
    tk.Label(frames["Consejos"], text="\n".join(consejos), font=("Arial",12), fg="white",
             bg=colores["Consejos"], justify="left").pack(anchor="w", padx=10, pady=5)

    mostrar_graficas(frames["Gráficas"], df_materiales, dias, semanas, meses, clima)
    mostrar_frame("Materiales")

# =============================
# BOTON CALCULAR
# =============================
btn_calcular = tk.Button(frame_entrada, text="Calcular 🏗️", bg="#388e3c", fg="white",
                         font=("Arial",12,"bold"), command=calcular, image=icono_start, compound="left")
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)
active_button = botones_secciones[0]

root.mainloop()