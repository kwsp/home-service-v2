class TestFactory:
    def test_factory(self, app):
        assert app.config.get("TESTING")

    def test_app_notest(self, app_notest):
        assert not app_notest.config.get("TESTING")
