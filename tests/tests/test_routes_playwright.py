import requests


def test_index_screenshot(play_ip, play_port, sut_ip, sut_port, browsers="http", endpoint=None):
    BASE_URL = f"http://{play_ip}:{play_port}"
    print("test_create_card BASE_URL", BASE_URL)

    payload = {
        "sut_ip": sut_ip,
        "sut_port": sut_port,
        "browsers": browsers,
        "endpoint": endpoint
    }
    response = requests.post(f"{BASE_URL}/screenshot/", json=payload)
    print("test_index_screenshot returen code", response.status_code)
    assert response.status_code == 200
    print("test_create_card returen", response.json())
    assert response.headers["content-type"] == "application/json"
    assert isinstance(response.json(), dict)
