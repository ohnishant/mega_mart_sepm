import customtkinter as ctk

from typing import Optional, Union, Tuple


class Checkout(ctk.CTkFrame):
    def __init__(
        self,
        master: any,  # type: ignore
        db_cursor = None,
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
        self.draw()

    active_cart: dict = dict()
    color_toggle: int = 0

    def draw(self):
        cart_item_height = 75
        self.cart_frame = ctk.CTkScrollableFrame(
            self, width=500, height=cart_item_height * 6
        )
        self.cart_frame.configure(label_text="Your Cart")
        self.cart_frame.pack()
        self.button_add_item = ctk.CTkButton(
            self,
            text="add item to frame",
            command=lambda: self.__add_item_to_cart(id=123),
        )
        self.button_add_item.pack()

    def __add_item_to_cart(self, id: int):
        item = (123, "hi this is an item", "metadata")
        self._add_item_to_frame(item=item)

    def _add_item_to_frame(self, item: tuple[int, str, str]):
        item_name = item[1]
        label = ctk.CTkLabel(
            self.cart_frame, text=f"Itemname: {item_name}", height=100, corner_radius=20
        )

        if self.color_toggle == 0:
            label.configure(bg_color="#3f4857")
            self.color_toggle = 1
        else:
            label.configure(bg_color="#23272e")
            self.color_toggle = 0

        label.pack(fill="x")


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry(f"{1366}x{768}")
    app.minsize(1366, 768)
    app.title("User Self Checkout Panel")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    frame_login = Checkout(app)
    frame_login.grid(row=0, column=0, sticky="nsew")

    app.mainloop()
