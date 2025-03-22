import 'package:app_dart/app.dart';
import 'package:app_dart/app_config.dart';
import 'package:app_dart/domain/formatting.dart';
import 'package:app_dart/domain/time_zone_interactor.dart';
import 'package:app_dart/test_tag.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() async {
  final interactor = await TimeZoneInteractor.setup(
    timezone: AppConfig.timezone,
  );

  /**
   * Expects that page shows the correct time in format:
   *
   * Current time in Yekaterinburg:
   * hh:mm:ss dd.mm.yyyy
   *
   * Test runs for 5 ticks (seconds)
   */

  testWidgets('Yekaterinburg time test', (WidgetTester tester) async {
    await tester.pumpWidget(App(interactor: interactor));

    for (int i = 0; i < 5; ++i) {
      final title = find
        .byKey(Key(TestTag.homePageTitle))
        .evaluate().single.widget as Text;

      expect(title.data, 'Current Time in Yekaterinburg:');
      expect(title.style, TextStyle(fontSize: 32, color: Colors.black));

      final time = find
        .byKey(Key(TestTag.homePageTime))
        .evaluate().single.widget as Text;

      expect(time.data, interactor.now.appFormat);
      expect(time.style, TextStyle(fontSize: 18, color: Colors.black));

      await tester.pump(Duration(seconds: i));
    }
  });
}
