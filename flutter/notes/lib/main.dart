import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';
import 'package:notes/services/auth/auth_service.dart';
import 'package:notes/utils/functions.dart';
import 'package:notes/views/home.dart';

void main() {
  // Error Widget
  ErrorWidget.builder = (FlutterErrorDetails details) {
    return customErrorScreen(); // Material
  };

  // Run App
  runApp(MaterialApp(
    title: 'Notes',
    theme: ThemeData(
      useMaterial3: true,
    ),
    home: const StartApp(),
    routes: appRoutes,
  ));
}

class StartApp extends StatelessWidget {
  const StartApp({super.key});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: AuthService.instance().initialize(),
      builder: (context, snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.done: // if instance is done initializing
            return const HomeView();
          default: // if instance is not done initializing
            return const Center(
              child: CircularProgressIndicator(),
            );
        }
      },
    );
  }
}
