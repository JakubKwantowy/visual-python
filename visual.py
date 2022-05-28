import libs.tkinter as tk

def create_window(
    title: str = "Visual Python (powered by tkinter)",
    width: int = 800, height: int = 600, x: int = 0, y: int = 0,
    bg: str = "#008080",
) -> tk.Tk:
    window = tk.Tk()
    window.title(title)
    window.geometry("{}x{}+{}+{}".format(width, height, x, y))
    window.config(bg=bg)
    return window

def destroy_window(window: tk.Tk):
    window.destroy()

def add_widget(window: tk.Tk, Widget: tk.Widget):
    return Widget(window)

def position_widget(widget: tk.Widget, x: int = 0, y: int = 0):
    widget.place(x=x, y=y)

def hide_widget(widget: tk.Widget):
    widget.place_forget()

def set_label_text(label: tk.Label, text: str = ""):
    label.config(text=text)