# Entry Component

## 📋 Overview

**Entry** is a single-line text input widget that allows users to enter and edit text.

## 🎯 Use Cases

- User registration forms (name, email, password)
- Search boxes
- Numeric input fields
- Configuration settings
- Login credentials

## 🔧 Basic Syntax

```python
from tkinter import *

root = Tk()

entry = Entry(root, font=("Arial", 12), width=30)
entry.pack()

# Get the text
text = entry.get()

# Set text
entry.insert(0, "Default text")

# Clear text
entry.delete(0, END)

root.mainloop()
```

## ⚙️ Common Options

| Option         | Description                | Example Values                   |
| -------------- | -------------------------- | -------------------------------- |
| `textvariable` | StringVar for binding      | `StringVar()`                    |
| `show`         | Mask character (passwords) | `"*"`, `"•"`                     |
| `width`        | Width in characters        | `20`, `50`                       |
| `font`         | Font configuration         | `("Arial", 12)`                  |
| `fg` / `bg`    | Text/background color      | `"black"`, `"white"`             |
| `justify`      | Text alignment             | `LEFT`, `CENTER`, `RIGHT`        |
| `state`        | Entry state                | `NORMAL`, `DISABLED`, `READONLY` |
| `relief`       | Border style               | `SUNKEN`, `RAISED`, `FLAT`       |
| `borderwidth`  | Border thickness           | `2`, `5`                         |

## 🔍 Common Methods

### Get Text

```python
text = entry.get()  # Returns the current text
```

### Set/Insert Text

```python
entry.insert(0, "Hello")  # Insert at beginning
entry.insert(END, "!")    # Insert at end
```

### Delete Text

```python
entry.delete(0, END)       # Clear all text
entry.delete(0, 5)         # Delete first 5 characters
```

### Select Text

```python
entry.select_range(0, END)  # Select all text
entry.icursor(5)            # Place cursor at position 5
```

## 🔗 Using StringVar (Recommended)

```python
text_var = StringVar(value="Default")

entry = Entry(root, textvariable=text_var)

# Get value
current_text = text_var.get()

# Set value
text_var.set("New text")  # Automatically updates entry

# Bind to changes
def on_change(*args):
    print(f"Text changed to: {text_var.get()}")

text_var.trace_add("write", on_change)
```

## 🔐 Password Entry

```python
password_entry = Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

# Or use bullet points
password_entry = Entry(root, show="•")
```

## ✅ Validation Examples

### Numeric Only

```python
def validate_number(text):
    return text.isdigit() or text == ""

vcmd = (root.register(validate_number), '%P')
entry = Entry(root, validate='key', validatecommand=vcmd)
```

### Simple Validation

```python
def submit():
    text = entry.get()
    if not text:
        print("Entry is empty!")
    elif len(text) < 3:
        print("Too short!")
    else:
        print(f"Valid: {text}")
```

## 🎨 Placeholder Text

```python
entry = Entry(root, fg="gray")

def add_placeholder(event=None):
    if entry.get() == "":
        entry.insert(0, "Enter text...")
        entry.config(fg="gray")

def remove_placeholder(event):
    if entry.get() == "Enter text...":
        entry.delete(0, END)
        entry.config(fg="black")

entry.bind("<FocusIn>", remove_placeholder)
entry.bind("<FocusOut>", add_placeholder)
add_placeholder()
```

## ⌨️ Keyboard Bindings

```python
# Submit on Enter key
entry.bind("<Return>", lambda e: submit_form())

# Clear on Escape
entry.bind("<Escape>", lambda e: entry.delete(0, END))

# Real-time character count
def update_count(event):
    count = len(entry.get())
    label.config(text=f"{count} characters")

entry.bind("<KeyRelease>", update_count)
```

## 💡 Pro Tips

1. **Use `textvariable`** for reactive updates
2. **Validate input** before processing
3. **Clear sensitive data** after use:
   ```python
   password_entry.delete(0, END)
   ```
4. **Set focus** programmatically:
   ```python
   entry.focus_set()
   ```
5. **Disable editing** but allow copying:
   ```python
   entry.config(state=READONLY)
   ```

## 🎮 Halo Theme Examples

### Login Form

```python
Label(root, text="Spartan ID:", fg="white", bg="#0a0e1a").pack()
id_entry = Entry(root, font=("Arial", 12), width=25)
id_entry.pack()

Label(root, text="Password:", fg="white", bg="#0a0e1a").pack()
pwd_entry = Entry(root, show="*", font=("Arial", 12), width=25)
pwd_entry.pack()
```

### Styled Entry

```python
entry = Entry(
    root,
    font=("Arial", 12),
    width=30,
    bg="white",
    fg="black",
    relief=SUNKEN,
    borderwidth=2,
    justify=CENTER
)
```

## ⚠️ Common Mistakes

1. **Forgetting to `.get()`**: Use `entry.get()`, not just `entry`
2. **Wrong delete range**: Use `delete(0, END)` not `delete(END)`
3. **Setting text incorrectly**: Use `insert()`, not direct assignment

## 🔗 Related Components

- **Text** - Multi-line text input
- **Label** - Display-only text
- **Spinbox** - Numeric entry with up/down buttons

---

Run `example.py` to see all entry variations! 🚀
