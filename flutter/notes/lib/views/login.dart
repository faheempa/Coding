import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

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
    final user = FirebaseAuth.instance.currentUser;
    if (user != null) {
      Navigator.of(context).pushNamedAndRemoveUntil('/home/', (route) => false);
    }
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
          TextButton(
            onPressed: () async {
              if (_email.text.isEmpty || _password.text.isEmpty) {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Please fill in all fields'),
                  ),
                );
                return;
              }
              try {
                await FirebaseAuth.instance
                    .signInWithEmailAndPassword(
                      email: _email.text,
                      password: _password.text,
                    )
                    .then((value) => {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                              content: Text('Login successfully'),
                            ),
                          ),
                          _email.text = '',
                          _password.text = '',
                          // focus out
                          Navigator.of(context).pushNamedAndRemoveUntil(
                              '/home', (route) => false)
                        });
              } on FirebaseAuthException catch (e) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      // capitalize the error code and replace "-" with " "
                      'Login failed: ${e.code[0].toUpperCase() + e.code.substring(1).replaceAll("-", " ")}',
                    ),
                  ),
                );
              }
            },
            child: const Text('Login'),
          ),
          TextButton(
            onPressed: () {
              Navigator.of(context)
                  .pushNamedAndRemoveUntil('/register', (route) => false);
            },
            child: const Text('No account? Register here'),
          ),
        ],
      ),
    );
  }
}
