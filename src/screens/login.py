from ast import Call
import os
from typing import Optional, Tuple, Union, Callable

from PIL import Image

import customtkinter as ctk
import os
import sqlite3


class Login(ctk.CTkFrame):
    fullscreen: bool = False
    """
    Login Frame:
    Contains the logic and widgets for login
    Arguments:
    master: The containing widget for the frame
    fn_login: The function to be called when login succeeds
    db_cursor: sqlite cursor to be used for login
    """

    def __init__(
        self,
        master: any,  # type: ignore
        fn_login: Callable,
        fn_admin: Callable,
        db_cursor,
        width: int = 500,
        height: int = 500,
        corner_radius: Optional[Union[int, str]] = None,
        border_width: Optional[Union[int, str]] = None,
        bg_color: Union[str, Tuple[str, str]] = "transparent",
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        border_color: Optional[Union[str, Tuple[str, str]]] = None,
        background_corner_colors: Union[
            Tuple[Union[str, Tuple[str, str]]], None
        ] = None,
        overwrite_preferred_drawing_method: Union[str, None] = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        self.__uname_variable = ctk.StringVar()
        self.__passwd_variable = ctk.StringVar()
        self.db_cursor: sqlite3.Cursor = db_cursor

        image_path = os.path.join(os.path.dirname(os.getcwd()), "media")
        # self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "mega_mart_logo.png")), size=("150x150"))
        # self.bind("<F11>", command=self.toggle_fullscreen)
        # I hate this
        self.draw(fn_login=fn_login, fn_admin=fn_admin)

    def draw(self, fn_login: Callable, fn_admin: Callable) -> None:
        # setup grid 2x1
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images
        try:
            self.image_path = os.path.join(os.getcwd(), "media")
        except:
            raise FileNotFoundError(
                "Folder does not exist in file tree: ./media/\n Are you at project root?"
            )

        self.image_logo = ctk.CTkImage(
            Image.open(os.path.join(self.image_path, "mega_mart_logo.png")),
            size=(500, 500),
        )

        # logo frame
        self.frame_logo: ctk.CTkFrame = ctk.CTkFrame(
            self, bg_color="yellow", width=500, corner_radius=0
        )
        self.frame_logo.grid(row=0, column=0, sticky="nsew")

        self.logo_label: ctk.CTkLabel = ctk.CTkLabel(
            self.frame_logo, image=self.image_logo, text=""
        )
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")

        # credential frame
        self.frame_credential: ctk.CTkFrame = ctk.CTkFrame(self, bg_color="green")
        self.frame_credential.grid(row=0, column=1, sticky="nsew")

        self.entry_uname = ctk.CTkEntry(
            self.frame_credential, textvariable=self.__uname_variable
        )
        self.entry_passwd = ctk.CTkEntry(
            self.frame_credential,
            textvariable=self.__passwd_variable,
            placeholder_text="Password",
            show="*",
        )

        # Hate this again
        self.button_sumbit = ctk.CTkButton(self.frame_credential, text="Submit")
        self.button_sumbit.configure(
            command=lambda: self._login_event(
                self.entry_uname,
                self.entry_passwd,
                fn_login=fn_login,
                fn_admin=fn_admin,
                db_cursor=self.db_cursor,
            )  # type: ignore
        )

        self.entry_uname.grid(row=0, column=0)
        self.entry_passwd.grid(row=1, column=0)
        self.button_sumbit.grid(row=2, column=0, sticky="e")

    def toggle_fullscreen(self) -> None:
        self.fullscreen = not (self.fullscreen)
        self.master.attributes("-fullscreen", self.fullscreen)  # type: ignore

    # TODO: add cryptography
    def _login_event(
        self,
        entry_uname: ctk.CTkEntry,
        entry_passwd: ctk.CTkEntry,
        fn_login: Callable,
        fn_admin: Callable,
        db_cursor: sqlite3.Cursor,
    ) -> None:
        self.uname: str = entry_uname.get()
        self.passwd: str = entry_passwd.get()

        # incoming sql injection exploit PagMan
        print(type(db_cursor))

        user_deets = db_cursor.execute(
            f"SELECT * FROM users WHERE uname = '{self.uname}' AND pwd = '{self.passwd}'"
        ).fetchone()

        print("data fetched: ", user_deets)
        if user_deets is None:
            print("User does not exist")
            return
        if user_deets[5] == 1:
            print("Admin Login successful")
            fn_admin()
        else:
            print("Login successful")
            fn_login()


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(f"{1366}x{768}")
    app.minsize(1366, 768)
    app.title("Login Page")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    frame_login = Login(
        app,
        fn_login=lambda: print("A login was attempted"),
        fn_admin=lambda: print("Admin Login was attempted :o"),
        db_cursor=None,
    )
    frame_login.grid(row=0, column=0, sticky="nsew")

    app.mainloop()
