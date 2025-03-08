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


def create_visits_page(count) -> str:
    """
    This function formats an HTML document for a visits page
    displaying the visit count.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visitor Count</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #e3f2fd;
                color: #333;
            }}
            .count {{
                font-size: 2em;
                font-weight: bold;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Number of Visits</h1>
        <div class="count">{count}</div>
    </body>
    </html>
    """
    return html_content
