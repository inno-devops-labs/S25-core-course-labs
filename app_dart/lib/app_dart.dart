import 'package:http/http.dart' as http;
import 'package:shelf/shelf.dart';
import 'dart:convert';

// get the current time in Moscow
Future<String> getMoscowTime() async {
  const moscowTimeZoneParam = 'Europe/Moscow';
  final timeApiUrl =
      'https://timeapi.io/api/Time/current/zone?timeZone=$moscowTimeZoneParam';
  try {
    final response = await http
        .get(Uri.parse(timeApiUrl))
        .timeout(const Duration(seconds: 5));
    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final moscowTime = data['dateTime'];

      // format the time and replace 'T's with ' '
      final formattedTime = moscowTime.replaceAll('T', ' ').split('.')[0];
      return formattedTime;
    } else {
      return 'error: failed to load time';
    }
  } catch (e) {
    return 'error: $e';
  }
}

// handle requests to the server
Future<Response> handleRequest(Request request) async {
  final moscowTime = await getMoscowTime();
  return Response.ok(
    '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time in Moscow</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f0f8ff;
                color: #333;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                background: linear-gradient(135deg, #6e7cfc, #8d9eff);
            }
            .container {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                padding: 40px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
                width: 100%;
            }
            h1 {
                font-size: 2.5em;
                color: #333;
                margin-bottom: 20px;
                font-weight: 600;
            }
            h2 {
                font-size: 3.5em;
                color: #6e7cfc;
                font-weight: 700;
                letter-spacing: 2px;
            }
            h2 {
                animation: fadeIn 1.5s ease-in-out;
            }
            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>The time in Moscow now is:</h1>
            <h2>$moscowTime</h2>
        </div>
    </body>
    </html>
    ''',
    headers: {'Content-Type': 'text/html; charset=utf-8'},
  );
}
