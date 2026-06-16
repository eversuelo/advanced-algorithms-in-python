# Button Component

## 📋 Overview

**Button** is an interactive widget that executes a function when clicked. It's the primary way users trigger actions in GUI applications.

## 🎯 Use Cases

- Trigger actions (submit, save, delete)
- Navigate between screens
- Toggle states (on/off, show/hide)
- Confirm or cancel operations
- Open dialogs or new windows

## 🔧 Basic Syntax

```python
from tkinter import *

root = Tk()

def button_clicked():
    print("Button was clicked!")

button = Button(
    root,
    text="Click Me",      # Button label
    command=button_clicked,  # Function to call
    bg="blue",            # Background color
    fg="white"            # Text color
)

button.pack()

root.mainloop()
```

## ⚙️ Common Options

| Option              | Description             | Example Values                 |
| ------------------- | ----------------------- | ------------------------------ |
| `text`              | Button label text       | `"Submit"`, `"Cancel"`         |
| `command`           | Function to execute     | `my_function`                  |
| `bg` / `background` | Background color        | `"blue"`, `"#0000ff"`          |
| `fg` / `foreground` | Text color              | `"white"`, `"#ffffff"`         |
| `font`              | Font configuration      | `("Arial", 12, "bold")`        |
| `padx` / `pady`     | Internal padding        | `10`, `15`                     |
| `width` / `height`  | Size in characters      | `15`, `3`                      |
| `state`             | Button state            | `NORMAL`, `DISABLED`, `ACTIVE` |
| `relief`            | Border style            | `FLAT`, `RAISED`, `SUNKEN`     |
| `borderwidth`       | Border thickness        | `2`, `5`                       |
| `activebackground`  | Color when clicked      | `"lightblue"`                  |
| `activeforeground`  | Text color when clicked | `"black"`                      |

## 🎨 Styling Examples

### Styled Button

```python
Button(
    root,
    text="🛡️ Activate Shields",
    command=activate_shields,
    bg="#00a8ff",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    relief=RAISED,
    borderwidth=3
)
```

### Flat Modern Button

```python
Button(root, text="Submit", bg="#4CAF50", fg="white", relief=FLAT, padx=30, pady=15)
```

## 🔄 Dynamic Button State

### Enable/Disable

```python
button = Button(root, text="Click Me", command=my_function)

# Disable button
button.config(state=DISABLED)

# Enable button
button.config(state=NORMAL)
```

### Change Appearance

```python
def toggle():
    if button['bg'] == 'red':
        button.config(bg='green', text='ON')
    else:
        button.config(bg='red', text='OFF')

button = Button(root, text='OFF', bg='red', command=toggle)
```

## 🎯 Command Patterns

### Simple Function

```python
def click_action():
    print("Clicked!")

Button(root, text="Click", command=click_action)
```

### Lambda with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

Button(root, text="Greet", command=lambda: greet("Spartan"))
```

### Multiple Buttons with Same Function

```python
def select_weapon(weapon):
    print(f"Selected: {weapon}")

for weapon in ["Rifle", "Shotgun", "Sniper"]:
    Button(
        root,
        text=weapon,
        command=lambda w=weapon: select_weapon(w)
    ).pack()
```

## 💡 Pro Tips

1. **Don't include `()` in command** - Use `command=my_function`, not `command=my_function()`

2. **Use lambda for parameters**:

   ```python
   # ❌ Wrong
   Button(root, text="Save", command=save_file(filename))

   # ✅ Correct
   Button(root, text="Save", command=lambda: save_file(filename))
   ```

3. **Bind Enter key** to button:

   ```python
   button.bind('<Return>', lambda e: button.invoke())
   ```

4. **Set default button**:

   ```python
   button.config(default=ACTIVE)  # Highlighted by default
   ```

5. **Use icons/emojis** for visual appeal:
   ```python
   Button(root, text="🔥 Fire", ...)
   ```

## 🎮 Halo Theme Examples

### Action Button

```python
Button(
    root,
    text="🔫 Fire Weapon",
    command=fire_weapon,
    bg="#ff1744",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8,
    relief=RAISED,
    borderwidth=3
)
```

### Toggle Button

```python
active = False

def toggle():
    global active
    active = not active
    if active:
        btn.config(bg="#76ff03", text="ON")
    else:
        btn.config(bg="#2d3436", text="OFF")

btn = Button(root, text="OFF", command=toggle)
```

## ⚠️ Common Mistakes

1. **Using `()` in command**: `command=func()` executes immediately, use `command=func`
2. **Lambda scope issues**: Always use default parameters: `lambda w=weapon: ...`
3. **Forgetting to pack/grid**: Button won't show without geometry manager

## 🔗 Related Components

- **Label** - Display-only text (no interaction)
- **Entry** - Text input field
- **Checkbutton** - On/off toggle
- **Radiobutton** - Multiple choice selection

---

Run `example.py` to see all button variations in action! 🚀
