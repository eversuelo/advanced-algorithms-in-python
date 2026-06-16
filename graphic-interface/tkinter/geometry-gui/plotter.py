#!/usr/bin/env python3
# coding: utf-8
"""
HALO EQUATION PLOTTER
=====================
Graficador de ecuaciones matemáticas 2D y 3D con interfaz Tkinter.
Soporta ecuaciones como: x²+y²=z², y=x², x²+y²=25, etc.

Características:
- Gráficas 2D (funciones y ecuaciones implícitas)
- Gráficas 3D (superficies)
- Ecuaciones predefinidas (círculo, parábola, esfera, etc.)
- Entrada personalizada de ecuaciones
- Controles interactivos
- Tema Halo
"""

from tkinter import *
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Halo theme colors
HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_RED = "#ff1744"
HALO_GOLD = "#ffd700"
HALO_DARK = "#0a0e1a"
HALO_GRAY = "#2d3436"

class EquationPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Halo Equation Plotter - Graficador Matemático")
        self.root.geometry("1200x800")
        self.root.configure(bg=HALO_DARK)
        
        # Plot mode: '2d' or '3d'
        self.plot_mode = StringVar(value='2d')
        
        # Equation presets
        self.presets_2d = {
            "Parábola: y = x²": "y = x**2",
            "Círculo: x² + y² = 25": "x**2 + y**2 = 25",
            "Hipérbola: x² - y² = 1": "x**2 - y**2 = 1",
            "Seno: y = sin(x)": "y = np.sin(x)",
            "Coseno: y = cos(x)": "y = np.cos(x)",
            "Elipse: x²/4 + y²/9 = 1": "x**2/4 + y**2/9 = 1",
        }
        
        self.presets_3d = {
            "Esfera: x² + y² + z² = 25": "x**2 + y**2 + z**2 = 25",
            "Paraboloide: z = x² + y²": "z = x**2 + y**2",
            "Cono: x² + y² = z²": "x**2 + y**2 = z**2",
            "Hiperboloide: x² + y² - z² = 1": "x**2 + y**2 - z**2 = 1",
            "Plano: z = 2x + 3y": "z = 2*x + 3*y",
            "Silla: z = x² - y²": "z = x**2 - y**2",
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # ====================================================================
        # HEADER
        # ====================================================================
        header = Frame(self.root, bg=HALO_DARK, pady=10)
        header.pack(fill=X)
        
        Label(
            header,
            text="🎮 HALO EQUATION PLOTTER 🎮",
            font=("Arial", 24, "bold"),
            fg=HALO_BLUE,
            bg=HALO_DARK
        ).pack()
        
        Label(
            header,
            text="Graficador de Ecuaciones Matemáticas 2D y 3D",
            font=("Arial", 12),
            fg=HALO_GREEN,
            bg=HALO_DARK
        ).pack()
        
        # ====================================================================
        # MAIN CONTAINER
        # ====================================================================
        main_container = Frame(self.root, bg=HALO_DARK)
        main_container.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Controls
        left_panel = Frame(main_container, bg=HALO_GRAY, padx=15, pady=15, 
                          relief=RIDGE, borderwidth=3, width=350)
        left_panel.pack(side=LEFT, fill=Y, padx=5)
        left_panel.pack_propagate(False)
        
        # Right panel - Plot area
        right_panel = Frame(main_container, bg=HALO_GRAY, padx=10, pady=10,
                           relief=RIDGE, borderwidth=3)
        right_panel.pack(side=RIGHT, fill=BOTH, expand=True, padx=5)
        
        # ====================================================================
        # LEFT PANEL - CONTROLS
        # ====================================================================
        
        # Mode selection
        Label(left_panel, text="MODO DE GRÁFICA", font=("Arial", 12, "bold"),
              fg=HALO_GOLD, bg=HALO_GRAY).pack(pady=(0, 10))
        
        mode_frame = Frame(left_panel, bg=HALO_GRAY)
        mode_frame.pack(pady=5)
        
        Radiobutton(
            mode_frame,
            text="2D",
            variable=self.plot_mode,
            value='2d',
            bg=HALO_GRAY,
            fg="white",
            selectcolor="black",
            font=("Arial", 11),
            command=self.update_presets
        ).pack(side=LEFT, padx=10)
        
        Radiobutton(
            mode_frame,
            text="3D",
            variable=self.plot_mode,
            value='3d',
            bg=HALO_GRAY,
            fg="white",
            selectcolor="black",
            font=("Arial", 11),
            command=self.update_presets
        ).pack(side=LEFT, padx=10)
        
        # Separator
        Frame(left_panel, bg=HALO_BLUE, height=2).pack(fill=X, pady=15)
        
        # Preset equations
        Label(left_panel, text="ECUACIONES PREDEFINIDAS", font=("Arial", 11, "bold"),
              fg=HALO_GOLD, bg=HALO_GRAY).pack(pady=(0, 10))
        
        self.preset_listbox = Listbox(
            left_panel,
            font=("Courier", 9),
            bg="white",
            fg="black",
            selectbackground=HALO_BLUE,
            height=8
        )
        self.preset_listbox.pack(fill=X, pady=5)
        self.preset_listbox.bind('<<ListboxSelect>>', self.load_preset)
        
        # Custom equation
        Label(left_panel, text="ECUACIÓN PERSONALIZADA", font=("Arial", 11, "bold"),
              fg=HALO_GOLD, bg=HALO_GRAY).pack(pady=(15, 5))
        
        Label(left_panel, text="Ingresa tu ecuación:", fg="white", bg=HALO_GRAY).pack(anchor=W)
        
        self.equation_entry = Entry(left_panel, font=("Courier", 10), width=30)
        self.equation_entry.pack(fill=X, pady=5)
        
        # Help text
        help_frame = Frame(left_panel, bg=HALO_DARK, relief=SUNKEN, borderwidth=2, padx=8, pady=8)
        help_frame.pack(fill=X, pady=10)
        
        Label(help_frame, text="💡 AYUDA:", font=("Arial", 9, "bold"),
              fg=HALO_GREEN, bg=HALO_DARK, anchor=W).pack(fill=X)
        
        help_text = """2D: y = ..., x**2 + y**2 = ...
3D: z = ..., x**2 + y**2 + z**2 = ...

Operadores:
  + - * / ** (potencia)
  np.sin(), np.cos(), np.sqrt()
  
Ejemplos:
  y = x**2
  x**2 + y**2 = 25
  z = x**2 + y**2"""
        
        Label(help_frame, text=help_text, font=("Courier", 8),
              fg="white", bg=HALO_DARK, justify=LEFT).pack(fill=X)
        
        # Range controls
        Label(left_panel, text="RANGO", font=("Arial", 11, "bold"),
              fg=HALO_GOLD, bg=HALO_GRAY).pack(pady=(15, 5))
        
        range_frame = Frame(left_panel, bg=HALO_GRAY)
        range_frame.pack(fill=X, pady=5)
        
        Label(range_frame, text="Min:", fg="white", bg=HALO_GRAY).grid(row=0, column=0, sticky=W)
        self.min_entry = Entry(range_frame, width=8, font=("Arial", 10))
        self.min_entry.grid(row=0, column=1, padx=5)
        self.min_entry.insert(0, "-10")
        
        Label(range_frame, text="Max:", fg="white", bg=HALO_GRAY).grid(row=0, column=2, sticky=W, padx=(10, 0))
        self.max_entry = Entry(range_frame, width=8, font=("Arial", 10))
        self.max_entry.grid(row=0, column=3, padx=5)
        self.max_entry.insert(0, "10")
        
        # Action buttons
        Button(
            left_panel,
            text="📊 GRAFICAR",
            command=self.plot_equation,
            bg=HALO_BLUE,
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            relief=RAISED,
            borderwidth=3
        ).pack(fill=X, pady=(20, 5))
        
        Button(
            left_panel,
            text="🗑️ LIMPIAR",
            command=self.clear_plot,
            bg=HALO_RED,
            fg="white",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=8
        ).pack(fill=X, pady=5)
        
        # ====================================================================
        # RIGHT PANEL - PLOT AREA
        # ====================================================================
        
        Label(right_panel, text="VISUALIZACIÓN", font=("Arial", 14, "bold"),
              fg=HALO_GOLD, bg=HALO_GRAY).pack(pady=(0, 10))
        
        # Create matplotlib figure
        self.fig = Figure(figsize=(8, 6), facecolor=HALO_DARK)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        
        # Add navigation toolbar
        toolbar_frame = Frame(right_panel, bg=HALO_GRAY)
        toolbar_frame.pack(fill=X)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        
        # Initialize with 2D presets
        self.update_presets()
        
    def update_presets(self):
        """Actualiza la lista de ecuaciones predefinidas según el modo"""
        self.preset_listbox.delete(0, END)
        
        presets = self.presets_2d if self.plot_mode.get() == '2d' else self.presets_3d
        
        for name in presets.keys():
            self.preset_listbox.insert(END, name)
    
    def load_preset(self, event):
        """Carga una ecuación predefinida"""
        selection = self.preset_listbox.curselection()
        if selection:
            preset_name = self.preset_listbox.get(selection[0])
            presets = self.presets_2d if self.plot_mode.get() == '2d' else self.presets_3d
            equation = presets[preset_name]
            self.equation_entry.delete(0, END)
            self.equation_entry.insert(0, equation)
    
    def plot_equation(self):
        """Grafica la ecuación ingresada"""
        equation = self.equation_entry.get().strip()
        
        if not equation:
            messagebox.showwarning("Advertencia", "Por favor ingresa una ecuación")
            return
        
        try:
            x_min = float(self.min_entry.get())
            x_max = float(self.max_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Los valores de rango deben ser números")
            return
        
        # Clear previous plot
        self.fig.clear()
        
        try:
            if self.plot_mode.get() == '2d':
                self.plot_2d(equation, x_min, x_max)
            else:
                self.plot_3d(equation, x_min, x_max)
            
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error al graficar", f"Error: {str(e)}\n\nVerifica la sintaxis de tu ecuación.")
    
    def plot_2d(self, equation, x_min, x_max):
        """Grafica ecuación en 2D"""
        ax = self.fig.add_subplot(111)
        ax.set_facecolor(HALO_DARK)
        ax.grid(True, color=HALO_GRAY, alpha=0.3)
        
        # Configurar colores del plot
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        
        x = np.linspace(x_min, x_max, 1000)
        
        # Check if it's a function (y = ...) or implicit equation
        if '=' in equation:
            parts = equation.split('=')
            
            if 'y' in parts[0] and 'y' not in parts[1]:
                # Function form: y = f(x)
                expr = parts[1].strip()
                y = eval(expr, {"__builtins__": None}, {"x": x, "np": np})
                ax.plot(x, y, color=HALO_BLUE, linewidth=2, label=equation)
                ax.set_xlabel('x', fontsize=12)
                ax.set_ylabel('y', fontsize=12)
            else:
                # Implicit equation: f(x,y) = c
                y = np.linspace(x_min, x_max, 500)
                X, Y = np.meshgrid(x, y)
                
                # Evaluate both sides
                left_side = eval(parts[0].strip(), {"__builtins__": None}, 
                               {"x": X, "y": Y, "np": np})
                right_side = eval(parts[1].strip(), {"__builtins__": None},
                                {"x": X, "y": Y, "np": np})
                
                # Plot contour where left = right
                ax.contour(X, Y, left_side - right_side, [0], colors=HALO_GREEN, linewidths=2)
                ax.set_xlabel('x', fontsize=12)
                ax.set_ylabel('y', fontsize=12)
                ax.set_title(equation, color=HALO_GOLD, fontsize=14, pad=20)
        else:
            # Direct expression
            y = eval(equation, {"__builtins__": None}, {"x": x, "np": np})
            ax.plot(x, y, color=HALO_BLUE, linewidth=2, label=equation)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
        
        ax.legend(facecolor=HALO_GRAY, edgecolor='white', labelcolor='white')
        ax.set_title(f'Gráfica 2D: {equation}', color=HALO_GOLD, fontsize=14, pad=20)
    
    def plot_3d(self, equation, x_min, x_max):
        """Grafica ecuación en 3D"""
        ax = self.fig.add_subplot(111, projection='3d')
        ax.set_facecolor(HALO_DARK)
        
        # Configurar colores
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.zaxis.label.set_color('white')
        
        # Create grid
        x = np.linspace(x_min, x_max, 50)
        y = np.linspace(x_min, x_max, 50)
        X, Y = np.meshgrid(x, y)
        
        if '=' in equation:
            parts = equation.split('=')
            
            if 'z' in parts[0] and 'z' not in parts[1]:
                # Function form: z = f(x,y)
                expr = parts[1].strip()
                Z = eval(expr, {"__builtins__": None}, {"x": X, "y": Y, "np": np})
                surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, 
                                      edgecolor='none', antialiased=True)
                self.fig.colorbar(surf, ax=ax, shrink=0.5)
            else:
                # Implicit surface: f(x,y,z) = c
                # Use marching cubes or contour3D
                z = np.linspace(x_min, x_max, 30)
                X3, Y3, Z3 = np.meshgrid(x, y, z)
                
                left_side = eval(parts[0].strip(), {"__builtins__": None},
                               {"x": X3, "y": Y3, "z": Z3, "np": np})
                right_side = float(eval(parts[1].strip(), {"__builtins__": None},
                                      {"np": np}))
                
                # Plot isosurface
                from skimage import measure
                try:
                    verts, faces, _, _ = measure.marching_cubes(left_side, right_side)
                    # Scale to actual coordinates
                    verts = verts * (x_max - x_min) / 30 + x_min
                    ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
                                   cmap='viridis', alpha=0.8, edgecolor='none',
                                   antialiased=True)
                except:
                    # Fallback to contour plot
                    for level in np.linspace(x_min, x_max, 10):
                        ax.contour(X, Y, Z3[:, :, 15], levels=[level],
                                  colors=HALO_BLUE, alpha=0.3)
        else:
            # Direct expression
            Z = eval(equation, {"__builtins__": None}, {"x": X, "y": Y, "np": np})
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8,
                                  edgecolor='none', antialiased=True)
            self.fig.colorbar(surf, ax=ax, shrink=0.5)
        
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        ax.set_zlabel('Z', fontsize=12)
        ax.set_title(f'Gráfica 3D: {equation}', color=HALO_GOLD, fontsize=14, pad=20)
    
    def clear_plot(self):
        """Limpia el gráfico"""
        self.fig.clear()
        self.canvas.draw()
        self.equation_entry.delete(0, END)

def main():
    root = Tk()
    app = EquationPlotter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
