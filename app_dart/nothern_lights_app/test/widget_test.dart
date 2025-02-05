import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:nothern_lights_app/main.dart';

void main() {
  testWidgets('Northern Lights app renders correctly', (WidgetTester tester) async {
    await tester.pumpWidget(NorthernLightsApp());
    expect(find.text('Northern Lights'), findsOneWidget);
    expect(find.byType(NorthernLightsWidget), findsOneWidget);
  });
}
