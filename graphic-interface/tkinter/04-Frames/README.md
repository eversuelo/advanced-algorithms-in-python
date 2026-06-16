# Frame Component

## 📋 Overview

**Frame** is a container widget used to organize and group other widgets. It's essential for creating structured, well-organized GUI layouts. Frames can also be made scrollable for content that exceeds the visible area.

## 🎯 Use Cases

- Group related widgets (form sections, control panels)
- Create multi-panel layouts (sidebar + content)
- Add visual separation between sections
- Apply common styling to widget groups
- Structure complex interfaces
- **Create scrollable content areas**
- **Display large lists or grids**

## 🔧 Basic Syntax

```python
from tkinter import *

root = Tk()

# Create a frame
frame = Frame(root, bg="gray", padx=10, pady=10)
frame.pack()

# Add widgets to the frame
Label(frame, text="Inside frame").pack()
Button(frame, text="Click").pack()

root.mainloop()
```

## ⚙️ Common Options

| Option              | Description      | Example Values                                |
| ------------------- | ---------------- | --------------------------------------------- |
| `bg` / `background` | Background color | `"white"`, `"#f0f0f0"`                        |
| `padx` / `pady`     | Internal padding | `10`, `(5, 10)`                               |
| `relief`            | Border style     | `FLAT`, `RAISED`, `SUNKEN`, `GROOVE`, `RIDGE` |
| `borderwidth`       | Border thickness | `2`, `5`                                      |
| `width` / `height`  | Size in pixels   | `300`, `200`                                  |

## 📜 Scrollable Frame Pattern

Creating a scrollable frame requires combining a **Canvas**, **Scrollbar**, and **Frame**:

### Vertical Scrollable Frame

```python
from tkinter import *

root = Tk()

# Create canvas with scrollbar
canvas = Canvas(root, bg="white")
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white")

# Configure scrolling
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack elements
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add many widgets to scrollable_frame
for i in range(50):
    Label(scrollable_frame, text=f"Item {i}").pack()

# Enable mouse wheel
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mousewheel)

root.mainloop()
```

### Horizontal Scrollable Frame

```python
canvas = Canvas(root, height=150, bg="white")
scrollbar = Scrollbar(root, orient="horizontal", command=canvas.xview)
scrollable_frame = Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(xscrollcommand=scrollbar.set)

canvas.pack(side="top", fill="both", expand=True)
scrollbar.pack(side="bottom", fill="x")
```

## 🎭 Using Emojis and Icons

### Common Useful Emojis

| Category        | Emojis                  |
| --------------- | ----------------------- |
| **Status**      | ✅ ❌ ⚠️ ℹ️ 📌          |
| **UI Elements** | 📋 📊 📈 📉 🔍 ⚙️       |
| **Actions**     | ▶️ ⏸️ ⏹️ 🔄 ⬆️ ⬇️ ➡️ ⬅️ |
| **Gaming**      | 🎮 🎯 🏆 ⭐ 💫 ⚡ 🔥    |
| **Weapons**     | 🔫 🗡️ ⚔️ 🏹 💣 🚀       |
| **Stats**       | ❤️ 🛡️ 💪 📦             |
| **Maps**        | 🗺️ 🏔️ 🏝️ 🏜️ 🌋 🏰       |

```python
# Use emojis in labels
Label(frame, text="🛡️ Shields Active", font=("Arial", 12))
Label(frame, text="❤️ Health: 100%", fg="green")
```

## 🎮 Halo Theme Examples

### Scrollable Weapon List

```python
# Outer container
weapon_panel = Frame(root, bg="#2d3436", relief=RIDGE, borderwidth=3)
weapon_panel.pack(fill=BOTH, expand=True)

# Scrollable canvas
canvas = Canvas(weapon_panel, bg="#0a0e1a", height=300)
scrollbar = Scrollbar(weapon_panel, command=canvas.yview)
items_frame = Frame(canvas, bg="#0a0e1a")

items_frame.bind("<Configure>",
                 lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=items_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add weapons with icons
weapons = ["🔫 Assault Rifle", "🗡️ Energy Sword", "🚀 Rocket Launcher"]
for weapon in weapons:
    Label(items_frame, text=weapon, fg="#00a8ff", bg="#0a0e1a").pack(pady=5)
```

## 💡 Pro Tips

1. **Scrollable frames** for dynamic content - see pattern above
2. **Emojis for visual clarity**: `Label(frame, text="🔥 Critical", fg="red")`
3. **Card-style layouts** with relief and padding
4. **Nested frames** for complex structures

## ⚠️ Common Mistakes

1. **Forgetting to pack/grid**: Frames won't show without geometry manager
2. **Size not working**: Use `pack(fill=BOTH, expand=True)`
3. **Scrollbar not syncing**: Configure `yscrollcommand` and `scrollregion`
4. **Canvas not expanding**: Set `fill="both"` and `expand=True`

---

Run `example.py` to see **8 examples** including scrollable frames! 🚀
