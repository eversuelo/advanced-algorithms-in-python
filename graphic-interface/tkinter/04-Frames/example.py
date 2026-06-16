#!/usr/bin/env python3
# coding: utf-8
"""
FRAME COMPONENT - HALO THEME
=============================
Frames are container widgets used to organize and group other widgets.
They help structure your GUI into logical sections.

KEY FEATURES:
- Group related widgets together
- Create layout structure
- Apply styling to widget groups
- Nest frames for complex layouts
- Support for borders and relief styles
- Scrollable frames for overflow content
"""

from tkinter import *
from tkinter import ttk

HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_RED = "#ff1744"
HALO_GOLD = "#ffd700"
HALO_DARK = "#0a0e1a"
HALO_GRAY = "#2d3436"
HALO_LIGHT_GRAY = "#636e72"

# Create main window with scrollable content
root = Tk()
root.title("🎮 Frame Component - Halo Theme")
root.geometry("900x750")
root.configure(bg=HALO_DARK)

# ============================================================================
# CREATE MAIN SCROLLABLE CONTAINER
# ============================================================================

# Create main canvas with scrollbar
main_canvas = Canvas(root, bg=HALO_DARK, highlightthickness=0)
main_scrollbar = Scrollbar(root, orient="vertical", command=main_canvas.yview)
scrollable_frame = Frame(main_canvas, bg=HALO_DARK)

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
)

main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
main_canvas.configure(yscrollcommand=main_scrollbar.set)

main_canvas.pack(side="left", fill="both", expand=True)
main_scrollbar.pack(side="right", fill="y")

# Enable mouse wheel scrolling
def on_mousewheel(event):
    main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

main_canvas.bind_all("<MouseWheel>", on_mousewheel)

# Now use scrollable_frame instead of root for all content
container = scrollable_frame

# ============================================================================
# HEADER
# ============================================================================
Label(container, text="🎮 FRAME COMPONENT EXAMPLES 🎮", font=("Arial", 22, "bold"),
      fg=HALO_BLUE, bg=HALO_DARK, pady=15).pack()

Label(container, text="📦 Scrollable Content with Enhanced Icons", font=("Arial", 11),
      fg=HALO_GREEN, bg=HALO_DARK).pack()

