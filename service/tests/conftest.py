import os
import tempfile

import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from server import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
