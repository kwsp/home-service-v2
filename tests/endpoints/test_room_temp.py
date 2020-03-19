import time


class TestRoomTemp:
    url = "/home_api/room_temp"

    def test_post(self, client):
        res = client.post(self.url)
        assert res.status_code != 200  # This should fail

        data = {"name": "pytest", "value": -1}
        res = client.post(self.url, json=data)
        assert res.status_code == 200

        data = {"name": "pytest"}
        res = client.post(self.url, json=data)
        assert res.status_code != 200  # This should fail

    def test_get_simple(self, client):
        res = client.get(self.url)
        assert res.status_code == 200

    def test_get_with_name(self, client):
        res = client.get(self.url + "?name=pytest")
        assert res.status_code == 200
        assert "result" in res.json

    def test_get_with_time(self, client):
        res = client.get(self.url + "?begin={}".format(time.time() + 1000))
        assert res.status_code == 200
        assert len(res.json["result"]) == 0

        res = client.get(self.url + "?end={}".format(0))
        assert len(res.json["result"]) == 0
