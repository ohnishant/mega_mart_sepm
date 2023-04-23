import customtkinter as ctk

from typing import Optional, Union, Tuple


class Admin(ctk.CTkFrame):
    def __init__(
        self,
        master: any,  # type: ignore
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


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(f"{1366}x{768}")
    app.minsize(1366, 768)
    app.title("Admin Panel")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    frame_login = Admin(app)
    frame_login.grid(row=0, column=0, sticky="nsew")

    app.mainloop()