
def test_get_curr_data(client):
    res = client.get('/home_api/get_curr_data')
    assert res.status_code == 200


def test_pi_temp(client):
    res = client.get('/home_api/pi_temp')
    assert res.status_code == 200
