import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import "package:firebase_auth/firebase_auth.dart";
import 'firebase_options.dart';

void main() {
  runApp(MaterialApp(
    title: 'Flutter Demo',
    theme: ThemeData(
      useMaterial3: true,
    ),
    home: const HomePage(),
  ));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // text controller for email, password and confirm password
  late final TextEditingController _email;
  late final TextEditingController _password;
  late final TextEditingController _confirmPassword;

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
        backgroundColor: const Color.fromARGB(255, 108, 255, 157),
      ),
      body: FutureBuilder(
        // Initialize FlutterFire before rendering the form
        future: Firebase.initializeApp(
          options: DefaultFirebaseOptions.currentPlatform,
        ),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.done: // if firebase is done initializing
              return Column(
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
                      if (_password.text != _confirmPassword.text) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text('Password does not match'),
                          ),
                        );
                        return;
                      }
                      try {
                        await FirebaseAuth.instance
                            .createUserWithEmailAndPassword(
                              email: _email.text,
                              password: _password.text,
                            )
                            .then((value) => {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    const SnackBar(
                                      content:
                                          Text('User created successfully'),
                                    ),
                                  ),
                                  _email.text = '',
                                  _password.text = '',
                                  _confirmPassword.text = '',
                                  // focus out
                                  FocusScope.of(context).unfocus(),
                                });
                      } on FirebaseAuthException catch (e) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(
                            content: Text(e.message ?? 'Error'),
                          ),
                        );
                      }
                    },
                    child: const Text('Register'),
                  ),
                ],
              );
            default: // if firebase is not done initializing
              return const Center(
                child: CircularProgressIndicator(),
              );
          }
        },
      ),
    );
  }
}
