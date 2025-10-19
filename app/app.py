import reflex as rx
from app.pages.home import home_page
from app.pages.about import about_page
from app.pages.services import services_page
from app.pages.contact import contact_page
from app.pages.blog import blog_page, blog_post_page
from app.states.state import AppState
from app.components.navbar import navbar
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.main(
        navbar(), home_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


def about() -> rx.Component:
    return rx.el.main(
        navbar(), about_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


def services() -> rx.Component:
    return rx.el.main(
        navbar(), services_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


def contact() -> rx.Component:
    return rx.el.main(
        navbar(), contact_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


def blog() -> rx.Component:
    return rx.el.main(
        navbar(), blog_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


def post() -> rx.Component:
    return rx.el.main(
        navbar(), blog_post_page(), footer(), class_name="font-['Montserrat'] bg-white"
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(about)
app.add_page(services)
app.add_page(contact)
app.add_page(blog)
app.add_page(post, route="/blog/[slug]", on_load=AppState.load_post)