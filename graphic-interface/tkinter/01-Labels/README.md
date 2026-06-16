# Label Component

## 📋 Overview

**Label** is a widget used to display text or images. It's a read-only (non-interactive) component that shows information to the user.

## 🎯 Use Cases

- Display titles and headings
- Show status information
- Present instructions
- Display dynamic data (scores, stats, etc.)
- Add decorative text

## 🔧 Basic Syntax

```python
from tkinter import *

root = Tk()

label = Label(
    root,                    # Parent widget
    text="Hello, Spartan!",  # Text to display
    font=("Arial", 12),      # Font configuration
    fg="blue",               # Foreground (text) color
    bg="white"               # Background color
)

label.pack()  # Display the label

root.mainloop()
```

## ⚙️ Common Options

| Option              | Description               | Example Values                                |
| ------------------- | ------------------------- | --------------------------------------------- |
| `text`              | The text to display       | `"Hello World"`                               |
| `font`              | Font configuration        | `("Arial", 12, "bold")`                       |
| `fg` / `foreground` | Text color                | `"red"`, `"#ff0000"`                          |
| `bg` / `background` | Background color          | `"white"`, `"#ffffff"`                        |
| `padx` / `pady`     | External padding          | `10`, `(5, 10)`                               |
| `width` / `height`  | Widget size in characters | `20`, `5`                                     |
| `anchor`            | Text position             | `W`, `E`, `N`, `S`, `CENTER`                  |
| `justify`           | Multi-line text alignment | `LEFT`, `CENTER`, `RIGHT`                     |
| `relief`            | Border style              | `FLAT`, `RAISED`, `SUNKEN`, `GROOVE`, `RIDGE` |
| `borderwidth`       | Border thickness          | `1`, `5`                                      |
| `wraplength`        | Max line width (pixels)   | `200`                                         |

## 🎨 Styling Examples

### Bold Title

```python
title = Label(root, text="HALO", font=("Arial", 24, "bold"), fg="#00a8ff")
```

### Multi-line Text

```python
Label(root, text="Line 1\nLine 2\nLine 3", justify=LEFT)
```

### Bordered Label

```python
Label(root, text="Alert!", relief=RAISED, borderwidth=3)
```

## 🔄 Dynamic Updates

Labels can be updated after creation:

```python
label = Label(root, text="Score: 0")

def update_score(new_score):
    label.config(text=f"Score: {new_score}")  # Update text
    label.config(fg="green")                   # Update color
```

## 💡 Pro Tips

1. **Use `textvariable`** for automatic updates:

   ```python
   score = StringVar()
   Label(root, textvariable=score)
   score.set("100")  # Auto-updates label
   ```

2. **Emoji support** - Modern Python/tkinter supports emojis:

   ```python
   Label(root, text="🎮 Game Ready!")
   ```

3. **Color contrast** - Ensure text is readable against background

4. **Font families** - Common options: `"Arial"`, `"Courier"`, `"Times"`, `"Helvetica"`

## 🎮 Halo Theme Example

```python
HALO_BLUE = "#00a8ff"
HALO_DARK = "#0a0e1a"

Label(
    root,
    text="🛡️ SHIELDS ACTIVE",
    font=("Arial", 16, "bold"),
    fg=HALO_BLUE,
    bg=HALO_DARK,
    pady=15
)
```

## 🔗 Related Components

- **Button** - Interactive clickable element
- **Entry** - Text input field
- **Text** - Multi-line editable text

---

Run `example.py` to see all label variations in action! 🚀
