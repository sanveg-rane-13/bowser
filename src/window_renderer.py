import tkinter as tk


HSTEP, VSTEP = 13, 18
SCROLL_STEP = 100

class WindowRenderer():

    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 800
        self.OFFSET = 50
        self.scroll = 0

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()

        # bind scrolling
        self.window.bind("<Up>", self.scroll_up)
        self.window.bind("<Down>", self.scroll_down)


    def launch_window(self):
        self.window.mainloop()

    
    def load_webpage(self, content):
        self.display_list = self.__create_layout__(content)
        self.__draw__()


    def scroll_up(self, event):
        self.scroll -= SCROLL_STEP
        self.__draw__()


    def scroll_down(self, event):
        self.scroll += SCROLL_STEP
        self.__draw__()

    # === inner implementations ===

    def __draw__(self):
        self.canvas.delete("all")
        for x, y, item in self.display_list:
            if y > self.scroll + self.HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=item)


    def __create_layout__(self, content):
        cursor_x, cursor_y = HSTEP, VSTEP
        display_list = []

        for item in content:
            display_list.append((cursor_x, cursor_y, item))
            cursor_x += HSTEP

            if cursor_x >= self.WIDTH - HSTEP:
                cursor_y += VSTEP
                cursor_x = HSTEP

        return display_list


    