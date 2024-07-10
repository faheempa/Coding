import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';
import 'package:notes/services/auth/auth_exceptions.dart';
import 'package:notes/services/auth/auth_service.dart';
import 'package:notes/utils/functions.dart';

class LoginView extends StatefulWidget {
  const LoginView({super.key});

  @override
  State<LoginView> createState() => _LoginViewState();
}

class _LoginViewState extends State<LoginView> {
  // text controllers
  late final TextEditingController _email, _password;

  @override
  void initState() {
    _email = TextEditingController();
    _password = TextEditingController();
    super.initState();
  }

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
        backgroundColor: const Color.fromARGB(255, 32, 255, 170),
      ),
      body: Column(
        children: [
          TextField(
            controller: _email,
            keyboardType: TextInputType.emailAddress,
            decoration: const InputDecoration(border: OutlineInputBorder(), labelText: 'Email Address'),
          ),
          TextField(
            controller: _password,
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              labelText: 'Password',
            ),
            autocorrect: false,
            obscureText: true,
            enableSuggestions: false,
          ),
          TextButton(
            onPressed: () async {
              if (_email.text.isEmpty || _password.text.isEmpty) {
                popUpFromBottom('Please fill in all fields', context);
                return;
              }
              try {
                await AuthService.instance()
                    .login(
                      email: _email.text,
                      password: _password.text,
                    )
                    .then((value) => {
                          if (AuthService.instance().currentUser?.isEmailVerified == false)
                            {
                              popUpFromBottom("Please verify your email address", context),
                              AuthService.instance().sendEmailVerification(),
                              AuthService.instance().logout(),
                              Navigator.of(context).pushNamed(verifyEmailRoute),
                            }
                          else
                            {popUpFromBottom("Login successful", context), Navigator.of(context).pushNamedAndRemoveUntil(homeRoute, (route) => false)}
                        });
              } on InvalidEmailAuthException {
                popUpFromBottom("Invalid Email", context);
              } on WrongPasswordAuthException {
                popUpFromBottom("Wrong Password", context);
              } on UserNotFoundAuthException {
                popUpFromBottom("User Not Found", context);
              } on GeneralAuthException {
                popUpFromBottom("Login Failed", context);
              } catch (e) {
                popUpFromBottom("Error: ${e.toString()}", context);
              }
            },
            child: const Text('Login'),
          ),
          TextButton(
            onPressed: () {
              Navigator.of(context).pushNamed(registerRoute);
            },
            child: const Text('No account? Register here'),
          ),
          TextButton(
              onPressed: () {
                Navigator.of(context).pushNamedAndRemoveUntil(homeRoute, (route) => false);
              },
              style:
                  TextButton.styleFrom(foregroundColor: const Color.fromARGB(255, 0, 0, 0), backgroundColor: const Color.fromARGB(255, 32, 255, 170)),
              child: const Text("Go Home")),
        ],
      ),
    );
  }
}
