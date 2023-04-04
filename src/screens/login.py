import os
from tkinter import NSEW
from typing import NoReturn, Optional, Tuple, Union

from PIL import Image

import customtkinter as ctk


class Login(ctk.CTkFrame):
    def __init__(
        self,
        master: any, # type: ignore
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

        image_path = os.path.join(os.path.dirname(os.getcwd()), "media")
        # self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "mega_mart_logo.png")), size=("150x150"))

        # self.bind("<F11>", command=self.toggle_fullscreen)
        self.draw()

    def draw(self):
        # setup grid
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # create logo frame
        self.logo_frame: ctk.CTkFrame = ctk.CTkFrame(self, corner_radius=0, width=500, bg_color="White")
        self.logo_image: ctk.CTkImage = ctk.CTkImage(Image.open(".//media//mega_mart_logo.png"), size=(500,500))
        self.logo_label: ctk.CTkLabel = ctk.CTkLabel(self, image=self.logo_image, text="")
        self.logo_label.grid(row = 0, column = 0, sticky=NSEW)

        # create credential frame
        self.credential_frame: ctk.CTkFrame = ctk.CTkFrame(self, bg_color="transparent", corner_radius=0,)
        self.credential_frame.grid(row = 0, column = 1, sticky = NSEW)
        

    fullscreen: bool = False

    def toggle_fullscreen(self) -> None:
        self.fullscreen = not (self.fullscreen)
        self.master.attributes("-fullscreen", self.fullscreen) # type: ignore


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(f"{1366}x{768}")
    app.rowconfigure(0, weight=1)
    app.columnconfigure(0, weight=1)
    Login(app).pack(fill="both")
    app.mainloop()