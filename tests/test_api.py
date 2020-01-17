

def test_sensor_data(client):
    res = client.get('/home_api/sensor_temp')
    assert res.status_code == 200


def test_pi_temp(client):
    res = client.get('/home_api/pi_temp')
    assert res.status_code == 200
