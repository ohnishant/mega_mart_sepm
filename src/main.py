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
    
    def _clear_contents(self) -> None:
        for child in self.winfo_children():
            child.destroy()

    def draw_login(self):
        self._clear_contents()
        loginFrame = screens.login.Login(self, self.draw_checkout, bg_color="Green")
        loginFrame.pack(fill = "both", expand = True)
    
    # TODO 
    def draw_checkout(self):
        self._clear_contents()
        print("Drawing checkout screen")
        self.button_logout: ctk.CTkButton = ctk.CTkButton(self,text="Log Out", command=self.draw_login)
        self.button_logout.pack()


if __name__ == "__main__":
    app = App()
    app.title("Mega Mart Self Checkout System")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
