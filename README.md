# 🧮 Métodos Numéricos en Python

Implementación de métodos numéricos para **derivación** e **integración** de funciones matemáticas.

---

## ⚙️ Requisitos

```bash
pip install math
```

> `math` forma parte de la librería estándar de Python, no requiere instalación adicional.

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

## ▶️ Ejecutar demostración

```bash
python metodos_numericos.py
```

---

## 📄 Licencia

MIT
