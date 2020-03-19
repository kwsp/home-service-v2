def test_index(client):
    res = client.get("/")
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
