from typing import Optional, Tuple, Union

import customtkinter as ctk
import screens.login


class App(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(fg_color, **kwargs)
        self.geometry("1366x768")
        self.minsize(1366, 768)
        self.draw_login()

    def draw_login(self):
        loginFrame = screens.login.Login(self, bg_color="Green")
        loginFrame.pack()


if __name__ == "__main__":
    app = App()
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
