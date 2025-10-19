import reflex as rx


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-500 hover:text-teal-500 transition-colors text-sm",
    )


def social_icon(tag: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(
            tag=tag, class_name="text-gray-400 hover:text-teal-500 transition-colors"
        ),
        href=href,
        target="_blank",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(tag="command", class_name="text-teal-500", size=24),
                        rx.el.h3(
                            "iSquared Solutions",
                            class_name="font-bold text-lg text-gray-800",
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "Engineering excellence, delivered.",
                        class_name="text-sm text-gray-500 max-w-xs",
                    ),
                    class_name="mb-6 md:mb-0",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "Company",
                            class_name="font-semibold text-gray-700 mb-4 text-sm tracking-wider uppercase",
                        ),
                        rx.el.div(
                            footer_link("About", "/about"),
                            footer_link("Services", "/services"),
                            footer_link("Blog", "/blog"),
                            footer_link("Contact Us", "/contact"),
                            class_name="flex flex-col gap-3",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4(
                            "Legal",
                            class_name="font-semibold text-gray-700 mb-4 text-sm tracking-wider uppercase",
                        ),
                        rx.el.div(
                            footer_link("Privacy Policy", "#"),
                            footer_link("Terms of Service", "#"),
                            class_name="flex flex-col gap-3",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-8",
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            rx.el.div(
                rx.el.p(
                    f"© 2024 iSquared Solutions. All rights reserved.",
                    class_name="text-sm text-gray-400",
                ),
                rx.el.div(
                    social_icon("github", "#"),
                    social_icon("twitter", "#"),
                    social_icon("linkedin", "#"),
                    class_name="flex items-center gap-4",
                ),
                class_name="mt-8 pt-8 border-t border-gray-200 flex flex-col md:flex-row items-center justify-between gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 py-12",
        ),
        class_name="bg-gray-50",
    )