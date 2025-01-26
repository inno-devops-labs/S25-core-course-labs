import 'dart:async';

import 'package:timezone/browser.dart' as tz;

final class TimeZoneInteractor {
  final tz.Location _location;
  final _nowChangesController = StreamController<tz.TZDateTime>();

  TimeZoneInteractor._({required tz.Location location}) : _location = location {
    _nowChangesController.addStream(
      Stream.periodic(Duration(milliseconds: 500), (_) => now)
    );
  }

  static Future<TimeZoneInteractor> setup({String? timezone}) async {
    await tz.initializeTimeZone();
    return TimeZoneInteractor._(
      location: tz.getLocation(timezone ?? 'Europe/Moscow')
    );
  }

  tz.TZDateTime get now => tz.TZDateTime.now(_location);

  Stream<tz.TZDateTime> get nowChanges => _nowChangesController.stream;

  Future<void> dispose() => _nowChangesController.close();
}
