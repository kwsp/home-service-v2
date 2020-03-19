class TestHumidity:
    url = "/home_api/room_humidity"

    def test_post(self, client):
        url = self.url

        data = {"name": "pytest", "value": 60}
        res = client.post(url, json=data)
        assert res.status_code == 200

    def test_post_invalid(self, client):
        url = self.url

        res = client.post(url)
        assert res.status_code != 200  # This should fail

        data = {"name": "pytest"}
        res = client.post(url, json=data)
        assert res.status_code != 200  # This should fail

        data = {"name": "pytest", "value": -1}
        res = client.post(url, json=data)
        assert res.status_code != 200

        data = {"name": "pytest", "value": 101}
        res = client.post(url, json=data)
        assert res.status_code != 200

    def test_get(self, client):
        url = self.url

        res = client.get(url)
        assert res.status_code == 200

        res = client.get(url + "?name=pytest")
        assert res.status_code == 200
        assert "result" in res.json
        assert "pytest" == res.json["result"][0]["name"]
