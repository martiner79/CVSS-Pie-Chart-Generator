import matplotlib.pyplot as plt
import numpy as np

def generar_grafico_cvss():
    # Categorías CVSS y colores
    categorias = ['Critical', 'High', 'Medium', 'Low', 'Info']
    colores = ['#800000', '#FF0000', '#FFA500', '#008000', '#0000FF']  # Bordó, rojo, naranja, verde, azul

    # Solicitar la cantidad de vulnerabilidades
    print("Enter the number of vulnerabilities found for each category:")
    cantidades = []
    for n in categorias:
        while True:
            try:
                cantidad = int(input(f"{n}: "))
                if cantidad < 0:
                    raise ValueError("The number must be greater than or equal to 0.")
                cantidades.append(cantidad)
                break
            except ValueError as e:
                print(f"Invalid entry: {e}")

    # Calcular porcentajes
    total = sum(cantidades)
    if total == 0:
        print("No vulnerabilities were entered.")
        return

    porcentajes = [(cantidad / total) * 100 if total > 0 else 0 for cantidad in cantidades]

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Crear un degradado que cubra toda la figura
    x = np.linspace(0, 1, 500)
    y = np.linspace(0, 1, 500)
    X, Y = np.meshgrid(x, y)
    gradiente = np.sqrt(X**2 + Y**2)
    
    # Dibujar el degradado azul detrás del gráfico
    ax_background = fig.add_axes([0, 0, 1, 1], zorder=-1)
    ax_background.imshow(
        gradiente,
        extent=[-1, 1, -1, 1],
        cmap='Blues',
        aspect='auto',
        alpha=0.5
    )
    ax_background.axis('off')

    # Crear gráfico de torta
    wedges, texts, autotexts = ax.pie(
        cantidades,
        labels=[categoria if cantidad > 0 else '' for categoria, cantidad in zip(categorias, cantidades)],
        colors=colores,
        autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else '',
        startangle=90,
        textprops=dict(color="black", fontsize=10)
    )

    # Añadir cantidad dentro del gráfico, solo si la categoría tiene datos
    for i, autotext in enumerate(autotexts):
        if cantidades[i] > 0:
            autotext.set_text(f"{cantidades[i]}")
            autotext.set_color("white")
            autotext.set_fontweight("bold")
            autotext.set_fontsize(15)
        else:
            autotext.set_text('')

    # Añadir leyenda
    ax.legend(
        wedges, 
        [f"{categoria}: {cantidad} ({porcentaje:.1f}%)" for categoria, cantidad, porcentaje in zip(categorias, cantidades, porcentajes)],
        #title= Aquí puedes agregar un título como "Vulnerabilities Found" en el cuadro,
        loc="upper left",
        bbox_to_anchor=(1.08, 0.8)
    )

    # Título
    ax.set_title("CVSS Classification Of Vulnerabilities Found", fontsize=14, weight='bold')

    # Ajustar aspecto
    ax.set_aspect('equal')

    # Mostrar gráfico
    plt.tight_layout()
    plt.show()

# Llamar a la función
generar_grafico_cvss()

