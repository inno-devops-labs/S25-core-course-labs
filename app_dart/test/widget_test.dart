import 'package:app_dart/app.dart';
import 'package:app_dart/app_config.dart';
import 'package:app_dart/domain/formatting.dart';
import 'package:app_dart/domain/time_zone_interactor.dart';
import 'package:flutter_test/flutter_test.dart';

void main() async {
  final interactor = await TimeZoneInteractor.setup(timezone: AppConfig.timezone);

  testWidgets('Yekaterinburg time test', (WidgetTester tester) async {
    await tester.pumpWidget(App(interactor: interactor));
    final now = interactor.now.appFormat;
    expect(find.text(now), findsOneWidget);
  });
}
