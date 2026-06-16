#!/usr/bin/env python3
# coding: utf-8
"""
HALO TKINTER TUTORIAL
=====================
A comprehensive tutorial demonstrating all major tkinter components
with a Halo game theme.

Components covered:
- Window configuration (Tk)
- Labels
- Buttons  
- Entry fields
- Text widget
- Frames
- Listbox
- Checkbuttons
- Radiobuttons
- Scale/Slider
- Canvas for drawing
- Message boxes
"""

# Import tkinter for the GUI
from tkinter import *
from tkinter import messagebox, scrolledtext
from pathlib import Path

# ============================================================================
# WINDOW SETUP
# ============================================================================

# Create the main window - This is the root container for all widgets
root = Tk()

# Set the title that appears in the window's title bar
root.title("Halo Tkinter Tutorial - Spartan Training")

# Set window to be resizable (width, height) - False means fixed size
root.resizable(True, True)

# Set the initial size of the window (width x height in pixels)
root.geometry("800x600")

# Set the background color - Halo's iconic dark theme
root.configure(bg="#0a0e1a")

# Set the icon of the window (with fallback for Linux compatibility)
try:
    from PIL import Image, ImageTk
    icon_path = Path(__file__).parent / "halo.ico"
    icon_image = ImageTk.PhotoImage(Image.open(icon_path))
    root.iconphoto(True, icon_image)
except (ImportError, Exception) as e:
    # If PIL is not available or icon can't be loaded, continue without icon
    print(f"Note: Could not load icon - {e}")

# Define Halo-themed colors
HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_RED = "#ff1744"
HALO_GOLD = "#ffd700"
HALO_DARK = "#0a0e1a"
HALO_GRAY = "#2d3436"

# ============================================================================
# COMPONENT 1: LABEL - Used to display text or images
# ============================================================================

# Create a title label with custom font and colors
title_label = Label(
    root,
    text="🎮 HALO COMPONENTS SHOWCASE 🎮",
    font=("Arial", 20, "bold"),
    fg=HALO_BLUE,
    bg=HALO_DARK,
    pady=10
)
title_label.pack()  # Pack places the widget in the window

# Create an info label with different styling
info_label = Label(
    root,
    text="Spartan ID: 117 | Status: Active | Mission: Learn Tkinter",
    font=("Courier", 10),
    fg=HALO_GREEN,
    bg=HALO_DARK
)
info_label.pack()

# ============================================================================
# COMPONENT 2: FRAME - Container to group and organize widgets
# ============================================================================

# Main content frame - helps organize widgets in sections
main_frame = Frame(root, bg=HALO_DARK, padx=10, pady=10)
main_frame.pack(fill=BOTH, expand=True)

# Left panel frame for controls
left_panel = Frame(main_frame, bg=HALO_GRAY, padx=10, pady=10, relief=RIDGE, borderwidth=2)
left_panel.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

# Right panel frame for output
right_panel = Frame(main_frame, bg=HALO_GRAY, padx=10, pady=10, relief=RIDGE, borderwidth=2)
right_panel.pack(side=RIGHT, fill=BOTH, expand=True, padx=5)

# ============================================================================
# COMPONENT 3: BUTTON - Clickable element that triggers actions
# ============================================================================

Label(left_panel, text="BUTTONS:", font=("Arial", 12, "bold"), 
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(0, 5))

def activate_shields():
    """Callback function for button click"""
    messagebox.showinfo("Shields", "⚡ Energy Shields Activated!")

# Create a button with command callback
shield_button = Button(
    left_panel,
    text="🛡️ Activate Shields",
    command=activate_shields,
    bg=HALO_BLUE,
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    relief=RAISED
)
shield_button.pack(fill=X, pady=2)

def fire_weapon():
    combat_log.insert(END, "🔫 Assault Rifle fired!\n")
    combat_log.see(END)  # Auto-scroll to bottom

