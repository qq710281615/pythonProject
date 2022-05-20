from test_ui_cases.pages.app_main import App


class TestMain:
    app = App()
    app.start().homepage()
