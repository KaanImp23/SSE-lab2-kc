import requests


def test_request():
    response = requests.get(
            "https://sse-lab2-kc.vercel.app/"
            )
    assert response.status_code == 200
