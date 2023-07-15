import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  bool _loggedIn = FirebaseAuth.instance.currentUser != null;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Home"),
          backgroundColor: const Color.fromARGB(255, 32, 255, 170),
          actions: [
            if (_loggedIn == true)
              IconButton(
                onPressed: () {
                  showLogoutDialog(context).then(
                    (value) => {
                      debugPrint(value.toString()),
                      if (value == true) logout(),
                    },
                  );
                },
                icon: const Icon(Icons.logout),
              ),
            if (_loggedIn == false)
              IconButton(
                onPressed: () {
                  Navigator.of(context)
                      .pushNamedAndRemoveUntil(loginRoute, (route) => false);
                },
                icon: const Icon(Icons.login),
              ),
          ],
        ),
        body: const Center(child: Text("Home")));
  }

  void logout() {
    FirebaseAuth.instance.signOut().then(
          (value) => {
            ScaffoldMessenger.of(context).showSnackBar(
              const SnackBar(
                content: Text('Logged out successfully.'),
              ),
            ),
          },
        );
    setState(() {
      _loggedIn = false;
    });
  }
}

Future<bool> showLogoutDialog(BuildContext context) {
  return showDialog<bool>(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: const Text("Logout"),
        content: const Text("Are you sure you want to logout?"),
        actions: [
          TextButton(
              onPressed: () {
                Navigator.of(context).pop(false);
              },
              child: const Text("No")),
          TextButton(
              onPressed: () {
                Navigator.of(context).pop(true);
              },
              child: const Text("Yes")),
        ],
      );
    },
  ).then((value) => value ?? false);
}
