# 🎮 Halo Equation Plotter

Graficador de ecuaciones matemáticas 2D y 3D con interfaz Tkinter y tema Halo.

## 📋 Características

- ✅ **Gráficas 2D**: Funciones y ecuaciones implícitas
- ✅ **Gráficas 3D**: Superficies y ecuaciones implícitas
- ✅ **Ecuaciones predefinidas**: Círculos, parábolas, esferas, etc.
- ✅ **Entrada personalizada**: Escribe tus propias ecuaciones
- ✅ **Controles interactivos**: Zoom, rotación, pan
- ✅ **Tema Halo**: Colores icónicos del universo Halo

## 🚀 Instalación

### Instalar dependencias:

```bash
pip install numpy matplotlib scikit-image
```

### Ejecutar:

```bash
python3 plotter.py
```

## 🎯 Cómo Usar

### Modo 2D

**Funciones explícitas** (y = f(x)):

```
y = x**2
y = np.sin(x)
y = x**3 - 2*x
```

**Ecuaciones implícitas** (relaciones entre x e y):

```
x**2 + y**2 = 25         # Círculo
x**2/4 + y**2/9 = 1      # Elipse
x**2 - y**2 = 1          # Hipérbola
```

### Modo 3D

**Funciones explícitas** (z = f(x,y)):

```
z = x**2 + y**2          # Paraboloide
z = np.sin(x) * np.cos(y)
z = x**2 - y**2          # Silla de montar
```

**Ecuaciones implícitas** (relaciones entre x, y, z):

```
x**2 + y**2 + z**2 = 25  # Esfera
x**2 + y**2 = z**2       # Cono
x**2 + y**2 - z**2 = 1   # Hiperboloide
```

## 📚 Ecuaciones Predefinidas

### 2D

- Parábola: `y = x²`
- Círculo: `x² + y² = 25`
- Hipérbola: `x² - y² = 1`
- Seno: `y = sin(x)`
- Coseno: `y = cos(x)`
- Elipse: `x²/4 + y²/9 = 1`

### 3D

- Esfera: `x² + y² + z² = 25`
- Paraboloide: `z = x² + y²`
- Cono: `x² + y² = z²`
- Hiperboloide: `x² + y² - z² = 1`
- Plano: `z = 2x + 3y`
- Silla: `z = x² - y²`

## ⌨️ Operadores Soportados

| Operador    | Descripción       | Ejemplo      |
| ----------- | ----------------- | ------------ |
| `+`         | Suma              | `x + 2`      |
| `-`         | Resta             | `x - 3`      |
| `*`         | Multiplicación    | `2 * x`      |
| `/`         | División          | `x / 2`      |
| `**`        | Potencia          | `x**2` (x²)  |
| `np.sin()`  | Seno              | `np.sin(x)`  |
| `np.cos()`  | Coseno            | `np.cos(x)`  |
| `np.sqrt()` | Raíz cuadrada     | `np.sqrt(x)` |
| `np.exp()`  | Exponencial       | `np.exp(x)`  |
| `np.log()`  | Logaritmo natural | `np.log(x)`  |

## 🎨 Controles de la Interfaz

### Panel Izquierdo (Controles)

- **Modo**: Selecciona entre gráficas 2D o 3D
- **Ecuaciones predefinidas**: Click para cargar ejemplos
- **Ecuación personalizada**: Ingresa tu propia ecuación
- **Rango**: Define los límites min/max de graficación
- **GRAFICAR**: Genera la gráfica
- **LIMPIAR**: Borra la gráfica actual

### Panel Derecho (Visualización)

- **Zoom**: Usa la rueda del mouse o los botones de zoom
- **Pan**: Click y arrastra para mover
- **Rotación 3D**: Click y arrastra para rotar (solo en 3D)
- **Reset**: Botón home para volver a la vista original

## 💡 Ejemplos de Uso

### Ejemplo 1: Círculo

```
1. Selecciona modo: 2D
2. Ecuación: x**2 + y**2 = 25
3. Rango: -10 a 10
4. Click GRAFICAR
```

### Ejemplo 2: Esfera

```
1. Selecciona modo: 3D
2. Ecuación: x**2 + y**2 + z**2 = 25
3. Rango: -10 a 10
4. Click GRAFICAR
```

### Ejemplo 3: Paraboloide

```
1. Selecciona modo: 3D
2. Ecuación: z = x**2 + y**2
3. Rango: -5 a 5
4. Click GRAFICAR
```

### Ejemplo 4: Función Trigonométrica

```
1. Selecciona modo: 2D
2. Ecuación: y = np.sin(x)
3. Rango: -10 a 10
4. Click GRAFICAR
```

## 🔧 Personalización

### Modificar colores

Edita las constantes de color en `plotter.py`:

```python
HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_RED = "#ff1744"
HALO_GOLD = "#ffd700"
HALO_DARK = "#0a0e1a"
HALO_GRAY = "#2d3436"
```

### Agregar ecuaciones predefinidas

Añade nuevas ecuaciones a los diccionarios:

```python
self.presets_2d = {
    "Tu ecuación": "y = x**3",
    # ... más ecuaciones
}
```

## ⚠️ Notas Importantes

1. **Sintaxis**: Usa `**` para potencias, no `^`

   - ✅ Correcto: `x**2`
   - ❌ Incorrecto: `x^2`

2. **Funciones NumPy**: Usa el prefijo `np.`

   - ✅ Correcto: `np.sin(x)`
   - ❌ Incorrecto: `sin(x)`

3. **Ecuaciones implícitas 3D**: Requieren scikit-image

   - Si no está instalado, algunas gráficas 3D pueden fallar

4. **Rango**: Ajusta el rango según la ecuación
   - Para funciones que crecen rápido, usa rangos pequeños

## 🐛 Solución de Problemas

### Error: "No module named 'matplotlib'"

```bash
pip install matplotlib
```

### Error: "No module named 'skimage'"

```bash
pip install scikit-image
```

### La gráfica no se ve completa

- Ajusta el rango (min/max)
- Verifica la sintaxis de la ecuación

### Error de sintaxis

- Usa `**` para potencias
- Agrega `np.` antes de funciones matemáticas
- Verifica paréntesis balanceados

## 🎮 Tema Halo

Este graficador usa los colores icónicos del universo Halo:

- **Azul** (#00a8ff) - Escudos de energía
- **Verde** (#76ff03) - Salud y sistemas activos
- **Rojo** (#ff1744) - Alertas y peligro
- **Dorado** (#ffd700) - Títulos y destacados
- **Oscuro** (#0a0e1a) - Fondo principal

## 📖 Recursos Adicionales

- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Sintaxis de ecuaciones matemáticas](https://docs.python.org/3/library/math.html)

## 🎯 Proyectos Futuros

- [ ] Soporte para ecuaciones paramétricas
- [ ] Más funciones matemáticas (tan, log, etc.)
- [ ] Exportar gráficas como imágenes
- [ ] Animaciones de ecuaciones
- [ ] Múltiples ecuaciones en una gráfica

---

**Finish the fight!** 🎮 Disfruta graficando ecuaciones matemáticas!
