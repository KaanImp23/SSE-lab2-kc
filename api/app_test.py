from app import process_query
import requests


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == \
            "Dinosaurs ruled the Earth 200 million years ago"


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_request():
    assert response.status_code == 200
