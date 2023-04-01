from typing import NoReturn, Optional, Tuple, Union

import customtkinter as ctk


class Login(ctk.CTkFrame):
    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: Optional[Union[int, str]] = None,
        border_width: Optional[Union[int, str]] = None,
        bg_color: Union[str, Tuple[str, str]] = "transparent",
        fg_color: Optional[Union[str, Tuple[str, str]]] = None,
        border_color: Optional[Union[str, Tuple[str, str]]] = None,
        background_corner_colors: Union[
            Tuple[Union[str, Tuple[str, str]]], None
        ] = None,
        overwrite_preferred_drawing_method: Union[str, None] = None,
        **kwargs
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
            **kwargs
        )

        self.draw()

    def draw(self):
        fullscreen_button = ctk.CTkButton(self, text="Toggle Fullscreen", command=self.toggle_fullscreen)
        fullscreen_button.pack()


    fullscreen: bool = False
    def toggle_fullscreen(self) -> NoReturn:
        self.fullscreen = not(self.fullscreen)
        self.master.attributes('-fullscreen', self.fullscreen)

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(f"{1366}x{768}")
    Login(app).pack()
    app.mainloop()

