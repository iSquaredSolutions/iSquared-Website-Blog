import reflex as rx
from app.states.state import AppState


def form_field(
    label: str, placeholder: str, name: str, type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700 mb-1 block"),
        rx.el.input(
            placeholder=placeholder,
            name=name,
            type=type,
            required=True,
            class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-200 transition",
        ),
        class_name="mb-4",
    )


def contact_page() -> rx.Component:
    return rx.el.div(
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Get in Touch",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "We'd love to hear from you. Let's build something great together.",
                    class_name="mt-4 max-w-2xl mx-auto text-center text-lg md:text-xl text-gray-600",
                ),
                class_name="max-w-7xl mx-auto px-4 py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Contact Form",
                        class_name="text-2xl font-bold text-gray-800 mb-6",
                    ),
                    rx.el.form(
                        form_field("Full Name", "John Doe", "full_name"),
                        form_field(
                            "Email Address",
                            "john.doe@example.com",
                            "email",
                            type="email",
                        ),
                        form_field("Subject", "Project Inquiry", "subject"),
                        rx.el.div(
                            rx.el.label(
                                "Message",
                                class_name="text-sm font-medium text-gray-700 mb-1 block",
                            ),
                            rx.el.textarea(
                                placeholder="Your message here...",
                                name="message",
                                required=True,
                                class_name="w-full px-4 py-2 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-200 transition h-32",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.button(
                            "Send Message",
                            type="submit",
                            class_name="w-full bg-teal-500 text-white font-semibold px-8 py-3 rounded-xl hover:bg-teal-600 transition-all duration-300 shadow-lg hover:shadow-teal-500/20",
                        ),
                        on_submit=AppState.handle_submit,
                        reset_on_submit=True,
                    ),
                    class_name="p-8 bg-white rounded-2xl border border-gray-200/80 shadow-sm",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Our Information",
                        class_name="text-2xl font-bold text-gray-800 mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(tag="mail", class_name="size-5 text-teal-600"),
                            rx.el.p(
                                "contact@isquared.solutions", class_name="text-gray-700"
                            ),
                            class_name="flex items-center gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.icon(tag="phone", class_name="size-5 text-teal-600"),
                            rx.el.p("(123) 456-7890", class_name="text-gray-700"),
                            class_name="flex items-center gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.icon(tag="map-pin", class_name="size-5 text-teal-600"),
                            rx.el.p(
                                "123 Tech Avenue, Silicon Valley, CA",
                                class_name="text-gray-700",
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="p-8 bg-white rounded-2xl border border-gray-200/80 shadow-sm",
                    ),
                ),
                class_name="max-w-7xl mx-auto grid lg:grid-cols-2 gap-12 items-start",
            ),
            class_name="px-4 py-20",
        ),
    )