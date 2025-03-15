import 'package:timezone/browser.dart' as tz;

extension DateFormatting on tz.TZDateTime {
  String get appFormat =>
      '${hour.timeFormat}:${minute.timeFormat}:${second.timeFormat} '
          '${day.timeFormat}.${month.timeFormat}.$year';
}

extension _TimeFormatting on int {
  String get timeFormat => this < 10 ? '0$this' : toString();
}
