# Practica-6 Acreditacion por Ema



## 🧠 ¿Qué hace este proyecto?

Este asistente te ayuda a elegir el *material óptimo* para una obra según:

- Resistencia  
- Durabilidad  
- Costo  
- Impacto ambiental  
- Tipo de obra  

Basado en criterios técnicos educativos, resaltando la importancia de ensayos realizados en *laboratorios acreditados por EMA*.

---

## 🚀 Características

✔ CLI (línea de comandos)  
✔ GUI con Tkinter  
✔ API Web con Flask  
✔ Recomendación técnica + cantidades  
✔ Reporte detallado  
✔ Pruebas automatizadas con pytest  
✔ Código modular y limpio  

---

---

### 📌 **Descripción detallada del propósito de cada componente**

#### 🟦 **Carpeta `/src/`**
Contiene toda la lógica interna del asistente, organizada para respetar principios de diseño limpio (Clean Code y Clean Architecture a nivel básico).

- **`materiales.py`**  
  Define la "base de datos" interna con las propiedades técnicas de cada material.  
  Es el archivo que más modificarás si deseas agregar nuevos materiales.

- **`reglas.py`**  
  Contiene los pesos o prioridades según el tipo de obra (cimentación, muro, techo, etc.).  
  Estas reglas determinan cómo se calculan los puntajes de cada material.

- **`calculos.py`**  
  Aquí vive la inteligencia del sistema:  
  - Evalúa los materiales  
  - Calcula el mejor según el tipo de obra  
  - Determina cantidades aproximadas  
  Es el motor del asistente.

- **`reporte.py`**  
  Toma los resultados y los transforma en un reporte amigable, didáctico y fácil de leer.  
  Ideal para usuarios finales, estudiantes o personal técnico.

---

### 🟩 **Archivos fuera de `/src/`**

#### **`main.py`**  
Entrada principal para usar el asistente por consola (CLI).  
Este archivo mantiene el proyecto universal: siempre funcionará, sin necesidad de GUI o web.

#### **`gui.py`**  
Interfaz gráfica con Tkinter.  
Pensada para usuarios que prefieren algo visual y sencillo, sin escribir comandos.

#### **`app.py`**  
Servidor web básico usando Flask.  
Permite usar el asistente en navegador o integrarlo en otros sistemas mediante HTTP.

---

### 🧪 **Carpeta `/tests/`**
Incluye pruebas automatizadas escritas con pytest.  
Esto garantiza que:

- Las funciones principales funcionan correctamente  
- La lógica del proyecto no se rompa al hacer cambios  
- El proyecto es más profesional y estable  

---

