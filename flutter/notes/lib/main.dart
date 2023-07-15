import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:notes/views/home.dart';
import 'package:notes/views/login.dart';
import 'package:notes/views/register.dart';
import 'package:notes/views/verify_email.dart';

import 'firebase_options.dart';

void main() {
  // Error Widget
  ErrorWidget.builder = (FlutterErrorDetails details) {
    return Material(
      child: Container(
        color: const Color.fromARGB(255, 2, 161, 26),
        child: const Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Error',
              style: TextStyle(
                fontSize: 30,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ), // Text
          ],
        ),
      ), // TextColumn
    ); // Material
  };

  // Run App
  runApp(MaterialApp(
    title: 'Notes',
    theme: ThemeData(
      useMaterial3: true,
    ),
    home: const StartApp(),
    routes: {
      '/login': (context) => const LoginView(),
      '/verify_email': (context) => const VerifyEmail(),
      '/register': (context) => const RegisterView(),
      '/home': (context) => const HomeView(),
    },
  ));
}

class StartApp extends StatelessWidget {
  const StartApp({super.key});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      // Initialize FlutterFire before rendering the form
      future: Firebase.initializeApp(
        options: DefaultFirebaseOptions.currentPlatform,
      ),
      builder: (context, snapshot) {
        switch (snapshot.connectionState) {
          case ConnectionState.done: // if firebase is done initializing
            // if (user == null) {
            //   return const LoginView();
            // }
            // if (user.emailVerified != true) {
            //   return const VerifyEmail();
            // }
            return const HomeView();
          default: // if firebase is not done initializing
            return const Center(
              child: CircularProgressIndicator(),
            );
        }
      },
    );
  }
}
