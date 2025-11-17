import matplotlib.pyplot as plt

def plot_costos(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["Material"], df["Costo ($)"], marker='o', linewidth=3, color="red")
    plt.title("Comparativa de precios entre materiales")
    plt.xlabel("Material")
    plt.ylabel("Costo total ($)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
