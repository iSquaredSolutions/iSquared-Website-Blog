import reflex as rx
from app.states.state import AppState


def nav_link(text: str, url: str) -> rx.Component:
    return rx.el.a(
        text,
        href=url,
        on_click=AppState.close_mobile_menu,
        class_name="text-gray-500 hover:text-teal-500 transition-colors py-2 md:py-0",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon(tag="command", class_name="text-teal-500"),
                        rx.el.h2(
                            "iSquared Solutions",
                            class_name="font-bold text-gray-800 text-lg",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    href="/",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon(tag=rx.cond(AppState.is_mobile_menu_open, "x", "menu")),
                        on_click=AppState.toggle_mobile_menu,
                        class_name="p-2 rounded-md text-gray-600 hover:bg-gray-100 md:hidden",
                    ),
                    class_name="md:hidden",
                ),
                class_name="flex items-center justify-between",
            ),
            rx.el.nav(
                nav_link("Home", "/"),
                nav_link("About", "/about"),
                nav_link("Services", "/services"),
                nav_link("Blog", "/blog"),
                nav_link("Contact", "/contact"),
                class_name=rx.cond(
                    AppState.is_mobile_menu_open,
                    "flex flex-col items-start gap-4 mt-4",
                    "hidden md:flex md:items-center md:gap-6",
                ),
            ),
            class_name="md:flex md:items-center md:justify-between w-full",
        ),
        class_name="sticky top-0 bg-white/80 backdrop-blur-md z-50 p-4 border-b border-gray-200",
    )