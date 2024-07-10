import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';
import 'package:notes/services/auth/auth_exceptions.dart';
import 'package:notes/services/auth/auth_service.dart';
import '../utils/functions.dart';

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
        const Text("we have sent you a verification email, please check your mail"),
        const Text("if you have not received the email, please click the button below to resend it"),
        TextButton(
            onPressed: () async {
              try {
                await AuthService.instance().sendEmailVerification().then((value) => {
                      popUpFromBottom("Verification email was sent, please check your mail.", context),
                    });
              } on GeneralAuthException {
                popUpFromBottom("Something Went Wrong", context);
              } catch (e) {
                popUpFromBottom("Error: ${e.toString()}", context);
              }
            },
            style: TextButton.styleFrom(
              foregroundColor: const Color.fromARGB(255, 0, 0, 0),
              backgroundColor: const Color.fromARGB(255, 32, 255, 170),
            ),
            child: const Text("Resent Email")),
        TextButton(
            onPressed: () {
              Navigator.of(context).pop();
            },
            style: TextButton.styleFrom(
              foregroundColor: const Color.fromARGB(255, 0, 0, 0),
              backgroundColor: const Color.fromARGB(255, 32, 255, 170),
            ),
            child: const Text("Go back")),
        TextButton(
            onPressed: () {
              Navigator.of(context).pushNamedAndRemoveUntil(loginRoute, (route) => false);
            },
            style: TextButton.styleFrom(
              foregroundColor: const Color.fromARGB(255, 0, 0, 0),
              backgroundColor: const Color.fromARGB(255, 32, 255, 170),
            ),
            child: const Text("Login")),
      ]),
    );
  }
}
