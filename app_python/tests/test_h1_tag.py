"""
This module contains tests for checking the presence of
 an <h1> tag with the current time in Moscow.
"""


def test_h1_tag(client):
    """
    Test that the response contains an
      <h1> tag with the current time in Moscow.
    """
    response = client.get('/')
    current_time = bytes(response.text.split(
        "Current time in Moscow: ")[1][0:8], 'utf-8'
    )
    h1_tag_content = b"<h1>Current time in Moscow: " + current_time + b"</h1>"
    assert h1_tag_content in response.data, (
        "Expected <h1> tag with time "
        f"'{current_time.decode()}' not found in response."
    )
