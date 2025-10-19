import reflex as rx
from typing import TypedDict, Optional
import json


class Service(TypedDict):
    icon: str
    title: str
    description: str


class TeamMember(TypedDict):
    name: str
    role: str
    avatar_url: str


class BlogPost(TypedDict):
    slug: str
    title: str
    author: str
    date: str
    category: str
    excerpt: str
    content: str


class AppState(rx.State):
    """The main application state."""

    is_mobile_menu_open: bool = False
    form_data: dict = {}
    services: list[Service] = [
        {
            "icon": "code-2",
            "title": "Custom Software Development",
            "description": "Tailored software solutions to meet your unique business needs, from web apps to enterprise systems.",
        },
        {
            "icon": "cloud",
            "title": "Cloud & DevOps",
            "description": "Optimize your infrastructure with our cloud migration, management, and DevOps automation services.",
        },
        {
            "icon": "database",
            "title": "Data Engineering & Analytics",
            "description": "Unlock insights from your data with our expertise in data warehousing, ETL pipelines, and BI.",
        },
        {
            "icon": "shield-check",
            "title": "Cybersecurity Solutions",
            "description": "Protect your digital assets with comprehensive security audits, threat monitoring, and compliance.",
        },
        {
            "icon": "figma",
            "title": "UI/UX Design",
            "description": "Creating intuitive and beautiful user interfaces that provide a seamless user experience.",
        },
        {
            "icon": "briefcase",
            "title": "IT Consulting",
            "description": "Strategic guidance to align your technology with your business goals for growth and efficiency.",
        },
    ]
    team_members: list[TeamMember] = [
        {
            "name": "John Doe",
            "role": "CEO & Lead Architect",
            "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=JohnDoe",
        },
        {
            "name": "Jane Smith",
            "role": "Head of Engineering",
            "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=JaneSmith",
        },
        {
            "name": "Peter Jones",
            "role": "Cybersecurity Expert",
            "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=PeterJones",
        },
        {
            "name": "Emily Williams",
            "role": "Lead UI/UX Designer",
            "avatar_url": "https://api.dicebear.com/9.x/notionists/svg?seed=EmilyWilliams",
        },
    ]
    blog_search_query: str = ""
    active_category: str = "All"
    blog_posts_shown: int = 6
    blog_posts: list[BlogPost] = [
        {
            "slug": "mastering-async-in-python",
            "title": "Mastering Asynchronous Python for High-Performance Apps",
            "author": "Jane Smith",
            "date": "2024-07-21",
            "category": "Engineering",
            "excerpt": "Dive deep into Python's asyncio library, understand event loops, and learn best practices for building scalable, non-blocking applications.",
            "content": """<p>Asynchronous programming is a cornerstone of modern, high-performance applications. In Python, the <code>asyncio</code> library provides a powerful framework for writing single-threaded concurrent code using coroutines, event loops, and futures.</p><h4>The Event Loop</h4><p>The heart of any asyncio application is the event loop. It's responsible for managing and executing asynchronous tasks. When an async function awaits another, it yields control back to the event loop, which can then run other tasks.</p><pre><code class="language-python">import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('...world!')

asyncio.run(main())
</code></pre><h4>Coroutines and `await`</h4><p>A function defined with <code>async def</code> is a coroutine. It can be paused and resumed. The <code>await</code> keyword is used to call other coroutines, effectively pausing the current one until the awaited coroutine completes.</p><h4>Building a Scalable Service</h4><p>Let's consider a web scraper. A synchronous scraper would fetch one page at a time. An asynchronous one can initiate multiple requests concurrently, dramatically speeding up the process. This non-blocking I/O is where asyncio shines.</p>""",
        },
        {
            "slug": "ci-cd-pipelines-with-github-actions",
            "title": "Building Robust CI/CD Pipelines with GitHub Actions",
            "author": "Peter Jones",
            "date": "2024-07-20",
            "category": "DevOps",
            "excerpt": "Learn how to automate your development workflow, from testing to deployment, using the power and simplicity of GitHub Actions.",
            "content": """<p>Continuous Integration and Continuous Deployment (CI/CD) are essential DevOps practices. GitHub Actions makes it easier than ever to automate these workflows directly within your repository.</p><h4>What is GitHub Actions?</h4><p>It allows you to create custom software development life cycle (SDLC) workflows. You define a series of commands to be executed on specific events, like a push or pull request.</p><h4>Example Workflow: Python CI</h4><p>A typical CI workflow for a Python project might include steps to:</p><ul><li>Check out the code</li><li>Set up a specific Python version</li><li>Install dependencies</li><li>Run tests with pytest</li><li>Lint code with flake8</li></ul><pre><code class="language-yaml">name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test with pytest
      run: |
        pytest
</code></pre><p>This simple workflow ensures that every change is automatically tested, catching bugs early and maintaining code quality.</p>""",
        },
        {
            "slug": "microservices-vs-monoliths",
            "title": "Microservices vs. Monoliths: Choosing the Right Architecture",
            "author": "John Doe",
            "date": "2024-07-18",
            "category": "Architecture",
            "excerpt": "A balanced look at the pros and cons of microservices and monolithic architectures to help you make informed decisions for your next project.",
            "content": "<p>The choice between a monolithic and a microservices architecture is one of the most critical decisions in software design. There is no one-size-fits-all answer.</p><h4>Monolithic Architecture</h4><p>A monolith is a single, unified application. All components are tightly coupled and run as a single service.<h5>Pros:</h5><ul><li>Simpler to develop initially</li><li>Easier to deploy and test</li></ul><h5>Cons:</h5><ul><li>Scalability challenges</li><li>Technology stack is locked in</li><li>Difficult to maintain as it grows</li></ul></p><h4>Microservices Architecture</h4><p>In this approach, the application is broken down into a collection of smaller, independent services.<h5>Pros:</h5><ul><li>Improved scalability and flexibility</li><li>Services can be developed and deployed independently</li><li>Technology diversity is possible</li></ul><h5>Cons:</h5><ul><li>Increased complexity in management and deployment</li><li>Challenges with data consistency and network latency</li></ul></p><h4>Which to Choose?</h4><p>Start with a monolith if your team is small, your domain is not well-understood, or time-to-market is critical. Consider microservices for large, complex applications where scalability and team autonomy are paramount. A 'modular monolith' can often be a good compromise.</p>",
        },
        {
            "slug": "zero-trust-security-model",
            "title": "Implementing a Zero Trust Security Model",
            "author": "Peter Jones",
            "date": "2024-07-15",
            "category": "Security",
            "excerpt": "Move beyond the traditional perimeter-based security and learn how the 'never trust, always verify' principle can secure your modern enterprise.",
            "content": "<p>The traditional security model of a 'castle and moat' is no longer sufficient in a world of cloud services and remote work. Zero Trust is a security concept centered on the belief that organizations should not automatically trust anything inside or outside their perimeters.</p><h4>Core Principles of Zero Trust</h4><ul><li><strong>Verify Explicitly:</strong> Always authenticate and authorize based on all available data points.</li><li><strong>Use Least Privilege Access:</strong> Limit user access with just-in-time and just-enough-access (JIT/JEA).</li><li><strong>Assume Breach:</strong> Minimize blast radius for breaches and prevent lateral movement.</li></ul><h4>Implementation Steps</h4><p>1. <strong>Identity and Access Management (IAM):</strong> Implement strong multi-factor authentication (MFA).<br>2. <strong>Device Management:</strong> Ensure all devices accessing resources are healthy and compliant.<br>3. <strong>Network Segmentation:</strong> Create micro-segments to limit lateral movement.<br>4. <strong>Application Security:</strong> Secure application access and APIs.<br>5. <strong>Data-centric Security:</strong> Classify and encrypt data both at rest and in transit.</p><p>Implementing Zero Trust is a journey, not a destination. It requires a shift in mindset and a commitment to continuous verification.</p>",
        },
        {
            "slug": "the-art-of-ux-design",
            "title": "The Art of Simplicity in UX Design",
            "author": "Emily Williams",
            "date": "2024-07-12",
            "category": "Design",
            "excerpt": "Discover how simplifying user interfaces can lead to more intuitive, engaging, and effective user experiences.",
            "content": "<p>In a world full of complex applications, simplicity is a powerful design principle. A simple, intuitive user interface (UI) reduces cognitive load and allows users to accomplish their goals more efficiently.</p><h4>What is Simplicity in UX?</h4><p>It's not about minimalism for its own sake. It's about clarity, focus, and removing the unnecessary. It's the art of making the complex feel simple.</p><h4>Key Principles for Simple Design</h4><ul><li><strong>Clarity over clutter:</strong> Every element on the screen should have a clear purpose. If it doesn't add value, remove it.</li><li><strong>Progressive disclosure:</strong> Show users only what they need at each step of their journey. Hide advanced features until they are requested.</li><li><strong>Consistency:</strong> Use consistent patterns, colors, and typography throughout the application. This makes the interface predictable and easy to learn.</li><li><strong>Visual Hierarchy:</strong> Guide the user's eye to the most important elements on the page using size, color, and spacing.</li></ul><p>As Antoine de Saint-Exupéry said, \"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.\" This is the essence of simplicity in UX design.</p>",
        },
        {
            "slug": "kubernetes-for-beginners",
            "title": "Kubernetes 101: A Beginner's Guide to Container Orchestration",
            "author": "Jane Smith",
            "date": "2024-07-10",
            "category": "DevOps",
            "excerpt": "An introduction to the core concepts of Kubernetes, including Pods, Services, and Deployments, to get you started with container orchestration.",
            "content": """<p>Kubernetes (K8s) is an open-source platform for automating the deployment, scaling, and management of containerized applications. It has become the de facto standard for container orchestration.</p><h4>Core Concepts</h4><ul><li><strong>Pod:</strong> The smallest deployable unit in Kubernetes. A Pod represents a single instance of a running process in your cluster and can contain one or more containers.</li><li><strong>Service:</strong> An abstraction that defines a logical set of Pods and a policy by which to access them. This provides a stable endpoint for your application.</li><li><strong>Deployment:</strong> A resource object in Kubernetes that provides declarative updates for Pods and ReplicaSets. You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate.</li></ul><h4>Example Deployment YAML</h4><pre><code class="language-yaml">apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
</code></pre><p>This YAML file tells Kubernetes to create a Deployment named 'nginx-deployment' that maintains 3 replicas of a Pod running the nginx image. Getting started with Kubernetes can be daunting, but understanding these fundamental concepts is the first step to mastering it.</p>""",
        },
        {
            "slug": "data-warehousing-with-snowflake",
            "title": "Modern Data Warehousing with Snowflake",
            "author": "John Doe",
            "date": "2024-07-05",
            "category": "Architecture",
            "excerpt": "Explore the architecture and benefits of Snowflake's cloud data platform, and why it's a game-changer for data analytics.",
            "content": "<p>Snowflake is a cloud-native data platform that provides a unique architecture for data warehousing, data lakes, data engineering, and data science.</p><h4>Key Architectural Features</h4><ul><li><strong>Decoupled Storage and Compute:</strong> Snowflake separates data storage from compute resources. This allows you to scale compute up or down independently, paying only for what you use.</li><li><strong>Multi-Cluster, Shared Data:</strong> Multiple compute clusters can access the same shared data without performance degradation, enabling concurrent workloads without contention.</li><li><strong>Cloud Agnostic:</strong> Snowflake runs on all three major cloud providers (AWS, Azure, and GCP), providing flexibility and avoiding vendor lock-in.</li></ul><h4>Why is it a Game-Changer?</h4><p>Traditional data warehouses struggle with concurrency and scalability. Snowflake's architecture solves these problems, offering near-infinite scalability and allowing for a wide range of analytical workloads to run simultaneously. Its Time Travel feature also provides powerful data protection and recovery capabilities.</p><p>For any organization looking to build a modern data stack, Snowflake is a compelling option that offers unparalleled performance, flexibility, and ease of use.</p>",
        },
        {
            "slug": "secure-coding-practices",
            "title": "Top 10 Secure Coding Practices for Developers",
            "author": "Peter Jones",
            "date": "2024-06-28",
            "category": "Security",
            "excerpt": "A practical checklist of essential security practices every developer should incorporate into their workflow to build more secure applications.",
            "content": "<p>Security is not just a job for the security team; it's a responsibility for every developer. Building security into the development lifecycle from the start is the most effective way to prevent vulnerabilities.</p><h4>Top 10 Practices</h4><ol><li><strong>Validate Input:</strong> Never trust user input. Validate, sanitize, and escape all data coming from external sources to prevent injection attacks (SQLi, XSS).</li><li><strong>Use Parameterized Queries:</strong> Always use prepared statements or parameterized queries to interact with the database.</li><li><strong>Implement Proper Authentication and Session Management:</strong> Use strong hashing for passwords, enforce multi-factor authentication, and manage sessions securely.</li><li><strong>Enforce Access Control:</strong> Follow the principle of least privilege. Ensure users can only access the data and functionality they are authorized for.</li><li><strong>Keep Dependencies Updated:</strong> Regularly scan and update third-party libraries and frameworks to patch known vulnerabilities.</li><li><strong>Use HTTPS Everywhere:</strong> Encrypt all data in transit to protect against man-in-the-middle attacks.</li><li><strong>Handle Errors and Logs Carefully:</strong> Avoid leaking sensitive information in error messages or logs.</li><li><strong>Protect Data:</strong> Encrypt sensitive data both at rest and in transit.</li><li><strong>Implement Security Headers:</strong> Use headers like Content-Security-Policy (CSP), Strict-Transport-Security (HSTS), and X-Frame-Options.</li><li><strong>Conduct Security Testing:</strong> Integrate static (SAST) and dynamic (DAST) analysis tools into your CI/CD pipeline.</li></ol><p>By following these practices, you can significantly improve the security posture of your applications and protect your users' data.</p>",
        },
    ]
    current_post: Optional[BlogPost] = None

    @rx.var
    def filtered_blog_posts(self) -> list[BlogPost]:
        search_lower = self.blog_search_query.lower().strip()
        return [
            post
            for post in self.blog_posts
            if (
                self.active_category == "All"
                or post["category"] == self.active_category
            )
            and (
                search_lower in post["title"].lower()
                or search_lower in post["excerpt"].lower()
                or search_lower in post["content"].lower()
            )
        ]

    @rx.var
    def visible_blog_posts(self) -> list[BlogPost]:
        return self.filtered_blog_posts[: self.blog_posts_shown]

    @rx.var
    def has_more_posts(self) -> bool:
        return len(self.visible_blog_posts) < len(self.filtered_blog_posts)

    @rx.event
    def set_blog_search_query(self, query: str):
        self.blog_search_query = query

    @rx.event
    def set_active_category(self, category: str):
        self.active_category = category
        self.blog_posts_shown = 6

    @rx.event
    def load_more_posts(self):
        self.blog_posts_shown += 6

    @rx.event
    def load_post(self):
        slug = self.router.page.params.get("slug", "")
        self.current_post = next(
            (post for post in self.blog_posts if post["slug"] == slug), None
        )
        if self.current_post:
            return rx.call_script("window.scrollTo(0, 0); hljs.highlightAll();")

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    @rx.event
    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(f"Form data received: {form_data}")
        return rx.toast("Your message has been sent successfully!")