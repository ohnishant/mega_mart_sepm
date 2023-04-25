from typing import Optional, Tuple, Union

import customtkinter as ctk

import screens.login
import screens.admin
import screens.checkout

import sqlite3
import os


class App(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ):
        super().__init__(fg_color, **kwargs)
        self.geometry("1366x768")
        self.minsize(1366, 768)
        self.cur = self._connect_to_db().cursor()
        self.draw_login()

    def _clear_contents(self) -> None:
        for child in self.winfo_children():
            child.destroy()

    @staticmethod
    def _connect_to_db() -> sqlite3.Connection:
        db_path = os.path.join(os.getcwd(), "db", "mega_mart_db.db")

        if os.path.exists(db_path):
            pass
        else:
            raise FileNotFoundError(
                "Couldn't find the database in ./db/mega_mart_db.db \nAre you running this from project root?"
            )

        return sqlite3.connect(database=db_path)
    
    def pre_login(self, user_type: str):
        if user_type == "admin":
            self.draw_admin()
        elif user_type == "customer":
            self.draw_checkout()
        else:
            raise ValueError("Invalid user type")

    def draw_login(self):
        self._clear_contents()
        loginFrame = screens.login.Login(self, fn_login= self.draw_checkout, fn_admin=self.draw_admin, bg_color="Green", db_cursor=self.cur)
        loginFrame.pack(fill="both", expand=True)

    def draw_admin(self):
        self._clear_contents()
        adminFrame = screens.admin.Admin(self, bg_color="Red")
        adminFrame.pack(fill="both", expand=True)

    # TODO
    def draw_checkout(self):
        self._clear_contents()
        print("Drawing checkout screen")
        checkoutFrame = screens.checkout.Checkout(self, db_cursor=self.cur)
        checkoutFrame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.title("Mega Mart Self Checkout System")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()