import 'package:flutter/material.dart';
import 'package:notes/constants/routes.dart';
import 'package:notes/services/auth/auth_service.dart';
import 'package:notes/utils/functions.dart';

class HomeView extends StatefulWidget {
  const HomeView({super.key});

  @override
  State<HomeView> createState() => _HomeViewState();
}

class _HomeViewState extends State<HomeView> {
  bool _loggedIn = AuthService.instance().currentUser != null;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Notes"),
        backgroundColor: const Color.fromARGB(255, 32, 255, 170),
        actions: [
          if (_loggedIn == true)
            IconButton(
              onPressed: () {
                try {
                  showLogoutDialog(context).then(
                    (value) => {
                      if (value == true)
                        {
                          AuthService.instance().logout().then(
                                (value) => {popUpFromBottom("Logout Successful", context)},
                              ),
                          setState(() {
                              _loggedIn = false;
                            },
                          ),
                        },
                    },
                  );
                } catch (e) {
                  popUpFromBottom(e.toString(), context);
                }
              },
              icon: const Icon(Icons.logout),
            ),
          if (_loggedIn == false)
            IconButton(
              onPressed: () {
                Navigator.of(context).pushNamed(loginRoute);
              },
              icon: const Icon(Icons.login),
            ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Welcome to Notes"),
            if (_loggedIn == true)
              TextButton(
                onPressed: () {
                  Navigator.of(context).pushNamed(homeRoute);
                },
                child: const Text("Add Note"),
              ),
            if (_loggedIn == false)
              TextButton(
                onPressed: () {
                  Navigator.of(context).pushNamed(loginRoute);
                },
                child: const Text("Login"),
              ),
          ],
        ),
      ),
    );
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
