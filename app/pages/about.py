import reflex as rx
from app.states.state import AppState, TeamMember


def team_member_card(member: TeamMember) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=member["avatar_url"],
            class_name="size-24 rounded-full mx-auto mb-4 border-2 border-gray-200 shadow-sm",
        ),
        rx.el.h3(member["name"], class_name="text-lg font-semibold text-gray-800"),
        rx.el.p(member["role"], class_name="text-teal-600 text-sm"),
        class_name="text-center p-6 bg-white rounded-2xl border border-gray-200/80 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def about_page() -> rx.Component:
    return rx.el.div(
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "About iSquared Solutions",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "We are a team of passionate engineers and designers dedicated to building exceptional technology.",
                    class_name="mt-4 max-w-3xl mx-auto text-center text-lg md:text-xl text-gray-600",
                ),
                class_name="max-w-7xl mx-auto px-4 py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Our Mission",
                            class_name="text-3xl font-bold text-gray-900 mb-4",
                        ),
                        rx.el.p(
                            "To empower businesses with innovative and robust technology solutions that drive growth, efficiency, and success in a rapidly evolving digital landscape. We are committed to engineering excellence and building long-term partnerships with our clients.",
                            class_name="text-gray-600 text-lg leading-relaxed",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h2(
                            "Our Vision",
                            class_name="text-3xl font-bold text-gray-900 mb-4",
                        ),
                        rx.el.p(
                            "To be a leading technology partner recognized for our expertise, integrity, and commitment to delivering transformative results. We envision a future where technology seamlessly integrates with business to unlock human potential.",
                            class_name="text-gray-600 text-lg leading-relaxed",
                        ),
                    ),
                    class_name="grid md:grid-cols-2 gap-12 max-w-7xl mx-auto",
                ),
                class_name="px-4 py-20",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Meet the Team",
                        class_name="text-3xl md:text-4xl font-bold text-gray-900",
                    ),
                    rx.el.p(
                        "The minds behind our innovation and success.",
                        class_name="mt-2 text-gray-600 text-lg",
                    ),
                    class_name="text-center mb-12",
                ),
                rx.el.div(
                    rx.foreach(AppState.team_members, team_member_card),
                    class_name="grid sm:grid-cols-2 lg:grid-cols-4 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 py-20",
            ),
            class_name="bg-gray-50",
        ),
    )