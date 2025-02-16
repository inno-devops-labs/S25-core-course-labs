from freezegun import freeze_time

def test_home_route_returns_200(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


@freeze_time("2025-02-03 15:18:18", tz_offset=0)
def test_home_route_displays_correct_moscow_time(test_client, captured_templates):
    response = test_client.get("/")
    assert response.status_code == 200

    assert captured_templates, "No template was rendered"
    _, context = captured_templates[0]
    expected_time = "18:18:18"
    assert context["time"] == expected_time, (
        f"Expected Moscow time {expected_time} but got {context['time']}"
    )
