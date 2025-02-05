import 'dart:ui';
import 'package:flutter/material.dart';

void main() {
  runApp(NorthernLightsApp());
}

class NorthernLightsApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Northern Lights',
      home: Scaffold(
        backgroundColor: const Color.fromARGB(255, 0, 140, 255),
        body: Center(
          child: NorthernLightsWidget(),
        ),
      ),
    );
  }
}

class NorthernLightsWidget extends StatefulWidget {
  @override
  _NorthernLightsWidgetState createState() => _NorthernLightsWidgetState();
}

class _NorthernLightsWidgetState extends State<NorthernLightsWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: Duration(seconds: 10),
    )..repeat(); // Continuous flowing animation
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return CustomPaint(
          size: Size(double.infinity, double.infinity), // Full screen
          painter: NorthernLightsPainter(_controller.value),
        );
      },
    );
  }
}

class NorthernLightsPainter extends CustomPainter {
  final double animationValue;
  NorthernLightsPainter(this.animationValue);

  @override
  void paint(Canvas canvas, Size size) {
    final Paint paint = Paint()
      ..shader = LinearGradient(
        colors: [
          const Color.fromARGB(255, 3, 194, 102).withOpacity(0.5),
          const Color.fromARGB(255, 27, 255, 217).withOpacity(0.5),
          const Color.fromARGB(255, 0, 255, 255).withOpacity(0.4),   
          const Color.fromARGB(255, 255, 0, 157).withOpacity(0.4),  
          const Color.fromARGB(255, 255, 255, 255).withOpacity(0.3), 
          const Color.fromARGB(255, 217, 0, 255).withOpacity(0.4), 
        ],
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        stops: [
          0.0,
          0.2,
          0.3,
          0.6,
          0.8,
          1.0,
        ],
      ).createShader(Rect.fromLTRB(0, 0, size.width, size.height));

    double shift = animationValue * size.width;

    final Paint paintBackground = Paint()
      ..shader = LinearGradient(
        colors: [
          Colors.greenAccent.withOpacity(0.5),
          Colors.cyanAccent.withOpacity(0.4),
          Colors.pinkAccent.withOpacity(0.4),
          Colors.yellowAccent.withOpacity(0.3),
          Colors.purpleAccent.withOpacity(0.4),
        ],
        begin: Alignment.topLeft,
        end: Alignment.bottomRight,
        stops: [
          0.0,
          0.3,
          0.6,
          0.8,
          1.0,
        ],
      ).createShader(Rect.fromLTRB(-shift, 0, size.width - shift, size.height));

    canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), paintBackground);
  }

  @override
  bool shouldRepaint(NorthernLightsPainter oldDelegate) {
    return true; 
  }
}
