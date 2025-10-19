import reflex as rx
from app.states.state import AppState


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(class_name="circle -one"),
            rx.el.div(class_name="circle -two"),
            rx.el.div(class_name="circle -three"),
            class_name="animated-background",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    rx.el.span(
                        rx.el.span("I", class_name="text-teal-500 font-bold"),
                        "nformation ",
                        rx.el.span("i", class_name="text-teal-500 font-bold"),
                        "n formation.",
                    ),
                    class_name="text-4xl md:text-6xl font-extrabold text-gray-900 tracking-tight whitespace-nowrap",
                ),
                rx.el.p(
                    "We build intelligent systems to organize your data, transforming it into actionable insights. Make data-driven decisions with iSquared Solutions.",
                    class_name="mt-4 max-w-2xl text-lg md:text-xl text-gray-600",
                ),
                rx.el.div(
                    rx.el.a(
                        "Our Services",
                        href="#services",
                        class_name="bg-teal-500 text-white font-semibold px-8 py-3 rounded-xl hover:bg-teal-600 transition-all duration-300 shadow-lg hover:shadow-teal-500/20",
                    ),
                    rx.el.a(
                        "Contact Us",
                        rx.icon(tag="arrow-right", class_name="ml-2"),
                        href="/contact",
                        class_name="flex items-center text-gray-600 font-semibold hover:text-gray-900 transition-colors",
                    ),
                    class_name="mt-8 flex items-center gap-6",
                ),
                class_name="max-w-4xl text-center md:text-left relative z-10",
            ),
            class_name="relative z-10",
        ),
        class_name="relative w-full flex items-center justify-center bg-gray-50 py-24 md:py-32 overflow-hidden min-h-[50vh]",
    )


def service_card(service: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=service["icon"], class_name="text-teal-500"),
            class_name="p-3 bg-teal-100/50 rounded-lg w-fit mb-4",
        ),
        rx.el.h3(
            service["title"], class_name="text-lg font-semibold text-gray-800 mb-2"
        ),
        rx.el.p(service["description"], class_name="text-gray-600 text-sm"),
        class_name="p-6 bg-white rounded-2xl border border-gray-200/80 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def services_overview_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Our Expertise",
                    class_name="text-3xl md:text-4xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "We offer a comprehensive suite of services to cover all your technology needs.",
                    class_name="mt-2 text-gray-600 text-lg",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(AppState.services, service_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        id="services",
        class_name="py-20 px-4",
    )


def home_page() -> rx.Component:
    return rx.el.div(hero_section(), services_overview_section())