fire_button = Button(
    left_panel,
    text="🔫 Fire Weapon",
    command=fire_weapon,
    bg=HALO_RED,
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
fire_button.pack(fill=X, pady=2)

# ============================================================================
# COMPONENT 4: ENTRY - Single line text input field
# ============================================================================

Label(left_panel, text="ENTRY FIELD:", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(10, 5))

Label(left_panel, text="Enter Spartan Name:", fg="white", bg=HALO_GRAY).pack(anchor=W)

# StringVar is a special variable that can be traced/monitored
spartan_name = StringVar()
name_entry = Entry(
    left_panel,
    textvariable=spartan_name,
    font=("Arial", 10),
    bg="white",
    fg="black",
    width=25
)
name_entry.pack(fill=X, pady=2)
name_entry.insert(0, "Master Chief")  # Default value

def register_spartan():
    name = spartan_name.get()
    combat_log.insert(END, f"✅ Spartan '{name}' registered!\n")
    combat_log.see(END)

Button(left_panel, text="Register", command=register_spartan,
       bg=HALO_GREEN, fg="black", font=("Arial", 9, "bold")).pack(fill=X, pady=2)

# ============================================================================
# COMPONENT 5: CHECKBUTTON - Checkbox for on/off options
# ============================================================================

Label(left_panel, text="CHECKBUTTONS:", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(10, 5))

# IntVar tracks checkbox state (0=unchecked, 1=checked)
motion_tracker = IntVar()
night_vision = IntVar()
overshield = IntVar()

Checkbutton(
    left_panel,
    text="📡 Motion Tracker",
    variable=motion_tracker,
    bg=HALO_GRAY,
    fg="white",
    selectcolor="black",
    activebackground=HALO_GRAY
).pack(anchor=W)

Checkbutton(
    left_panel,
    text="🌙 Night Vision",
    variable=night_vision,
    bg=HALO_GRAY,
    fg="white",
    selectcolor="black",
    activebackground=HALO_GRAY
).pack(anchor=W)

Checkbutton(
    left_panel,
    text="💫 Overshield",
    variable=overshield,
    bg=HALO_GRAY,
    fg="white",
    selectcolor="black",
    activebackground=HALO_GRAY
).pack(anchor=W)

# ============================================================================
# COMPONENT 6: RADIOBUTTON - Multiple choice (only one selection)
# ============================================================================

Label(left_panel, text="RADIOBUTTONS:", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(10, 5))

Label(left_panel, text="Select Weapon:", fg="white", bg=HALO_GRAY).pack(anchor=W)

# StringVar to track which radio button is selected
weapon_choice = StringVar(value="Assault Rifle")

weapons = ["Assault Rifle", "Battle Rifle", "Sniper Rifle", "Rocket Launcher"]
for weapon in weapons:
    Radiobutton(
        left_panel,
        text=weapon,
        variable=weapon_choice,
        value=weapon,
        bg=HALO_GRAY,
        fg="white",
        selectcolor="black",
        activebackground=HALO_GRAY
    ).pack(anchor=W)

# ============================================================================
# COMPONENT 7: SCALE - Slider for numeric values
# ============================================================================

Label(left_panel, text="SCALE/SLIDER:", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(10, 5))

def update_difficulty(value):
    difficulty_label.config(text=f"Difficulty: {int(float(value))}")

difficulty_label = Label(left_panel, text="Difficulty: 5", fg="white", bg=HALO_GRAY)
difficulty_label.pack(anchor=W)

difficulty_scale = Scale(
    left_panel,
    from_=1,
    to=10,
    orient=HORIZONTAL,
    bg=HALO_GRAY,
    fg="white",
    troughcolor=HALO_DARK,
    highlightbackground=HALO_GRAY,
    command=update_difficulty,
    length=200
)
difficulty_scale.set(5)
difficulty_scale.pack(fill=X)

# ============================================================================
# COMPONENT 8: LISTBOX - List of selectable items
# ============================================================================

Label(right_panel, text="LISTBOX:", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(0, 5))

Label(right_panel, text="Available Maps:", fg="white", bg=HALO_GRAY).pack(anchor=W)

# Create a frame for listbox with scrollbar
listbox_frame = Frame(right_panel, bg=HALO_GRAY)
listbox_frame.pack(fill=BOTH, expand=True, pady=5)

# Scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Listbox with multiple selection mode
maps_listbox = Listbox(
    listbox_frame,
    font=("Courier", 9),
    bg="white",
    fg="black",
    selectbackground=HALO_BLUE,
    height=6,
    yscrollcommand=scrollbar.set
)
maps_listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=maps_listbox.yview)

