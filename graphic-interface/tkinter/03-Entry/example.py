#!/usr/bin/env python3
# coding: utf-8
"""
ENTRY COMPONENT - HALO THEME
=============================
Entry widgets are single-line text input fields for user data entry.

KEY FEATURES:
- Accept user text input
- Support for validation
- Can be masked for passwords
- Bindable to StringVar for automatic updates
- Supports cut/copy/paste operations
"""

from tkinter import *

HALO_BLUE = "#00a8ff"
HALO_GREEN = "#76ff03"
HALO_DARK = "#0a0e1a"
HALO_GOLD = "#ffd700"
HALO_GRAY = "#2d3436"

root = Tk()
root.title("Entry Component - Halo Theme")
root.geometry("650x750")
root.configure(bg=HALO_DARK)

output_label = Label(root, text="Enter data and press buttons to see results", 
                     font=("Courier", 10), fg=HALO_GREEN, bg=HALO_DARK, pady=10)
output_label.pack()

# ============================================================================
# EXAMPLE 1: Basic Entry
# ============================================================================
Label(root, text="EXAMPLE 1: Basic Entry", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

Label(root, text="Spartan Name:", fg="white", bg=HALO_DARK).pack()

basic_entry = Entry(root, font=("Arial", 12), width=30)
basic_entry.pack(pady=5)
basic_entry.insert(0, "Master Chief")  # Default value

def show_name():
    name = basic_entry.get()  # Get the text from entry
    output_label.config(text=f"Spartan Name: {name}")

Button(root, text="Submit Name", command=show_name, bg=HALO_BLUE, 
       fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ============================================================================
# EXAMPLE 2: Entry with StringVar (Two-way Binding)
# ============================================================================
Label(root, text="EXAMPLE 2: Entry with StringVar", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

Label(root, text="Weapon Name:", fg="white", bg=HALO_DARK).pack()

weapon_var = StringVar(value="Assault Rifle")

weapon_entry = Entry(root, textvariable=weapon_var, font=("Arial", 12), width=30)
weapon_entry.pack(pady=5)

# Label automatically updates when StringVar changes
StringVar_label = Label(root, textvariable=weapon_var, fg=HALO_GREEN, 
                        bg=HALO_DARK, font=("Arial", 11))
StringVar_label.pack()

def update_weapon():
    weapon_var.set("Battle Rifle")  # Updates both entry and label

Button(root, text="Change to Battle Rifle", command=update_weapon, 
       bg=HALO_BLUE, fg="white").pack(pady=5)

# ============================================================================
# EXAMPLE 3: Password Entry (Hidden Text)
# ============================================================================
Label(root, text="EXAMPLE 3: Password Entry", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

Label(root, text="Enter Password:", fg="white", bg=HALO_DARK).pack()

password_entry = Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)

def check_password():
    pwd = password_entry.get()
    if pwd == "Cortana117":
        output_label.config(text="✅ Access Granted!", fg=HALO_GREEN)
    else:
        output_label.config(text="❌ Access Denied!", fg="red")

Button(root, text="Login", command=check_password, bg=HALO_GREEN, 
       fg="black", font=("Arial", 10, "bold")).pack(pady=5)

# ============================================================================
# EXAMPLE 4: Styled Entry with Validation
# ============================================================================
Label(root, text="EXAMPLE 4: Numeric Entry (Validation)", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

Label(root, text="Shield Level (0-100):", fg="white", bg=HALO_DARK).pack()

shield_entry = Entry(root, font=("Arial", 12), width=15, justify=CENTER,
                     bg="white", fg="black", relief=SUNKEN, borderwidth=2)
shield_entry.pack(pady=5)

def set_shield():
    try:
        level = int(shield_entry.get())
        if 0 <= level <= 100:
            output_label.config(text=f"🛡️ Shield set to {level}%", fg=HALO_BLUE)
        else:
            output_label.config(text="⚠️ Shield must be 0-100!", fg="yellow")
    except ValueError:
        output_label.config(text="❌ Please enter a number!", fg="red")

Button(root, text="Set Shield Level", command=set_shield, bg=HALO_BLUE, 
       fg="white", font=("Arial", 10, "bold")).pack(pady=5)

# ============================================================================
# EXAMPLE 5: Entry with Placeholder Text
# ============================================================================
Label(root, text="EXAMPLE 5: Entry with Placeholder", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

placeholder_entry = Entry(root, font=("Arial", 12), width=35, fg="gray")
placeholder_entry.pack(pady=5)

def add_placeholder(event=None):
    if placeholder_entry.get() == "":
        placeholder_entry.insert(0, "Enter coordinates (X, Y, Z)...")
        placeholder_entry.config(fg="gray")

def remove_placeholder(event):
    if placeholder_entry.get() == "Enter coordinates (X, Y, Z)...":
        placeholder_entry.delete(0, END)
        placeholder_entry.config(fg="black")

placeholder_entry.bind("<FocusIn>", remove_placeholder)
placeholder_entry.bind("<FocusOut>", add_placeholder)
add_placeholder()  # Set initial placeholder

def show_coordinates():
    coords = placeholder_entry.get()
    if coords and coords != "Enter coordinates (X, Y, Z)...":
        output_label.config(text=f"📍 Coordinates: {coords}")

Button(root, text="Set Coordinates", command=show_coordinates, 
       bg=HALO_GREEN, fg="black").pack(pady=5)

# ============================================================================
# EXAMPLE 6: Multiple Entries (Form)
# ============================================================================
Label(root, text="EXAMPLE 6: Form with Multiple Entries", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

form_frame = Frame(root, bg=HALO_GRAY, padx=20, pady=15)
form_frame.pack(pady=5)

# Create form fields
fields = ["Spartan ID:", "Rank:", "Assignment:", "Status:"]
entries = {}

for i, field in enumerate(fields):
    Label(form_frame, text=field, fg="white", bg=HALO_GRAY, 
          font=("Arial", 10), anchor=W, width=12).grid(row=i, column=0, sticky=W, pady=3)
    
    entry = Entry(form_frame, font=("Arial", 10), width=25)
    entry.grid(row=i, column=1, pady=3, padx=5)
    entries[field] = entry

# Set default values
entries["Spartan ID:"].insert(0, "117")
entries["Rank:"].insert(0, "Master Chief Petty Officer")
entries["Assignment:"].insert(0, "UNSC Forward Unto Dawn")
entries["Status:"].insert(0, "Active")

def submit_form():
    form_data = "\n".join([f"{field} {entry.get()}" for field, entry in entries.items()])
    output_label.config(text="📋 Form Submitted:\n" + form_data)

def clear_form():
    for entry in entries.values():
        entry.delete(0, END)
    output_label.config(text="Form cleared")

Button(form_frame, text="Submit Form", command=submit_form, bg=HALO_BLUE, 
       fg="white", font=("Arial", 10, "bold"), padx=10).grid(row=len(fields), column=0, pady=10)
Button(form_frame, text="Clear Form", command=clear_form, bg=HALO_GRAY, 
       fg="white", font=("Arial", 10), padx=10).grid(row=len(fields), column=1, pady=10)

# ============================================================================
# EXAMPLE 7: Entry with Real-time Validation
# ============================================================================
Label(root, text="EXAMPLE 7: Real-time Character Counter", font=("Arial", 12, "bold"),
      fg=HALO_GOLD, bg=HALO_DARK).pack(pady=(15, 5))

char_count_label = Label(root, text="0 / 50 characters", fg="white", bg=HALO_DARK)
char_count_label.pack()

realtime_entry = Entry(root, font=("Arial", 11), width=40)
realtime_entry.pack(pady=5)

def update_count(*args):
    text = realtime_entry.get()
    count = len(text)
    char_count_label.config(text=f"{count} / 50 characters")
    
    if count > 50:
        char_count_label.config(fg="red")
    elif count > 40:
        char_count_label.config(fg="yellow")
    else:
        char_count_label.config(fg=HALO_GREEN)

realtime_entry.bind("<KeyRelease>", update_count)

# ============================================================================
# OPTIONS REFERENCE
# ============================================================================
Label(root, text="COMMON ENTRY OPTIONS", font=("Arial", 11, "bold", "underline"),
      fg=HALO_GREEN, bg=HALO_DARK).pack(pady=(20, 5))

options_text = """textvariable - StringVar for two-way binding
show - Character to display (e.g., '*' for passwords)
width - Width in characters
font - Font configuration
fg/bg - Text/background color
justify - Text alignment (LEFT, CENTER, RIGHT)
state - NORMAL, DISABLED, READONLY
relief - Border style
borderwidth - Border thickness

Methods:
  .get() - Retrieve text
  .insert(index, text) - Insert text at position
  .delete(start, end) - Delete text range"""

Label(root, text=options_text, font=("Courier", 9), fg="white", 
      bg=HALO_DARK, justify=LEFT).pack()

root.mainloop()
