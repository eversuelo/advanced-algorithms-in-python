#!/usr/bin/env python3
# coding: utf-8
"""
BUTTON COMPONENT - HALO THEME
==============================
Buttons are interactive widgets that trigger actions when clicked.
They are essential for user interaction in GUI applications.

KEY FEATURES:
- Execute functions when clicked
- Customizable appearance (colors, fonts, borders)
- Support for images and text
- Can be enabled/disabled
- Multiple styling states (normal, active, disabled)
"""

from tkinter import *
from tkinter import messagebox

# Halo theme colors
HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_RED = "#ff1744"
HALO_GOLD = "#ffd700"
HALO_DARK = "#0a0e1a"
HALO_GRAY = "#2d3436"

# Create main window
root = Tk()
root.title("Button Component - Halo Theme")
root.geometry("600x700")
root.configure(bg=HALO_DARK)

# Status label for displaying button actions
status_label = Label(
    root,
    text="Click buttons to see actions",
    font=("Courier", 11),
    fg=HALO_GREEN,
    bg=HALO_DARK,
    pady=10
)
status_label.pack()

# ============================================================================
# EXAMPLE 1: Basic Button
# ============================================================================
Label(root, text="EXAMPLE 1: Basic Button", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

def basic_action():
    status_label.config(text="✅ Basic button clicked!")

basic_button = Button(
    root,
    text="Click Me",
    command=basic_action,  # Function to call when clicked
    bg=HALO_BLUE,
    fg="white",
    font=("Arial", 11)
)
basic_button.pack()

# ============================================================================
# EXAMPLE 2: Styled Action Buttons
# ============================================================================
Label(root, text="EXAMPLE 2: Styled Buttons", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

button_frame = Frame(root, bg=HALO_DARK)
button_frame.pack(pady=5)

def activate_shields():
    messagebox.showinfo("Shields", "🛡️ Energy Shields Activated!")
    status_label.config(text="🛡️ Shields: ACTIVE")

Button(
    button_frame,
    text="🛡️ Activate Shields",
    command=activate_shields,
    bg=HALO_BLUE,
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief=RAISED,
    borderwidth=3
).pack(side=LEFT, padx=5)

def fire_weapon():
    status_label.config(text="🔫 Assault Rifle: FIRING!")

Button(
    button_frame,
    text="🔫 Fire Weapon",
    command=fire_weapon,
    bg=HALO_RED,
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief=RAISED,
    borderwidth=3
).pack(side=LEFT, padx=5)

def reload_weapon():
    status_label.config(text="🔄 Reloading weapon...")

Button(
    button_frame,
    text="🔄 Reload",
    command=reload_weapon,
    bg=HALO_GREEN,
    fg="black",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief=RAISED,
    borderwidth=3
).pack(side=LEFT, padx=5)

# ============================================================================
# EXAMPLE 3: Button with State Changes
# ============================================================================
Label(root, text="EXAMPLE 3: Toggle Button", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

night_vision_active = False

def toggle_night_vision():
    global night_vision_active
    night_vision_active = not night_vision_active
    
    if night_vision_active:
        toggle_btn.config(
            text="🌙 Night Vision: ON",
            bg=HALO_GREEN,
            fg="black"
        )
        status_label.config(text="🌙 Night Vision Activated")
    else:
        toggle_btn.config(
            text="🌙 Night Vision: OFF",
            bg=HALO_GRAY,
            fg="white"
        )
        status_label.config(text="🌙 Night Vision Deactivated")

toggle_btn = Button(
    root,
    text="🌙 Night Vision: OFF",
    command=toggle_night_vision,
    bg=HALO_GRAY,
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=10,
    width=20
)
toggle_btn.pack()

# ============================================================================
# EXAMPLE 4: Counter Button
# ============================================================================
Label(root, text="EXAMPLE 4: Counter Button", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

kill_count = 0

def increment_kills():
    global kill_count
    kill_count += 1
    counter_btn.config(text=f"💀 Kills: {kill_count}")
    status_label.config(text=f"Enemy eliminated! Total: {kill_count}")

counter_btn = Button(
    root,
    text=f"💀 Kills: {kill_count}",
    command=increment_kills,
    bg=HALO_RED,
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
)
counter_btn.pack()

def reset_counter():
    global kill_count
    kill_count = 0
    counter_btn.config(text=f"💀 Kills: {kill_count}")
    status_label.config(text="Kill counter reset")

Button(
    root,
    text="Reset Counter",
    command=reset_counter,
    bg=HALO_GRAY,
    fg="white",
    font=("Arial", 9),
    padx=10,
    pady=5
).pack(pady=5)

# ============================================================================
# EXAMPLE 5: Enable/Disable Button
# ============================================================================
Label(root, text="EXAMPLE 5: Disable/Enable", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

def launch_missile():
    messagebox.showwarning("Missile", "🚀 Missile Launched!")
    status_label.config(text="🚀 Missile launched!")

missile_btn = Button(
    root,
    text="🚀 Launch Missile",
    command=launch_missile,
    bg=HALO_RED,
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=10
)
missile_btn.pack()

def toggle_missile_system():
    if missile_btn['state'] == NORMAL:
        missile_btn.config(state=DISABLED)  # Disable button
        toggle_system_btn.config(text="Enable Missile System")
        status_label.config(text="⚠️ Missile system disabled")
    else:
        missile_btn.config(state=NORMAL)    # Enable button
        toggle_system_btn.config(text="Disable Missile System")
        status_label.config(text="✅ Missile system enabled")

toggle_system_btn = Button(
    root,
    text="Disable Missile System",
    command=toggle_missile_system,
    bg=HALO_GRAY,
    fg="white",
    font=("Arial", 9),
    padx=10,
    pady=5
)
toggle_system_btn.pack(pady=5)

# ============================================================================
# EXAMPLE 6: Button Styles Reference
# ============================================================================
Label(root, text="EXAMPLE 6: Different Relief Styles", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

styles_frame = Frame(root, bg=HALO_DARK)
styles_frame.pack()

relief_styles = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE]
style_names = ["FLAT", "RAISED", "SUNKEN", "GROOVE", "RIDGE"]

for i, (relief_style, name) in enumerate(zip(relief_styles, style_names)):
    Button(
        styles_frame,
        text=name,
        relief=relief_style,
        bg=HALO_BLUE,
        fg="white",
        font=("Arial", 9),
        padx=10,
        pady=5,
        borderwidth=3
    ).grid(row=0, column=i, padx=3)

# ============================================================================
# EXAMPLE 7: Button with Lambda Function
# ============================================================================
Label(root, text="EXAMPLE 7: Buttons with Parameters", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

def select_weapon(weapon_name):
    status_label.config(text=f"⚔️ Selected: {weapon_name}")

weapons_frame = Frame(root, bg=HALO_DARK)
weapons_frame.pack()

weapons = ["Assault Rifle", "Battle Rifle", "Sniper", "Shotgun"]
for weapon in weapons:
    Button(
        weapons_frame,
        text=weapon,
        command=lambda w=weapon: select_weapon(w),  # Lambda with parameter
        bg=HALO_BLUE,
        fg="white",
        font=("Arial", 9),
        padx=8,
        pady=5
    ).pack(side=LEFT, padx=2)

# ============================================================================
# OPTIONS REFERENCE
# ============================================================================
Label(root, text="COMMON BUTTON OPTIONS", font=("Arial", 11, "bold", "underline"),
      fg=HALO_GREEN, bg=HALO_DARK).pack(pady=(20, 5))

options_text = """command - Function to call when clicked
text - Button label text
bg/background - Background color
fg/foreground - Text color
font - Font configuration
padx/pady - Internal padding
width/height - Button size
state - NORMAL, DISABLED, ACTIVE
relief - Border style (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
borderwidth - Border thickness"""

Label(
    root,
    text=options_text,
    font=("Courier", 9),
    fg="white",
    bg=HALO_DARK,
    justify=LEFT
).pack()

# Run the application
root.mainloop()
