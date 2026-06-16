# 🎮 Tkinter Components Quick Reference - Halo Theme

## 📚 Component Status

✅ **Completed Components:**

- `01-Labels` - Display text and images
- `02-Buttons` - Interactive clickable elements
- `03-Entry` - Single-line text input
- `04-Frames` - Container for organizing widgets

📝 **Additional Components Available in main.py:**

- Checkbuttons - Multiple on/off toggles
- Radiobuttons - Single selection from options
- Scale - Numeric slider
- Listbox - Scrollable item list
- Text Widget - Multi-line text area
- Canvas - Drawing and graphics
- Menu - Menu bars and dropdowns
- MessageBox - Dialog boxes

## 🚀 Quick Start Guide

### 1. Basic Window Setup

```python
from tkinter import *

root = Tk()
root.title("My App")
root.geometry("800x600")
root.configure(bg="#0a0e1a")

# Add widgets here

root.mainloop()
```

### 2. Component Cheat Sheet

| Component       | Purpose       | Basic Code                                           |
| --------------- | ------------- | ---------------------------------------------------- |
| **Label**       | Display text  | `Label(root, text="Hello")`                          |
| **Button**      | Click action  | `Button(root, text="Click", command=func)`           |
| **Entry**       | Text input    | `Entry(root, width=30)`                              |
| **Frame**       | Container     | `Frame(root, bg="gray")`                             |
| **Checkbutton** | Toggle        | `Checkbutton(root, text="Option", variable=var)`     |
| **Radiobutton** | Single choice | `Radiobutton(root, text="A", variable=var, value=1)` |
| **Listbox**     | Item list     | `Listbox(root, height=10)`                           |
| **Text**        | Multi-line    | `Text(root, height=10, width=40)`                    |
| **Scale**       | Slider        | `Scale(root, from_=0, to=100)`                       |
| **Canvas**      | Drawing       | `Canvas(root, width=400, height=300)`                |

### 3. Layout Managers

**Pack** - Simple stacking

```python
widget.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)
```

**Grid** - Table layout

```python
widget.grid(row=0, column=0, sticky=W, padx=5, pady=5)
```

**Place** - Absolute positioning

```python
widget.place(x=100, y=50, width=200, height=30)
```

### 4. Common Patterns

**Get user input:**

```python
entry = Entry(root)
entry.pack()

def submit():
    value = entry.get()
    print(value)

Button(root, text="Submit", command=submit).pack()
```

**Toggle button state:**

```python
state = False

def toggle():
    global state
    state = not state
    btn.config(bg="green" if state else "red")

btn = Button(root, text="Toggle", command=toggle)
```

**Update label dynamically:**

```python
label = Label(root, text="Count: 0")
label.pack()

count = 0

def increment():
    global count
    count += 1
    label.config(text=f"Count: {count}")

Button(root, text="+1", command=increment).pack()
```

## 🎨 Halo Theme Colors

```python
HALO_BLUE = "#00a8ff"    # Shields, primary actions
HALO_GREEN = "#76ff03"   # Health, success states
HALO_RED = "#ff1744"     # Danger, weapons
HALO_GOLD = "#ffd700"    # Highlights, headers
HALO_DARK = "#0a0e1a"    # Background
HALO_GRAY = "#2d3436"    # Panels, secondary
```

## 🔧 Common Widget Options

### All Widgets

- `bg` / `background` - Background color
- `fg` / `foreground` - Foreground/text color
- `font` - Font tuple: `("Arial", 12, "bold")`
- `padx` / `pady` - Padding
- `relief` - Border style: `FLAT`, `RAISED`, `SUNKEN`, `GROOVE`, `RIDGE`
- `borderwidth` - Border thickness

### Text Widgets (Label, Button, Entry)

- `text` - Display text
- `textvariable` - StringVar for binding
- `justify` - Alignment: `LEFT`, `CENTER`, `RIGHT`
- `anchor` - Position: `N`, `S`, `E`, `W`, `NE`, `NW`, `SE`, `SW`, `CENTER`
- `width` / `height` - Size

## ⌨️ Keyboard & Mouse Bindings

```python
# Click events
widget.bind("<Button-1>", function)  # Left click
widget.bind("<Button-3>", function)  # Right click
widget.bind("<Double-Button-1>", function)  # Double click

# Keyboard events
widget.bind("<Return>", function)    # Enter key
widget.bind("<Escape>", function)    # Escape key
widget.bind("<KeyPress>", function)  # Any key
widget.bind("<KeyRelease>", function)  # Key release

# Mouse motion
widget.bind("<Motion>", function)    # Mouse move
widget.bind("<Enter>", function)     # Mouse enter widget
widget.bind("<Leave>", function)     # Mouse leave widget
```

## 💾 Saving User Data

```python
# Using StringVar
name_var = StringVar()
Entry(root, textvariable=name_var).pack()

# Later access
current_name = name_var.get()
name_var.set("New Name")
```

## 🎓 Learning Resources

1. **Start Here**: Run each component's `example.py` file
2. **Reference**: Read component `README.md` files
3. **Complete App**: Study `main.py` for integrated example
4. **Practice**: Modify examples to learn

## 📖 Example Project Ideas

1. **Login Screen** - Entry + Button + validation
2. **Calculator** - Buttons in grid + Entry for display
3. **Todo List** - Listbox + Entry + Add/Remove buttons
4. **Settings Panel** - Checkbuttons + Radiobuttons + Save button
5. **Drawing App** - Canvas + color buttons + clear button

## 🐛 Debugging Tips

1. **Widget not showing?** - Did you call `.pack()`, `.grid()`, or `.place()`?
2. **Button does nothing?** - Check `command=function` (no parentheses!)
3. **Can't get Entry text?** - Use `.get()` method
4. **Layout broken?** - Don't mix pack() and grid() in same parent
5. **Colors not working?** - Use quotes: `bg="blue"` or `bg="#0000ff"`

## 🎯 Next Steps

1. ✅ Complete the 4 basic components (Labels, Buttons, Entry, Frames)
2. 📝 Review `main.py` for advanced components
3. 🔨 Build a small project combining multiple components
4. 🚀 Experiment and customize!

---

**Finish the fight!** 🎮 Happy coding, Spartan!
