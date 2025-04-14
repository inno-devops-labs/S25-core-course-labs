"""
 In this module we implement template formatter for
 simplistic web service that provides current time in Moscow.

 SPDX-LICENCE: no-licence
 Author: Elon Max
"""


def create_time_page(location: str, time: str) -> str:
    """
        This function simply formats a web document given provided args.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Time in {location}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f4f4f9;
                color: #333;
            }}
            .time {{
                font-size: 2em;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Current Time in {location}</h1>
        <div class="time">{time}</div>
    </body>
    </html>
    """
    return html_content
