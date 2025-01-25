import 'package:app_dart/app.dart';
import 'package:app_dart/app_config.dart';
import 'package:app_dart/domain/time_zone_interactor.dart';
import 'package:flutter/material.dart';

void main() async {
  final interactor = await TimeZoneInteractor.setup(timezone: AppConfig.timezone);
  runApp(App(interactor: interactor));
}
