import reflex as rx
from app.states.state import AppState, Service


def service_feature(text: str) -> rx.Component:
    return rx.el.li(
        rx.icon(tag="square_check", class_name="text-teal-500 size-5"),
        rx.el.span(text, class_name="text-gray-700"),
        class_name="flex items-center gap-3",
    )


def service_detail_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=service["icon"], class_name="text-teal-500 size-8"),
            class_name="p-4 bg-teal-100/50 rounded-xl w-fit mb-4",
        ),
        rx.el.h3(service["title"], class_name="text-2xl font-bold text-gray-800 mb-3"),
        rx.el.p(service["description"], class_name="text-gray-600 mb-6"),
        rx.el.div(
            service_feature("Requirement Analysis"),
            service_feature("System Architecture & Design"),
            service_feature("Agile Development & Testing"),
            service_feature("Deployment & Maintenance"),
            class_name="flex flex-col gap-4",
        ),
        class_name="p-8 bg-white rounded-2xl border border-gray-200/80 shadow-sm",
    )


def services_page() -> rx.Component:
    return rx.el.div(
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "Our Services",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "Comprehensive technology solutions to meet your business needs.",
                    class_name="mt-4 max-w-2xl mx-auto text-center text-lg md:text-xl text-gray-600",
                ),
                class_name="max-w-7xl mx-auto px-4 py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.foreach(AppState.services, service_detail_card),
                class_name="max-w-7xl mx-auto grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="px-4 py-20",
        ),
    )