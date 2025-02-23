// ignore_for_file: unused_local_variable

import 'package:flutter/material.dart';

void main() {
  runApp(const NorthernLightsApp());
}

class NorthernLightsApp extends StatelessWidget {
  const NorthernLightsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Northern Lights',
      home: Scaffold(
        backgroundColor: Color.fromARGB(255, 0, 140, 255),
        body: Center(
          child: NorthernLightsWidget(),
        ),
      ),
    );
  }
}

class NorthernLightsWidget extends StatefulWidget {
  const NorthernLightsWidget({super.key});

  @override
  // ignore: library_private_types_in_public_api
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
      duration: const Duration(seconds: 10),
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
          size: const Size(double.infinity, double.infinity), // Full screen
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
        stops: const [
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
      ..shader = const LinearGradient(
        colors: [
          Colors.greenAccent,
          Colors.cyanAccent,
          Colors.pinkAccent,
          Colors.yellowAccent,
          Colors.purpleAccent,
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
