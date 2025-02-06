import 'package:flutter_test/flutter_test.dart';
import 'package:nothern_lights_app/main.dart';

void main() {
  testWidgets('Northern Lights app renders correctly', (WidgetTester tester) async {
    await tester.pumpWidget(const NorthernLightsApp());
    expect(find.byType(NorthernLightsWidget), findsOneWidget);
  });
}
