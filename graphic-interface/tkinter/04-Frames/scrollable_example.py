#!/usr/bin/env python3
"""
Halo-Themed Scrollable Frame Example
Demonstrates various scrolling techniques with Frames
"""

from tkinter import *

# ========================================
# METHOD 1: Canvas with Scrollbar (Most Common)
# ========================================

def create_scrollable_canvas_demo():
    """Vertical scrollable frame using Canvas"""
    window = Tk()
    window.title("Scrollable Frame - Canvas Method")
    window.geometry("400x500")
    window.configure(bg="#0a0e1a")
    
    # Create main container
    main_frame = Frame(window, bg="#0a0e1a")
    main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Create Canvas
    canvas = Canvas(main_frame, bg="#1a1f2e", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    # Add Scrollbar
    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Configure canvas to work with scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Create a frame INSIDE the canvas
    scrollable_frame = Frame(canvas, bg="#1a1f2e", padx=20, pady=20)
    
    # Add the frame to the canvas
    canvas_frame = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    # Title
    title = Label(
        scrollable_frame,
        text="⚔️ SPARTAN ROSTER ⚔️",
        font=("Arial", 16, "bold"),
        fg="#ffd700",
        bg="#1a1f2e"
    )
    title.pack(pady=(0, 20))
    
    # Add many items to demonstrate scrolling
    for i in range(50):
        spartan_card = Frame(
            scrollable_frame,
            bg="#2d3436",
            relief=RAISED,
            borderwidth=2,
            padx=15,
            pady=10
        )
        spartan_card.pack(fill=X, pady=5)
        
        Label(
            spartan_card,
            text=f"Spartan-{117 + i:03d}",
            font=("Arial", 10, "bold"),
            fg="#00a8ff",
            bg="#2d3436"
        ).pack(anchor=W)
        
        Label(
            spartan_card,
            text=f"Status: {'Active' if i % 3 else 'On Mission'}",
            fg="#76ff03" if i % 3 else "#ffab00",
            bg="#2d3436",
            font=("Arial", 8)
        ).pack(anchor=W)
    
    # Update scroll region when frame size changes
    def configure_scroll_region(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    scrollable_frame.bind("<Configure>", configure_scroll_region)
    
    # Mouse wheel scrolling
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    window.mainloop()


# ========================================
# METHOD 2: Horizontal & Vertical Scrolling
# ========================================

def create_dual_scroll_demo():
    """Frame with both horizontal and vertical scrolling"""
    window = Tk()
    window.title("Dual Scrolling - Both Directions")
    window.geometry("500x400")
    window.configure(bg="#0a0e1a")
    
    # Main container
    main_frame = Frame(window, bg="#0a0e1a")
    main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    
    # Canvas
    canvas = Canvas(main_frame, bg="#1a1f2e", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    # Vertical scrollbar
    v_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=RIGHT, fill=Y)
    
    # Horizontal scrollbar
    h_scrollbar = Scrollbar(window, orient=HORIZONTAL, command=canvas.xview)
    h_scrollbar.pack(side=BOTTOM, fill=X, padx=10)
    
    # Configure canvas
    canvas.configure(
        yscrollcommand=v_scrollbar.set,
        xscrollcommand=h_scrollbar.set
    )
    
    # Scrollable frame
    scrollable_frame = Frame(canvas, bg="#1a1f2e", padx=20, pady=20)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    
    # Title
    Label(
        scrollable_frame,
        text="🗺️ HALO RING MAP 🗺️",
        font=("Arial", 14, "bold"),
        fg="#ffd700",
        bg="#1a1f2e"
    ).grid(row=0, column=0, columnspan=10, pady=(0, 20))
    
    # Create a grid of locations (scrolls both ways)
    locations = [
        "Silent Cartographer", "Control Room", "Pillar of Autumn",
        "Alpha Base", "Delta Halo", "Installation 04",
        "Ark Portal", "Voi", "Crow's Nest", "The Storm"
    ]
    
    for i in range(15):
        for j in range(10):
            location_frame = Frame(
                scrollable_frame,
                bg="#2d3436",
                relief=RIDGE,
                borderwidth=2,
                width=150,
                height=100
            )
            location_frame.grid(row=i+1, column=j, padx=5, pady=5)
            location_frame.pack_propagate(False)
            
            Label(
                location_frame,
                text=locations[(i*j) % len(locations)],
                fg="#00a8ff",
                bg="#2d3436",
                wraplength=130,
                font=("Arial", 8)
            ).pack(expand=True)
    
    # Update scroll region
    scrollable_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Mouse wheel scrolling
    def on_vertical_scroll(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def on_horizontal_scroll(event):
        canvas.xview_scroll(int(-1*(event.delta/120)), "units")
    
    canvas.bind_all("<MouseWheel>", on_vertical_scroll)
    canvas.bind_all("<Shift-MouseWheel>", on_horizontal_scroll)
    
    window.mainloop()


# ========================================
# METHOD 3: Scrollable Frame Class (Reusable)
# ========================================

class ScrollableFrame(Frame):
    """Reusable scrollable frame widget"""
    
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        
        # Create canvas
        self.canvas = Canvas(self, bg=kwargs.get('bg', 'white'), highlightthickness=0)
        
        # Create scrollbars
        self.v_scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.h_scrollbar = Scrollbar(self, orient=HORIZONTAL, command=self.canvas.xview)
        
        # Create the scrollable frame
        self.scrollable_frame = Frame(self.canvas, bg=kwargs.get('bg', 'white'))
        
        # Configure canvas
        self.canvas.configure(
            yscrollcommand=self.v_scrollbar.set,
            xscrollcommand=self.h_scrollbar.set
        )
        
        # Pack scrollbars and canvas
        self.v_scrollbar.pack(side=RIGHT, fill=Y)
        self.h_scrollbar.pack(side=BOTTOM, fill=X)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Add frame to canvas
        self.canvas_frame = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )
        
        # Bind events
        self.scrollable_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        # Mouse wheel support
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _on_frame_configure(self, event=None):
        """Update scroll region when frame size changes"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _on_canvas_configure(self, event):
        """Resize frame to canvas width if needed"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")


def create_reusable_class_demo():
    """Demo using the reusable ScrollableFrame class"""
    window = Tk()
    window.title("Reusable Scrollable Frame Class")
    window.geometry("450x500")
    window.configure(bg="#0a0e1a")
    
    # Title
    title_frame = Frame(window, bg="#0a0e1a")
    title_frame.pack(fill=X, padx=10, pady=10)
    
    Label(
        title_frame,
        text="🎯 UNSC WEAPON INVENTORY 🎯",
        font=("Arial", 14, "bold"),
        fg="#ffd700",
        bg="#0a0e1a"
    ).pack()
    
    # Use the scrollable frame class
    scroll_frame = ScrollableFrame(window, bg="#1a1f2e")
    scroll_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
    
    # Add content to scroll_frame.scrollable_frame
    weapons = [
        ("MA5B Assault Rifle", "#76ff03", "Automatic"),
        ("BR55 Battle Rifle", "#00a8ff", "Burst Fire"),
        ("M6D Magnum", "#ffd700", "Semi-Auto"),
        ("SRS99 Sniper Rifle", "#ff1744", "Precision"),
        ("M90 Shotgun", "#ff6d00", "Close Range"),
        ("Rocket Launcher", "#d500f9", "Heavy"),
        ("Spartan Laser", "#00e5ff", "Energy"),
        ("DMR", "#76ff03", "Marksman"),
    ]
    
    for i in range(30):  # Many items to scroll
        weapon_name, color, weapon_type = weapons[i % len(weapons)]
        
        weapon_card = Frame(
            scroll_frame.scrollable_frame,
            bg="#2d3436",
            relief=RAISED,
            borderwidth=2,
            padx=20,
            pady=15
        )
        weapon_card.pack(fill=X, padx=10, pady=5)
        
        Label(
            weapon_card,
            text=f"{weapon_name} #{i+1:03d}",
            font=("Arial", 11, "bold"),
            fg=color,
            bg="#2d3436"
        ).pack(anchor=W)
        
        Label(
            weapon_card,
            text=f"Type: {weapon_type} | Ammo: {(i*7) % 100}",
            fg="#b0bec5",
            bg="#2d3436",
            font=("Arial", 8)
        ).pack(anchor=W)
    
    window.mainloop()


# ========================================
# MAIN MENU
# ========================================

def main():
    """Main menu to choose demo"""
    menu = Tk()
    menu.title("Scrollable Frame Examples")
    menu.geometry("400x350")
    menu.configure(bg="#0a0e1a")
    
    # Title
    Label(
        menu,
        text="📜 SCROLLABLE FRAMES 📜",
        font=("Arial", 16, "bold"),
        fg="#ffd700",
        bg="#0a0e1a"
    ).pack(pady=20)
    
    Label(
        menu,
        text="Choose a demo to run:",
        fg="#b0bec5",
        bg="#0a0e1a",
        font=("Arial", 10)
    ).pack(pady=10)
    
    # Buttons
    button_frame = Frame(menu, bg="#0a0e1a")
    button_frame.pack(expand=True)
    
    demos = [
        ("1. Vertical Scroll (Canvas)", create_scrollable_canvas_demo),
        ("2. Dual Scroll (H+V)", create_dual_scroll_demo),
        ("3. Reusable Class", create_reusable_class_demo),
    ]
    
    for text, command in demos:
        btn = Button(
            button_frame,
            text=text,
            command=command,
            bg="#2d3436",
            fg="#00a8ff",
            font=("Arial", 10, "bold"),
            width=30,
            height=2,
            relief=RAISED,
            borderwidth=2,
            activebackground="#00a8ff",
            activeforeground="#0a0e1a"
        )
        btn.pack(pady=8)
    
    menu.mainloop()


if __name__ == "__main__":
    main()
