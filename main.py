import tkinter as tk
import random

class UncatchableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("You'll never catch me")
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True) # Keep it on top
        
        self.width, self.height = 200, 100
        self.root.geometry(f"{self.width}x{self.height}+100+100")
        
        # UI Setup
        self.label = tk.Label(root, text="Click if you can!", bg="red", fg="white", font=("Arial", 12))
        self.label.pack(expand=True, fill="both")
        
        # Bind the click event
        self.label.bind("<Button-1>", self.on_click)
        
        self.target_x = 100
        self.target_y = 100
        self.is_running = True
        self.move_window()

    def move_window(self):
        if not self.is_running: return
        
        mouse_x = self.root.winfo_pointerx()
        mouse_y = self.root.winfo_pointery()
        win_x, win_y = self.root.winfo_x(), self.root.winfo_y()

        # Fleeing logic
        if abs(mouse_x - (win_x + self.width/2)) < 120 and \
           abs(mouse_y - (win_y + self.height/2)) < 120:
            self.target_x = random.randint(0, self.root.winfo_screenwidth() - self.width)
            self.target_y = random.randint(0, self.root.winfo_screenheight() - self.height)

        # Smooth movement (Lerp)
        new_x = win_x + (self.target_x - win_x) * 0.2
        new_y = win_y + (self.target_y - win_y) * 0.2
        self.root.geometry(f"{self.width}x{self.height}+{int(new_x)}+{int(new_y)}")
        
        self.root.after(20, self.move_window)

    def on_click(self, event):
        self.is_running = False
        self.label.config(text="You caught me! \n Prize: Absolutely Nothing.", bg="blue")
        self.fade_out(1.0)

    def fade_out(self, alpha):
        if alpha > 0:
            alpha -= 0.05
            self.root.attributes('-alpha', alpha)
            self.root.after(50, lambda: self.fade_out(alpha))
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UncatchableApp(root)
    root.mainloop()