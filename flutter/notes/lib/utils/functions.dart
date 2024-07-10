import 'package:flutter/material.dart';

Material customErrorScreen()
{
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
  );
}

void popUpFromBottom(String s, context) {
  ScaffoldMessenger.of(context).showSnackBar(
    SnackBar(
      content: Text(s),
    ),
  );
}