# Add items to the listbox
halo_maps = [
    "Blood Gulch",
    "Lockout",
    "Guardian",
    "Valhalla",
    "The Pit",
    "Sandtrap",
    "High Ground",
    "Zanzibar"
]

for map_name in halo_maps:
    maps_listbox.insert(END, map_name)

def load_selected_map():
    selection = maps_listbox.curselection()
    if selection:
        map_name = maps_listbox.get(selection[0])
        combat_log.insert(END, f"🗺️ Loading map: {map_name}\n")
        combat_log.see(END)

Button(right_panel, text="Load Selected Map", command=load_selected_map,
       bg=HALO_BLUE, fg="white", font=("Arial", 9, "bold")).pack(fill=X, pady=5)

# ============================================================================
# COMPONENT 9: TEXT WIDGET - Multi-line text display/edit
# ============================================================================

Label(right_panel, text="TEXT WIDGET (Combat Log):", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_GRAY).pack(anchor=W, pady=(10, 5))

# ScrolledText is a Text widget with built-in scrollbar
combat_log = scrolledtext.ScrolledText(
    right_panel,
    font=("Courier", 9),
    bg="black",
    fg=HALO_GREEN,
    height=10,
    wrap=WORD,
    relief=SUNKEN,
    borderwidth=2
)
combat_log.pack(fill=BOTH, expand=True)

# Insert initial text
combat_log.insert(END, "=== COMBAT LOG INITIALIZED ===\n")
combat_log.insert(END, "System: All components loaded\n")
combat_log.insert(END, "Status: Ready for combat\n")
combat_log.insert(END, "─" * 40 + "\n")

# ============================================================================
# COMPONENT 10: CANVAS - Drawing area for graphics
# ============================================================================

# Create a small canvas at the bottom for visual effects
canvas = Canvas(root, bg=HALO_DARK, height=50, highlightthickness=0)
canvas.pack(fill=X)

# Draw some Halo-themed graphics
# Create a shield bar visualization
canvas.create_rectangle(10, 15, 200, 35, fill=HALO_BLUE, outline=HALO_GOLD, width=2)
canvas.create_text(105, 25, text="SHIELD STATUS", fill="white", font=("Arial", 10, "bold"))

# Draw health bar
canvas.create_rectangle(220, 15, 410, 35, fill=HALO_GREEN, outline=HALO_GOLD, width=2)
canvas.create_text(315, 25, text="HEALTH STATUS", fill="black", font=("Arial", 10, "bold"))

# Draw ammo indicator
canvas.create_oval(430, 15, 470, 35, fill=HALO_RED, outline=HALO_GOLD, width=2)
canvas.create_text(450, 25, text="∞", fill="white", font=("Arial", 14, "bold"))

# ============================================================================
# COMPONENT 11: MENU BAR - Dropdown menus
# ============================================================================

# Create menu bar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Mission", command=lambda: combat_log.insert(END, "📋 New mission created\n"))
file_menu.add_command(label="Load Game", command=lambda: combat_log.insert(END, "💾 Game loaded\n"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Options menu
options_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Settings", command=lambda: messagebox.showinfo("Settings", "⚙️ Settings panel"))
options_menu.add_command(label="Controls", command=lambda: messagebox.showinfo("Controls", "🎮 Control configuration"))

# Help menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo(
    "About", 
    "Halo Tkinter Tutorial\n\nDemonstrating all major tkinter components\nwith Halo theme!\n\nFinish the fight! 🎮"
))

# ============================================================================
# FINAL STATUS MESSAGE
# ============================================================================

combat_log.insert(END, "\n✅ All Tkinter components demonstrated!\n")
combat_log.insert(END, "Components covered:\n")
combat_log.insert(END, "  • Labels, Buttons, Entry\n")
combat_log.insert(END, "  • Frames, Checkbuttons, Radiobuttons\n")
combat_log.insert(END, "  • Scale, Listbox, Text, Canvas\n")
combat_log.insert(END, "  • Menu bar, Message boxes\n")

# ============================================================================
# RUN THE APPLICATION
# ============================================================================

# Start the main event loop - keeps the window open and responsive
root.mainloop()
