import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class VerifyEmail extends StatefulWidget {
  const VerifyEmail({super.key});

  @override
  State<VerifyEmail> createState() => _VerifyEmailState();
}

class _VerifyEmailState extends State<VerifyEmail> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Verify Email"),
        backgroundColor: const Color.fromARGB(255, 32, 255, 170),
      ),
      body: Column(children: [
        const Text("Please verify your email address"),
        TextButton(
            onPressed: () async {
              try {
                final user = FirebaseAuth.instance.currentUser;
                await user?.sendEmailVerification().then((value) => {
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text(
                              'Verification email was sent, please check your mail.'),
                        ),
                      )
                    });
              } on FirebaseAuthException catch (e) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      'Error: ${e.code[0].toUpperCase() + e.code.substring(1).replaceAll("-", " ")}',
                    ),
                  ),
                );
                return;
              }
            },
            style: TextButton.styleFrom(
                foregroundColor: const Color.fromARGB(255, 0, 0, 0),
                backgroundColor: const Color.fromARGB(255, 32, 255, 170)),
            child: const Text("Verify Email")),
        TextButton(
            onPressed: () {
              Navigator.of(context)
                  .pushNamedAndRemoveUntil("/home", (route) => false);
            },
            style: TextButton.styleFrom(
                foregroundColor: const Color.fromARGB(255, 0, 0, 0),
                backgroundColor: const Color.fromARGB(255, 32, 255, 170)),
            child: const Text("Done"))
      ]),
    );
  }
}
