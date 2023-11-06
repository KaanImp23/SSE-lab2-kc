import requests


def test_request():
    response = requests.get(
            "https://api.github.com/users/input_git_username/repos"
            )
    assert response.status_code == 200
