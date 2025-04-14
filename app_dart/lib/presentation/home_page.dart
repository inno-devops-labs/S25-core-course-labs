import 'package:app_dart/domain/formatting.dart';
import 'package:app_dart/domain/time_zone_interactor.dart';
import 'package:flutter/material.dart';

final class HomePage extends StatelessWidget {
  final TimeZoneInteractor interactor;
  const HomePage({super.key, required this.interactor});

  @override
  Widget build(BuildContext context) => Scaffold(
    body: SizedBox(
      width: double.infinity,
      height: double.infinity,
      child: Align(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              'Current Time in Yekaterinburg:',
              style: TextStyle(
                fontSize: 32,
                color: Colors.black,
              ),
            ),

            SizedBox(height: 12),

            StreamBuilder(
              stream: interactor.nowChanges,
              builder: (context, now) => Text(
                now.data?.appFormat ?? interactor.now.appFormat,
                style: TextStyle(
                  fontSize: 18,
                  color: Colors.black,
                ),
              ),
            ),
          ],
        ),
      ),
    ),
  );
}
