def test_factory(app):
    assert app.config.get("TESTING")
