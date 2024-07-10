import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';
import 'package:notes/services/auth/auth_exceptions.dart';
import 'package:notes/services/auth/auth_service.dart';
import 'package:notes/utils/functions.dart';

class RegisterView extends StatefulWidget {
  const RegisterView({super.key});

  @override
  State<RegisterView> createState() => _RegisterViewState();
}

class _RegisterViewState extends State<RegisterView> {
  // text controllers
  late final TextEditingController _email, _password, _confirmPassword;

  @override
  void initState() {
    _email = TextEditingController();
    _password = TextEditingController();
    _confirmPassword = TextEditingController();
    super.initState();
  }

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    _confirmPassword.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Register'),
        backgroundColor: const Color.fromARGB(255, 32, 255, 170),
      ),
      body: Column(
        children: [
          TextField(
            controller: _email,
            keyboardType: TextInputType.emailAddress,
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              labelText: 'Email Address',
            ),
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
          TextField(
            controller: _confirmPassword,
            decoration: const InputDecoration(
              border: OutlineInputBorder(),
              labelText: 'Confirm Password',
            ),
            autocorrect: false,
            obscureText: true,
            enableSuggestions: false,
          ),
          TextButton(
            onPressed: () async {
              if (_email.text.isEmpty || _password.text.isEmpty || _confirmPassword.text.isEmpty) {
                popUpFromBottom('Please fill in all fields', context);
                return;
              }
              if (_password.text != _confirmPassword.text) {
                popUpFromBottom('Password does not match', context);
                return;
              }
              try {
                await AuthService.instance()
                    .createUser(email: _email.text, password: _password.text)
                    .then((value) => {
                          if (value == null)
                            {
                              popUpFromBottom('User already exists', context),
                            }
                          else
                            {popUpFromBottom('User created successfully', context)}
                        })
                    .then((value) => {
                          Navigator.of(context).pushNamedAndRemoveUntil(loginRoute, (route) => false),
                        });
              } on InvalidEmailAuthException {
                popUpFromBottom('Invalid Email', context);
              } on EmailAlreadyInUseAuthException {
                popUpFromBottom('Email already in use', context);
              } on WeakPasswordAuthException {
                popUpFromBottom('Password is too weak', context);
              } on GeneralAuthException {
                popUpFromBottom('Authentication Error', context);
              } catch (e) {
                popUpFromBottom("Error: ${e.toString()}", context);
              }
            },
            child: const Text('Register'),
          ),
          TextButton(
            onPressed: () {
              Navigator.of(context).pop();
            },
            child: const Text('Already have an account? Login'),
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
