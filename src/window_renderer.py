import tkinter as tk

class WindowRenderer():

    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 800
        self.OFFSET = 50

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()


    def launch_window(self):
        self.window.mainloop()

    
    def load_webpage(self, content):
        HSTEP, VSTEP = 13, 18
        cursor_x, cursor_y = HSTEP, VSTEP

        for item in content:
            self.canvas.create_text(cursor_x, cursor_y, text=item)
            cursor_x += HSTEP

            if cursor_x >= self.WIDTH - HSTEP:
                cursor_y += VSTEP
                cursor_x = HSTEP