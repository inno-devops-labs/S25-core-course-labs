import 'package:app_dart/presentation/home_page.dart';
import 'package:app_dart/domain/time_zone_interactor.dart';
import 'package:flutter/material.dart';

final class App extends StatelessWidget {
  final TimeZoneInteractor interactor;
  const App({super.key, required this.interactor});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Yekaterinburg Time',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: HomePage(interactor: interactor),
    );
  }
}
