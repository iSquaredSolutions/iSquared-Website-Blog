import reflex as rx
from app.states.state import AppState, BlogPost


def post_card(post: BlogPost) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    post["category"], class_name="text-teal-600 font-semibold text-sm"
                ),
                rx.el.p(post["date"], class_name="text-gray-500 text-sm"),
                class_name="flex items-center justify-between mb-2",
            ),
            rx.el.h3(post["title"], class_name="text-xl font-bold text-gray-800 mb-2"),
            rx.el.p(post["excerpt"], class_name="text-gray-600 text-sm mb-4"),
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src=f"https://api.dicebear.com/9.x/notionists/svg?seed={post['author']}",
                        class_name="size-8 rounded-full",
                    ),
                    rx.el.p(
                        post["author"], class_name="text-gray-700 font-medium text-sm"
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.div(
                    "Read More",
                    rx.icon(tag="arrow-right", class_name="size-4 ml-1"),
                    class_name="flex items-center text-teal-600 font-semibold text-sm",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="p-6 bg-white rounded-2xl border border-gray-200/80 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 h-full flex flex-col justify-between",
        ),
        href=f"/blog/{post['slug']}",
    )


def category_button(category: str) -> rx.Component:
    return rx.el.button(
        category,
        on_click=lambda: AppState.set_active_category(category),
        class_name=rx.cond(
            AppState.active_category == category,
            "px-4 py-2 text-sm font-semibold rounded-full bg-teal-500 text-white shadow-md",
            "px-4 py-2 text-sm font-semibold rounded-full bg-white text-gray-600 hover:bg-gray-100 border border-gray-200 transition-colors",
        ),
    )


def blog_page() -> rx.Component:
    return rx.el.div(
        rx.el.section(
            rx.el.div(
                rx.el.h1(
                    "The Engineering Blog",
                    class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight text-center",
                ),
                rx.el.p(
                    "Insights, tutorials, and thoughts on technology and software development.",
                    class_name="mt-4 max-w-2xl mx-auto text-center text-lg md:text-xl text-gray-600",
                ),
                class_name="max-w-7xl mx-auto px-4 py-16 md:py-24",
            ),
            class_name="bg-gray-50",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        placeholder="Search articles...",
                        on_change=AppState.set_blog_search_query.debounce(300),
                        class_name="w-full md:w-1/3 px-4 py-2 rounded-lg border border-gray-300 focus:border-teal-500 focus:ring-2 focus:ring-teal-200 transition",
                    ),
                    rx.el.div(
                        rx.foreach(
                            [
                                "All",
                                "Engineering",
                                "DevOps",
                                "Architecture",
                                "Security",
                                "Design",
                            ],
                            category_button,
                        ),
                        class_name="flex flex-wrap gap-2 justify-center",
                    ),
                    class_name="flex flex-col md:flex-row justify-between items-center gap-6 mb-12",
                ),
                rx.el.div(
                    rx.foreach(AppState.visible_blog_posts, post_card),
                    class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
                ),
                rx.cond(
                    AppState.filtered_blog_posts.length() == 0,
                    rx.el.div(
                        rx.el.p(
                            "No posts found. Try a different search or category.",
                            class_name="text-center text-gray-500 col-span-full",
                        )
                    ),
                ),
                rx.cond(
                    AppState.has_more_posts,
                    rx.el.div(
                        rx.el.button(
                            "Load More",
                            on_click=AppState.load_more_posts,
                            class_name="mt-12 bg-teal-500 text-white font-semibold px-6 py-3 rounded-xl hover:bg-teal-600 transition-all duration-300 shadow-lg hover:shadow-teal-500/20",
                        ),
                        class_name="text-center",
                    ),
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="px-4 py-20",
        ),
        rx.script(
            src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
        ),
    )


def blog_post_page() -> rx.Component:
    return rx.el.div(
        rx.cond(
            AppState.current_post,
            rx.el.div(
                rx.el.section(
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                AppState.current_post["category"],
                                class_name="text-teal-600 font-semibold",
                            ),
                            rx.el.h1(
                                AppState.current_post["title"],
                                class_name="text-4xl md:text-5xl font-extrabold text-gray-900 tracking-tight my-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.image(
                                        src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AppState.current_post['author']}",
                                        class_name="size-10 rounded-full",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            AppState.current_post["author"],
                                            class_name="font-semibold text-gray-800",
                                        ),
                                        rx.el.p(
                                            AppState.current_post["date"],
                                            class_name="text-sm text-gray-500",
                                        ),
                                    ),
                                    class_name="flex items-center gap-4",
                                ),
                                class_name="flex items-center gap-4",
                            ),
                            class_name="max-w-4xl mx-auto text-center",
                        ),
                        class_name="py-24 bg-gray-50",
                    )
                ),
                rx.el.section(
                    rx.el.div(
                        rx.el.div(
                            id="post-content",
                            class_name="prose lg:prose-xl max-w-4xl mx-auto py-20",
                        ),
                        rx.el.script(
                            f"document.getElementById('post-content').innerHTML = `{AppState.current_post['content']}`"
                        ),
                    )
                ),
            ),
            rx.el.div(
                rx.el.p("Post not found.", class_name="text-center text-2xl py-20")
            ),
        )
    )