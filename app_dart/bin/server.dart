import 'package:app_dart/app_dart.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart' as shelf_io;

// the main function to run the server
Future<void> main() async {
  var handler =
      const Pipeline().addMiddleware(logRequests()).addHandler(handleRequest);
  var server = await shelf_io.serve(handler, 'localhost', 8080);
  print('server listening on http://${server.address.host}:${server.port}');
}
