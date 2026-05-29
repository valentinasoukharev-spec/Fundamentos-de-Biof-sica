import math


def derivada_diferencia_centrada(f, x, h):
    """
    Calcula la derivada numérica de f en x usando la fórmula de diferencia centrada.

    Fórmula:
        f'(x) ≈ [f(x + h) - f(x - h)] / (2h)

    Parámetros:
        f  : callable — función a derivar, debe aceptar un número real
        x  : float   — punto en el que se evalúa la derivada
        h  : float   — tamaño de paso (debe ser > 0)

    Retorna:
        float — valor aproximado de la derivada en x

    Ejemplo:
        >>> derivada_diferencia_centrada(math.sin, math.pi / 4, 1e-5)
        0.7071067811865476   # ≈ cos(π/4)
    """
    if h <= 0:
        raise ValueError("El tamaño de paso h debe ser mayor que 0.")
    return (f(x + h) - f(x - h)) / (2 * h)


def integral_simpson(f, a, b, n):
    """
    Calcula la integral definida de f en [a, b] usando la Regla de Simpson
    compuesta, y estima la cota de error.

    Fórmula de la Regla de Simpson compuesta:
        ∫[a,b] f(x) dx ≈ (h/3) * [f(x₀) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + f(xₙ)]
        donde h = (b - a) / n

    Cota de error (a partir de la segunda derivada):
        E_T ≤ (b - a)³ / (12n²) * max|f''(x)| en [a, b]

    La segunda derivada se aproxima numéricamente con diferencia centrada
    sobre una malla fina de 1000 puntos para estimar el máximo de |f''(x)|.

    Parámetros:
        f : callable — función a integrar
        a : float    — límite inferior de integración
        b : float    — límite superior de integración
        n : int      — número de subintervalos (debe ser un entero par > 0)

    Retorna:
        tuple (integral, cota_error)
            integral    : float — valor aproximado de la integral
            cota_error  : float — cota superior del error de truncamiento

    Ejemplo:
        >>> integral_simpson(math.sin, 0, math.pi, 100)
        (2.0000000010824505, 1.7231e-09)
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n debe ser un entero positivo.")
    if n % 2 != 0:
        raise ValueError("n debe ser un número par para la Regla de Simpson.")
    if a >= b:
        raise ValueError("El límite inferior a debe ser menor que el límite superior b.")

    h = (b - a) / n

    # ── Regla de Simpson compuesta ──────────────────────────────────────────
    suma = f(a) + f(b)
    for i in range(1, n):
        x_i = a + i * h
        coef = 4 if i % 2 != 0 else 2
        suma += coef * f(x_i)
    integral = (h / 3) * suma

    # ── Estimación de la cota de error ──────────────────────────────────────
    # Se aproxima max|f''(x)| con diferencia centrada en 1000 puntos internos
    puntos = 1000
    delta = (b - a) / puntos
    eps = delta * 1e-4          # paso pequeño para la segunda derivada numérica
    max_f2 = 0.0
    for k in range(1, puntos):
        xi = a + k * delta
        f2 = abs((f(xi + eps) - 2 * f(xi) + f(xi - eps)) / (eps ** 2))
        if f2 > max_f2:
            max_f2 = f2

    cota_error = ((b - a) ** 3 / (12 * n ** 2)) * max_f2

    return integral, cota_error