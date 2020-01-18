def test_get(client):
    url = "/home_api/pi_temp"
    res = client.get(url)
    assert res.status_code == 200

    res = client.get(url + "?n=1")
    assert res.status_code == 200
    # assert "pytest" in res.json
    # assert len(res.json["pytest"]) == 1


def test_post(client):
    url = "/home_api/pi_temp"
    res = client.post(url)
    # assert res.status_code != 200  # This should fail

    data = {"name": "pytest", "temperature": -1}
    res = client.post(url, json=data)
    assert res.status_code == 200

    data = {"name": "pytest"}
    res = client.post(url, json=data)
    assert res.status_code != 200  # This should fail