# ============================================================================
# EXAMPLE 1: Basic Frame with Icons
# ============================================================================
Label(container, text="📋 EXAMPLE 1: Basic Frame with Icons", font=("Arial", 13, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

basic_frame = Frame(container, bg=HALO_GRAY, padx=20, pady=15, relief=RAISED, borderwidth=2)
basic_frame.pack(pady=5)

Label(basic_frame, text="📌 This is inside a frame", fg="white", 
      bg=HALO_GRAY, font=("Arial", 11)).pack()
Button(basic_frame, text="🚀 Launch", bg=HALO_BLUE, fg="white", 
       font=("Arial", 10, "bold")).pack(pady=5)

# ============================================================================
# EXAMPLE 2: Frame with Border/Relief Styles
# ============================================================================
Label(container, text="🎨 EXAMPLE 2: Frames with Different Border Styles", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

borders_container = Frame(container, bg=HALO_DARK)
borders_container.pack(pady=5)

relief_styles = [
    (FLAT, "FLAT", "⬜"),
    (RAISED, "RAISED", "🔼"),
    (SUNKEN, "SUNKEN", "🔽"),
    (GROOVE, "GROOVE", "📊"),
    (RIDGE, "RIDGE", "🎚️")
]

for relief_style, name, icon in relief_styles:
    frame = Frame(
        borders_container,
        bg=HALO_LIGHT_GRAY,
        relief=relief_style,
        borderwidth=4,
        padx=15,
        pady=10
    )
    frame.pack(side=LEFT, padx=5)
    Label(frame, text=f"{icon}\n{name}", bg=HALO_LIGHT_GRAY, fg="white", 
          font=("Arial", 9, "bold")).pack()

# ============================================================================
# EXAMPLE 3: Nested Frames (Two-Panel Layout)
# ============================================================================
Label(container, text="🔲 EXAMPLE 3: Nested Frames (Two-Panel Layout)", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

# Main container frame
main_container = Frame(container, bg=HALO_DARK, padx=10, pady=10)
main_container.pack(fill=BOTH, expand=True, padx=20)

# Left panel
left_panel = Frame(main_container, bg=HALO_GRAY, padx=15, pady=15, 
                   relief=RIDGE, borderwidth=3)
left_panel.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

Label(left_panel, text="⬅️ LEFT PANEL", font=("Arial", 12, "bold"),
      fg=HALO_BLUE, bg=HALO_GRAY).pack()
Label(left_panel, text="🎮 Controls Section", fg="white", bg=HALO_GRAY,
      font=("Arial", 10)).pack(pady=5)
Button(left_panel, text="🛡️ Shields", bg=HALO_BLUE, fg="white", 
       font=("Arial", 10, "bold"), width=18).pack(pady=3)
Button(left_panel, text="🔫 Weapons", bg=HALO_RED, fg="white", 
       font=("Arial", 10, "bold"), width=18).pack(pady=3)
Button(left_panel, text="⚙️ Settings", bg=HALO_GREEN, fg="black", 
       font=("Arial", 10, "bold"), width=18).pack(pady=3)
Button(left_panel, text="📡 Radar", bg=HALO_GOLD, fg="black", 
       font=("Arial", 10, "bold"), width=18).pack(pady=3)

# Right panel
right_panel = Frame(main_container, bg=HALO_GRAY, padx=15, pady=15,
                    relief=RIDGE, borderwidth=3)
right_panel.pack(side=RIGHT, fill=BOTH, expand=True, padx=5)

Label(right_panel, text="➡️ RIGHT PANEL", font=("Arial", 12, "bold"),
      fg=HALO_GREEN, bg=HALO_GRAY).pack()
Label(right_panel, text="ℹ️ Information Section", fg="white", bg=HALO_GRAY,
      font=("Arial", 10)).pack(pady=5)

# Nested frame inside right panel
info_frame = Frame(right_panel, bg=HALO_DARK, relief=SUNKEN, borderwidth=2, padx=10, pady=10)
info_frame.pack(pady=10, fill=X)

Label(info_frame, text="🆔 Spartan ID: 117", fg=HALO_BLUE, bg=HALO_DARK, 
      anchor=W, font=("Arial", 10)).pack(fill=X, pady=2)
Label(info_frame, text="✅ Status: Active", fg=HALO_GREEN, bg=HALO_DARK, 
      anchor=W, font=("Arial", 10)).pack(fill=X, pady=2)
Label(info_frame, text="🎯 Mission: Complete", fg=HALO_GOLD, bg=HALO_DARK, 
      anchor=W, font=("Arial", 10)).pack(fill=X, pady=2)
Label(info_frame, text="📍 Location: Installation 04", fg="white", bg=HALO_DARK, 
      anchor=W, font=("Arial", 10)).pack(fill=X, pady=2)

# ============================================================================
# EXAMPLE 4: Scrollable Frame with Many Items
# ============================================================================
Label(container, text="📜 EXAMPLE 4: Scrollable Frame (Many Items)", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

# Create frame with scrollbar
scroll_outer = Frame(container, bg=HALO_GRAY, relief=RIDGE, borderwidth=3)
scroll_outer.pack(pady=5, padx=20, fill=BOTH)

Label(scroll_outer, text="👇 Scroll to see all items", fg=HALO_GREEN, 
      bg=HALO_GRAY, font=("Arial", 10, "italic")).pack(pady=5)

# Scrollable area
scroll_canvas = Canvas(scroll_outer, bg=HALO_DARK, height=200, highlightthickness=0)
scroll_scrollbar = Scrollbar(scroll_outer, orient="vertical", command=scroll_canvas.yview)
scroll_content = Frame(scroll_canvas, bg=HALO_DARK)

scroll_content.bind(
    "<Configure>",
    lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))
)

scroll_canvas.create_window((0, 0), window=scroll_content, anchor="nw")
scroll_canvas.configure(yscrollcommand=scroll_scrollbar.set)

scroll_canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scroll_scrollbar.pack(side="right", fill="y")

# Add many items with icons
weapons_icons = ["🔫", "🗡️", "💣", "🚀", "⚔️", "🔨", "🏹", "🛡️", "⚡", "🔥", 
                 "❄️", "💥", "✨", "🌟", "💫", "⭐", "🎯", "🎪", "🎭", "🎨"]

for i, icon in enumerate(weapons_icons, 1):
    item_frame = Frame(scroll_content, bg=HALO_LIGHT_GRAY, relief=RAISED, 
                      borderwidth=1, padx=10, pady=8)
    item_frame.pack(fill=X, pady=2, padx=5)
    
    Label(item_frame, text=f"{icon} Weapon #{i}: Halo Arsenal", 
          fg="white", bg=HALO_LIGHT_GRAY, font=("Arial", 10), 
          anchor=W).pack(side=LEFT, fill=X, expand=True)
    
    Button(item_frame, text="⚙️", bg=HALO_BLUE, fg="white", 
           font=("Arial", 8), width=3).pack(side=RIGHT, padx=2)

# ============================================================================
# EXAMPLE 5: Frame with Grid Layout
# ============================================================================
Label(container, text="📊 EXAMPLE 5: Frame with Grid Layout", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

grid_frame = Frame(container, bg=HALO_GRAY, padx=20, pady=15, relief=GROOVE, borderwidth=3)
grid_frame.pack(pady=5, padx=20, fill=X)

Label(grid_frame, text="🔫 WEAPON STATISTICS", font=("Arial", 12, "bold"),
      fg=HALO_BLUE, bg=HALO_GRAY).grid(row=0, column=0, columnspan=2, pady=10)

stats = [
    ("💥 Damage:", "47", HALO_RED),
    ("📏 Range:", "Medium", HALO_BLUE),
    ("🎯 Accuracy:", "85%", HALO_GREEN),
    ("⚡ Fire Rate:", "Auto", HALO_GOLD),
    ("📦 Capacity:", "32 rounds", "white"),
    ("🔄 Reload:", "2.5s", "white")
]

for i, (label, value, color) in enumerate(stats, start=1):
    Label(grid_frame, text=label, fg="white", bg=HALO_GRAY, 
          font=("Arial", 10), anchor=W, width=15).grid(row=i, column=0, sticky=W, pady=3)
    Label(grid_frame, text=value, fg=color, bg=HALO_GRAY, 
          font=("Arial", 10, "bold"), anchor=W).grid(row=i, column=1, sticky=W, pady=3, padx=10)

# ============================================================================
# EXAMPLE 6: Colored Section Frames with Icons
# ============================================================================
Label(container, text="🎨 EXAMPLE 6: Colored Section Frames", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

sections_container = Frame(container, bg=HALO_DARK)
sections_container.pack(pady=5)

# Shields section
shields_frame = Frame(sections_container, bg=HALO_BLUE, padx=20, pady=12, 
                      relief=RAISED, borderwidth=3)
shields_frame.pack(side=LEFT, padx=5)
Label(shields_frame, text="🛡️", font=("Arial", 20),
      fg="white", bg=HALO_BLUE).pack()
Label(shields_frame, text="SHIELDS", font=("Arial", 10, "bold"),
      fg="white", bg=HALO_BLUE).pack()
Label(shields_frame, text="100%", font=("Arial", 16, "bold"),
      fg="white", bg=HALO_BLUE).pack()

# Health section
health_frame = Frame(sections_container, bg=HALO_GREEN, padx=20, pady=12,
                     relief=RAISED, borderwidth=3)
health_frame.pack(side=LEFT, padx=5)
Label(health_frame, text="❤️", font=("Arial", 20),
      fg="black", bg=HALO_GREEN).pack()
Label(health_frame, text="HEALTH", font=("Arial", 10, "bold"),
      fg="black", bg=HALO_GREEN).pack()
Label(health_frame, text="85%", font=("Arial", 16, "bold"),
      fg="black", bg=HALO_GREEN).pack()

# Ammo section
ammo_frame = Frame(sections_container, bg=HALO_RED, padx=20, pady=12,
                   relief=RAISED, borderwidth=3)
ammo_frame.pack(side=LEFT, padx=5)
Label(ammo_frame, text="🔫", font=("Arial", 20),
      fg="white", bg=HALO_RED).pack()
Label(ammo_frame, text="AMMO", font=("Arial", 10, "bold"),
      fg="white", bg=HALO_RED).pack()
Label(ammo_frame, text="32/128", font=("Arial", 16, "bold"),
      fg="white", bg=HALO_RED).pack()

# Score section
score_frame = Frame(sections_container, bg=HALO_GOLD, padx=20, pady=12,
                    relief=RAISED, borderwidth=3)
score_frame.pack(side=LEFT, padx=5)
Label(score_frame, text="⭐", font=("Arial", 20),
      fg="black", bg=HALO_GOLD).pack()
Label(score_frame, text="SCORE", font=("Arial", 10, "bold"),
      fg="black", bg=HALO_GOLD).pack()
Label(score_frame, text="9,999", font=("Arial", 16, "bold"),
      fg="black", bg=HALO_GOLD).pack()

# ============================================================================
# EXAMPLE 7: Card-Style Frames
# ============================================================================
Label(container, text="🃏 EXAMPLE 7: Card-Style Frames", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

cards_container = Frame(container, bg=HALO_DARK)
cards_container.pack(pady=10, padx=20, fill=X)

cards_data = [
    ("👤", "Spartans", "117", HALO_BLUE),
    ("🎯", "Missions", "42", HALO_GREEN),
    ("💀", "Eliminations", "1,337", HALO_RED),
    ("🏆", "Victories", "89", HALO_GOLD)
]

for icon, title, value, color in cards_data:
    card = Frame(cards_container, bg=HALO_GRAY, relief=RAISED, borderwidth=2, 
                 padx=15, pady=15)
    card.pack(side=LEFT, padx=5, expand=True, fill=BOTH)
    
    Label(card, text=icon, font=("Arial", 28), fg=color, bg=HALO_GRAY).pack()
    Label(card, text=title, font=("Arial", 10), fg="white", bg=HALO_GRAY).pack()
    Label(card, text=value, font=("Arial", 18, "bold"), fg=color, bg=HALO_GRAY).pack()

# ============================================================================
# EXAMPLE 8: Horizontal Scrollable Frame
# ============================================================================
Label(container, text="↔️ EXAMPLE 8: Horizontal Scrollable Frame", 
      font=("Arial", 13, "bold"), fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(20, 5))

h_scroll_outer = Frame(container, bg=HALO_GRAY, relief=RIDGE, borderwidth=3)
h_scroll_outer.pack(pady=5, padx=20, fill=X)

Label(h_scroll_outer, text="👈 Scroll horizontally to see all items 👉", 
      fg=HALO_GREEN, bg=HALO_GRAY, font=("Arial", 10, "italic")).pack(pady=5)

# Horizontal scrollable area
h_scroll_canvas = Canvas(h_scroll_outer, bg=HALO_DARK, height=120, highlightthickness=0)
h_scroll_scrollbar = Scrollbar(h_scroll_outer, orient="horizontal", command=h_scroll_canvas.xview)
h_scroll_content = Frame(h_scroll_canvas, bg=HALO_DARK)

h_scroll_content.bind(
    "<Configure>",
    lambda e: h_scroll_canvas.configure(scrollregion=h_scroll_canvas.bbox("all"))
)

h_scroll_canvas.create_window((0, 0), window=h_scroll_content, anchor="nw")
h_scroll_canvas.configure(xscrollcommand=h_scroll_scrollbar.set)

h_scroll_canvas.pack(side="top", fill="both", expand=True, padx=5, pady=5)
h_scroll_scrollbar.pack(side="bottom", fill="x", padx=5, pady=5)

# Add items horizontally
map_icons = ["🗺️", "🏔️", "🏝️", "🏜️", "🌋", "🏰", "🏛️", "🗼", "🌉", "🎡"]
map_names = ["Blood Gulch", "Lockout", "Guardian", "Valhalla", "The Pit", 
             "Sandtrap", "High Ground", "Zanzibar", "Last Resort", "Sidewinder"]

for icon, name in zip(map_icons, map_names):
    map_card = Frame(h_scroll_content, bg=HALO_LIGHT_GRAY, relief=RAISED, 
                     borderwidth=2, padx=15, pady=10)
    map_card.pack(side=LEFT, padx=5)
    
    Label(map_card, text=icon, font=("Arial", 24), 
          fg=HALO_BLUE, bg=HALO_LIGHT_GRAY).pack()
    Label(map_card, text=name, font=("Arial", 9, "bold"), 
          fg="white", bg=HALO_LIGHT_GRAY).pack()

# ============================================================================
# OPTIONS REFERENCE
# ============================================================================
reference_frame = Frame(container, bg=HALO_DARK, pady=20)
reference_frame.pack(padx=20, fill=X)

Label(reference_frame, text="📚 COMMON FRAME OPTIONS", 
      font=("Arial", 12, "bold", "underline"), fg=HALO_GREEN, bg=HALO_DARK).pack()

options_text = """📌 Basic Options:
  bg/background - Background color
  padx/pady - Internal padding (space inside frame)
  relief - Border style (FLAT, RAISED, SUNKEN, GROOVE, RIDGE)
  borderwidth - Border thickness
  width/height - Frame size in pixels

📦 Packing Options:
  fill - BOTH, X, Y, NONE (how frame expands)
  expand - True/False (whether frame grows to fill space)
  side - TOP, BOTTOM, LEFT, RIGHT (position in parent)
  
📜 Scrollable Frame:
  Use Canvas + Scrollbar + Frame pattern
  Bind <Configure> event to update scroll region
  Configure xscrollcommand/yscrollcommand for scrollbar sync"""

Label(reference_frame, text=options_text, font=("Courier", 9), fg="white",
      bg=HALO_DARK, justify=LEFT).pack(pady=10)

# Footer
Label(container, text="🎮 Finish the fight! 🎮", font=("Arial", 14, "bold"),
      fg=HALO_BLUE, bg=HALO_DARK, pady=20).pack()

root.mainloop()
