# 🧮 Métodos Numéricos en Python

Implementación de métodos numéricos clásicos para **derivación** e **integración** de funciones matemáticas. Incluye tanto aproximación numérica mediante diferencia centrada como integración por la Regla de Simpson con estimación de error.

---

## 📁 Archivos

| Archivo | Descripción |
|---|---|
| `metodos_numericos.py` | Diferencia centrada + Regla de Simpson |
| `derivada_exacta.py` | Derivada simbólica exacta con SymPy |

---

## ⚙️ Requisitos

```bash
pip install sympy
```

> La librería estándar de Python (`math`) no requiere instalación adicional.

---

## 📌 Función 1 — Derivada por Diferencia Centrada

### Propósito

Calcula la derivada numérica de una función usando la fórmula de **diferencia centrada**:

$$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$

### Parámetros

| Parámetro | Tipo | Descripción |
|---|---|---|
| `f` | `callable` | Función a derivar |
| `x` | `float` | Punto en el que se evalúa la derivada |
| `h` | `float` | Tamaño de paso (debe ser > 0) |

### Retorna

`float` — valor aproximado de f′(x) en el punto x.

### Uso

```python
import math
from metodos_numericos import derivada_diferencia_centrada

# f(x) = sin(x), f'(π/4) = cos(π/4) ≈ 0.70711
resultado = derivada_diferencia_centrada(math.sin, math.pi / 4, 1e-5)
print(resultado)  # 0.7071067811865476

# f(x) = x³, f'(2) = 12
resultado = derivada_diferencia_centrada(lambda x: x**3, 2.0, 1e-5)
print(resultado)  # 12.000000000132154
```

---

## 📌 Función 2 — Integral por Regla de Simpson

### Propósito

Calcula la integral definida de una función en el intervalo [a, b] usando la **Regla de Simpson compuesta**, y estima la cota de error de truncamiento.

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + \cdots + 4f(x_{n-1}) + f(x_n)\right]$$

donde $h = \dfrac{b - a}{n}$

### Cota de error

$$E_T \leq \frac{(b-a)^3}{12n^2} \max_{a \leq x \leq b} |f''(x)|$$

El máximo de |f″(x)| se estima numéricamente sobre una malla interna de 1000 puntos.

### Parámetros

| Parámetro | Tipo | Descripción |
|---|---|---|
| `f` | `callable` | Función a integrar |
| `a` | `float` | Límite inferior de integración |
| `b` | `float` | Límite superior de integración |
| `n` | `int` | Número de subintervalos (**debe ser par**) |

### Retorna

`tuple (integral, cota_error)`

| Componente | Tipo | Descripción |
|---|---|---|
| `integral` | `float` | Valor aproximado de la integral |
| `cota_error` | `float` | Cota superior del error de truncamiento |

### Uso

```python
import math
from metodos_numericos import integral_simpson

# ∫₀^π sin(x) dx = 2 (exacto)
resultado, error = integral_simpson(math.sin, 0, math.pi, 100)
print(f"Integral   : {resultado:.10f}")  # 2.0000000011
print(f"Cota error : {error:.2e}")       # 1.72e-09

# ∫₁^e (1/x) dx = 1 (exacto)
resultado, error = integral_simpson(lambda x: 1/x, 1, math.e, 50)
print(f"Integral   : {resultado:.10f}")  # 1.0000000000
print(f"Cota error : {error:.2e}")       # 3.45e-08
```

---

## 🔬 Comparación: Numérica vs Exacta

Para casos donde se necesita la derivada **matemáticamente exacta** (sin error de aproximación), se incluye `derivada_exacta.py` basado en cálculo simbólico con [SymPy](https://www.sympy.org/).

```python
from derivada_exacta import derivada_exacta

# Derivada simbólica → expresión exacta
derivada_exacta("x**3 + 2*x")           # 3*x**2 + 2
derivada_exacta("sin(x) * exp(x)")      # sqrt(2)*exp(x)*sin(x + pi/4)

# Evaluada en un punto → valor exacto
derivada_exacta("log(x**2 + 1)", punto=3)  # (expresión, 3/5)

# Segunda derivada
derivada_exacta("exp(x)*sin(x)", orden=2)  # 2*exp(x)*cos(x)
```

| Característica | Diferencia centrada | Simbólica (SymPy) |
|---|---|---|
| Tipo de resultado | Número flotante | Expresión matemática |
| Error | Depende de `h` | Cero (exacta) |
| Velocidad | Muy rápida | Más lenta |
| Requiere | Solo `math` | `sympy` |
| Derivadas de orden n | No | Sí |

---

## ▶️ Ejecutar demostraciones

```bash
# Métodos numéricos (diferencia centrada + Simpson)
python metodos_numericos.py

# Derivada simbólica exacta
python derivada_exacta.py
```

---

## 📐 Fundamentos matemáticos

### ¿Por qué diferencia centrada y no diferencia hacia adelante?

La diferencia hacia adelante tiene error de orden $O(h)$, mientras que la diferencia centrada tiene error de orden $O(h^2)$, lo que la hace significativamente más precisa para el mismo tamaño de paso.

| Método | Fórmula | Error |
|---|---|---|
| Hacia adelante | $[f(x+h) - f(x)] / h$ | $O(h)$ |
| Hacia atrás | $[f(x) - f(x-h)] / h$ | $O(h)$ |
| **Centrada** | $[f(x+h) - f(x-h)] / 2h$ | $O(h^2)$ |

### ¿Por qué n debe ser par en Simpson?

La Regla de Simpson ajusta parábolas sobre pares de subintervalos consecutivos. Requiere un número par de subintervalos para que los coeficientes 1–4–2–4–2–…–4–1 cierren correctamente.

---

## 📄 Licencia

MIT
