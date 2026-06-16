#!/usr/bin/env python3
# coding: utf-8
"""
LABEL COMPONENT - HALO THEME
=============================
Labels are used to display text or images in your tkinter application.
They are non-interactive display widgets.

KEY FEATURES:
- Display static text or images
- Customize fonts, colors, and alignment
- Support for multi-line text
- Can display images using PhotoImage
"""

from tkinter import *

# Halo theme colors
HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_DARK = "#0a0e1a"

# Create main window
root = Tk()
root.title("Label Component - Halo Theme")
root.geometry("600x500")
root.configure(bg=HALO_DARK)

# ============================================================================
# EXAMPLE 1: Basic Label
# ============================================================================
basic_label = Label(
    root,
    text="BASIC LABEL: Welcome to Halo",
    bg=HALO_DARK,
    fg="white",
    font=("Arial", 12)
)
basic_label.pack(pady=10)

# ============================================================================
# EXAMPLE 2: Styled Title Label
# ============================================================================
title_label = Label(
    root,
    text="🎮 MASTER CHIEF - SPARTAN 117 🎮",
    font=("Arial", 24, "bold"),  # Font: (family, size, style)
    fg=HALO_BLUE,
    bg=HALO_DARK,
    pady=15  # Internal padding
)
title_label.pack()

# ============================================================================
# EXAMPLE 3: Multi-line Label
# ============================================================================
info_text = """Mission Status: Active
Location: Installation 04
Objective: Destroy the Halo Ring
Allies: Cortana, Marines"""

multiline_label = Label(
    root,
    text=info_text,
    font=("Courier", 11),
    fg=HALO_GREEN,
    bg=HALO_DARK,
    justify=LEFT,  # Text alignment: LEFT, CENTER, RIGHT
    anchor=W,      # Widget anchor position
    padx=20,
    pady=10
)
multiline_label.pack()

# ============================================================================
# EXAMPLE 4: Label with Border/Relief
# ============================================================================
bordered_label = Label(
    root,
    text="⚠️ WARNING: Flood Detected Nearby ⚠️",
    font=("Arial", 14, "bold"),
    fg="yellow",
    bg="red",
    relief=RAISED,    # Relief style: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
    borderwidth=5,    # Border thickness
    padx=20,
    pady=10
)
bordered_label.pack(pady=15)

# ============================================================================
# EXAMPLE 5: Dynamic Label (updates programmatically)
# ============================================================================
shield_percentage = 100

dynamic_label = Label(
    root,
    text=f"🛡️ Shield: {shield_percentage}%",
    font=("Arial", 16, "bold"),
    fg=HALO_BLUE,
    bg=HALO_DARK
)
dynamic_label.pack(pady=10)

def update_shield():
    """Function to update label text dynamically"""
    global shield_percentage
    shield_percentage -= 10
    if shield_percentage < 0:
        shield_percentage = 100
    
    # Update the label text
    dynamic_label.config(text=f"🛡️ Shield: {shield_percentage}%")
    
    # Change color based on shield level
    if shield_percentage <= 30:
        dynamic_label.config(fg="red")
    elif shield_percentage <= 60:
        dynamic_label.config(fg="yellow")
    else:
        dynamic_label.config(fg=HALO_BLUE)

# Button to trigger shield update
Button(
    root,
    text="Take Damage",
    command=update_shield,
    bg=HALO_BLUE,
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=5
).pack(pady=10)

# ============================================================================
# EXAMPLE 6: Label Options Reference
# ============================================================================
reference_frame = Frame(root, bg=HALO_DARK)
reference_frame.pack(pady=20)

Label(
    reference_frame,
    text="COMMON LABEL OPTIONS:",
    font=("Arial", 12, "bold", "underline"),
    fg=HALO_GREEN,
    bg=HALO_DARK
).pack()

options_text = """text - The text to display
font - Font tuple: (family, size, style)
fg/foreground - Text color
bg/background - Background color
pady/padx - External padding (spacing)
justify - Text alignment (LEFT, CENTER, RIGHT)
relief - Border style (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
borderwidth - Border thickness
anchor - Position within widget (N, S, E, W, NE, NW, SE, SW, CENTER)
wraplength - Max line width before wrapping"""

Label(
    reference_frame,
    text=options_text,
    font=("Courier", 9),
    fg="white",
    bg=HALO_DARK,
    justify=LEFT
).pack()

# Run the application
root.mainloop()
