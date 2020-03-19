def test_post(client):
    url = "/home_api/server_temp"
    res = client.post(url)
    assert res.status_code != 200  # This should fail

    data = {"name": "pytest", "value": 30}
    res = client.post(url, json=data)
    assert res.status_code == 200

    data = {"name": "pytest"}
    res = client.post(url, json=data)
    assert res.status_code != 200  # This should fail


def test_get(client):
    url = "/home_api/server_temp"
    res = client.get(url)
    assert res.status_code == 200

    res = client.get(url + "?name=pytest")
    assert res.status_code == 200
    assert "result" in res.json
    assert "pytest" == res.json["result"][0]["name"]
