import '../views/home.dart';
import '../views/login.dart';
import '../views/register.dart';
import '../views/verify_email.dart';

const loginRoute = '/login';
const registerRoute = '/register';
const verifyEmailRoute = '/verify_email';
const homeRoute = '/home';

var appRoutes = {
  loginRoute: (context) => const LoginView(),
  registerRoute: (context) => const RegisterView(),
  verifyEmailRoute: (context) => const VerifyEmail(),
  homeRoute: (context) => const HomeView(),
};
