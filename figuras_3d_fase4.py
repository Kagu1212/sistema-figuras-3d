# -*- coding: utf-8 -*-
"""
Fase 3 — Modelos de herencia, polimorfismo y gestión de métodos
Ejercicio 2: Advanced 3D Shapes System
Estudiante: Kevin Alfonso Gómez Urbano
Código / Documento: [Tu número de identificación]
Curso: 213023 — Programación
Fecha: 2026-10-10
"""

import tkinter as tk
from tkinter import ttk
import math
from abc import ABC, abstractmethod
from datetime import datetime


class Figura3D(ABC):
    """Abstract base class for all 3D shapes — defines common interface."""

    def __init__(self):
        self.escala = 1.0

    @abstractmethod
    def calcular_volumen(self):
        """Calculate shape volume — must be implemented by each subclass."""
        pass

    @abstractmethod
    def calcular_area_superficial(self, factor_escala=None):
        """
        Calculate surface area — OVERLOADING via optional parameter.
        Called without argument → uses instance scale; with factor → uses given value.
        """
        pass

    @abstractmethod
    def dibujar(self):
        """Return string representation — POLYMORPHIC method."""
        pass

    def aplicar_escala(self, factor):
        """Set scale factor for all subsequent calculations."""
        if factor > 0:
            self.escala = factor


class Cubo(Figura3D):
    """Cube defined by side length."""

    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self):
        """Override — Volume = side³."""
        l = self.lado * self.escala
        return round(l ** 3, 4)

    def calcular_area_superficial(self, factor_escala=None):
        """Override with overloading — 6 × side²."""
        escala_real = self.escala if factor_escala is None else factor_escala
        l = self.lado * escala_real
        return round(6 * (l ** 2), 4)

    def dibujar(self):
        """Polymorphic representation."""
        return f"[CUBE] Side: {self.lado} units | Active scale: {self.escala}×"


class Esfera(Figura3D):
    """Sphere defined by radius."""

    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        """Override — Volume = (4/3) × π × r³."""
        r = self.radio * self.escala
        return round((4 / 3) * math.pi * (r ** 3), 4)

    def calcular_area_superficial(self, factor_escala=None):
        """Override with overloading — 4 × π × r²."""
        escala_real = self.escala if factor_escala is None else factor_escala
        r = self.radio * escala_real
        return round(4 * math.pi * (r ** 2), 4)

    def dibujar(self):
        """Polymorphic representation."""
        return f"[SPHERE] Radius: {self.radio} units | Active scale: {self.escala}×"


class Cilindro(Figura3D):
    """Right cylinder defined by radius and height."""

    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        """Override — Volume = π × r² × h."""
        r = self.radio * self.escala
        h = self.altura * self.escala
        return round(math.pi * (r ** 2) * h, 4)

    def calcular_area_superficial(self, factor_escala=None):
        """Override with overloading — 2πrh + 2πr²."""
        escala_real = self.escala if factor_escala is None else factor_escala
        r = self.radio * escala_real
        h = self.altura * escala_real
        return round((2 * math.pi * r * h) + (2 * math.pi * (r ** 2)), 4)

    def dibujar(self):
        """Polymorphic representation."""
        return f"[CYLINDER] Radius: {self.radio}, Height: {self.altura} units | Active scale: {self.escala}×"


class ShapesSystemApp:
    """Main GUI application — ALL text in ENGLISH as required."""

    def __init__(self, root):
        self.root = root
        self.root.title("3D Shapes System — Fase 3 UNAD")
        self.root.geometry("760x560")

        # Polymorphic collection — mixed shapes, same base type
        self.shapes = [
            Cubo(5),
            Esfera(3),
            Cilindro(2, 6),
            Cubo(4),
            Esfera(5),
            Cilindro(3, 8)
        ]

        self._build_interface()

    def _build_interface(self):
        """Construct all interface elements."""
        ttk.Label(
            self.root,
            text="3D Shapes System — Inheritance & Polymorphism Demo",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        self.output_area = tk.Text(self.root, wrap=tk.WORD, height=26, width=88, font=("Consolas", 10))
        self.output_area.pack(pady=8, padx=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text="1. List All Shapes", command=self.show_all).grid(row=0, column=0, padx=4)
        ttk.Button(button_frame, text="2. Calculate Volumes", command=self.show_volumes).grid(row=0, column=1, padx=4)
        ttk.Button(button_frame, text="3. Surface Areas (Standard)", command=self.show_areas_standard).grid(row=0, column=2, padx=4)
        ttk.Button(button_frame, text="4. Surface Areas (Scaled ×2)", command=self.show_areas_scaled).grid(row=0, column=3, padx=4)
        ttk.Button(button_frame, text="Clear", command=self._clear).grid(row=0, column=4, padx=4)

        self._log(f"System initialized — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self._log("Demonstration: same method calls → different behaviors (polymorphism)\n")

    def _log(self, message):
        self.output_area.insert(tk.END, message + "\n")

    def _clear(self):
        self.output_area.delete("1.0", tk.END)

    def show_all(self):
        """Call polymorphic dibujar() on every shape."""
        self._log("=== LIST OF REGISTERED SHAPES ===")
        for shape in self.shapes:
            self._log(shape.dibujar())
        self._log("")

    def show_volumes(self):
        """Call polymorphic calcular_volumen() on every shape."""
        self._log("=== CALCULATED VOLUMES ===")
        for shape in self.shapes:
            self._log(f"{shape.dibujar()} → Volume: {shape.calcular_volumen()} cubic units")
        self._log("")

    def show_areas_standard(self):
        """Overload form 1 — no factor provided."""
        self._log("=== SURFACE AREAS — STANDARD SCALE ===")
        for shape in self.shapes:
            area = shape.calcular_area_superficial()
            self._log(f"{shape.dibujar()} → Surface Area: {area} sq units")
        self._log("")

    def show_areas_scaled(self):
        """Overload form 2 — scale factor = 2 explicitly passed."""
        self._log("=== SURFACE AREAS — SCALE FACTOR = 2 ===")
        for shape in self.shapes:
            area = shape.calcular_area_superficial(factor_escala=2)
            self._log(f"{shape.dibujar()} → Scaled Area: {area} sq units")
        self._log("")


if __name__ == "__main__":
    main_window = tk.Tk()
    app = ShapesSystemApp(main_window)
    main_window.mainloop()