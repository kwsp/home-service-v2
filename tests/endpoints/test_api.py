def test_index(client):
    res = client.get("/")
    assert res.status_code == 200


def test_debug(client_notest):
    res = client_notest.get("/debug")
    assert res.status_code == 200


def test_room_temp(client):
    res = client.get("/home_api/room_temp")
    assert res.status_code == 200


def test_room_humidity(client):
    res = client.get("/home_api/room_humidity")
    assert res.status_code == 200


def test_server_temp(client):
    res = client.get("/home_api/server_temp")
    assert res.status_code == 200


def test_exception(client_notest):
    """
    The exception handler will handle any backend error
    "notest" will attach this exception handler
    """
    res = client_notest.post("/home_api/fakeendpoint")
    assert res.status_code != 200
