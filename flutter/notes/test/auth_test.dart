// testing auth service
import 'package:flutter_test/flutter_test.dart';
import 'package:notes/services/auth/auth_exceptions.dart';
import 'package:notes/services/auth/auth_provider.dart';
import 'package:notes/services/auth/auth_user.dart';

main() {
  group("Auth -> ", () {
    final provider = MockProvider();

    test("Not initialized", () async {
      expect(provider._isInitialized, false);
      expect(provider.createUser(email: "abcd@gmail.com", password: "123456"), throwsA(const TypeMatcher<NotInitilizedAuthException>()));
      expect(provider.login(email: "abcd@gmail.com", password: "123456"), throwsA(const TypeMatcher<NotInitilizedAuthException>()));
      expect(provider.logout(), throwsA(const TypeMatcher<NotInitilizedAuthException>()));
      expect(provider.sendEmailVerification(), throwsA(const TypeMatcher<NotInitilizedAuthException>()));
    });

    test("initilize", () async {
      await provider.initialize();
      expect(provider._isInitialized, true);
    }, timeout: const Timeout(Duration(seconds: 2)));

    test("create user", () async {
      expect(provider.createUser(email: "invalid@gmail.com", password: "123456"), throwsA(const TypeMatcher<InvalidEmailAuthException>()));
      expect(provider.createUser(email: "usedemail@gmail.com", password: "123456"), throwsA(const TypeMatcher<EmailAlreadyInUseAuthException>()));
      expect(provider.createUser(email: "abcd@gmail.com", password: "1234"), throwsA(const TypeMatcher<WeakPasswordAuthException>()));
      expect(provider.createUser(email: "abcd@gmail.com", password: "123456"), const TypeMatcher<Future<AuthUser?>>());
    }, timeout: const Timeout(Duration(seconds: 2)));

    test("login", () async {
      expect(provider._isLoggedIn, false);
      expect(provider.login(email: "invalid@gmail.com", password: "123456"), throwsA(const TypeMatcher<InvalidEmailAuthException>()));
      expect(provider.login(email: "abcd@gmail.com", password: "123456789"), throwsA(const TypeMatcher<WrongPasswordAuthException>()));
      expect(provider.login(email: "abcdefg@gmail.com", password: "123456"), throwsA(const TypeMatcher<UserNotFoundAuthException>()));
      expect(provider.login(email: "abcd@gmail.com", password: "123456"), const TypeMatcher<Future<AuthUser?>>());
      expect(provider._isLoggedIn, false);
      await Future.delayed(const Duration(seconds: 1));
      expect(provider._isLoggedIn, true);
    });

    test("get current user", () async {
      final user = provider.currentUser;
      expect(user, isNotNull);
      expect(user, const TypeMatcher<AuthUser?>());
    });

    test("email verification", () async {
      expect(provider._isEmailVerified, false);
      await provider.sendEmailVerification();
      expect(provider._isEmailVerified, true);
    });

    test("logout", () async {
      expect(provider._isLoggedIn, true);
      await provider.logout();
      expect(provider._isLoggedIn, false);
      expect(provider.logout(), throwsA(const TypeMatcher<UserNotLoggedInAuthException>()));
    });

    test("final", () async {
      expect(provider._isInitialized, true);
      expect(provider._isLoggedIn, false);
      expect(provider._isEmailVerified, true);
      expect(provider.sendEmailVerification(), throwsA(const TypeMatcher<UserNotLoggedInAuthException>()));
    });

    
  });
}


class MockProvider implements AuthProvider {
  bool _isInitialized = false;
  bool _isLoggedIn = false;
  bool _isEmailVerified = false;

  @override
  Future<AuthUser?> createUser({required String email, required String password}) async {
    if (_isInitialized == false) {
      throw NotInitilizedAuthException();
    }
    await Future.delayed(const Duration(seconds: 1));
    if (email == "invalid@gmail.com") {
      throw InvalidEmailAuthException();
    } else if (email == "usedemail@gmail.com") {
      throw EmailAlreadyInUseAuthException();
    } else if (password.length < 6) {
      throw WeakPasswordAuthException();
    } else {
      await Future.delayed(const Duration(seconds: 1));
      return AuthUser(isEmailVerified: _isEmailVerified);
    }
  }

  @override
  // TODO: implement currentUser
  AuthUser? get currentUser => AuthUser(isEmailVerified: _isEmailVerified);

  @override
  Future<void> initialize() async {
    await Future.delayed(const Duration(seconds: 1));
    _isInitialized = true;
    return Future.value();
  }

  @override
  Future<AuthUser?> login({required String email, required String password}) async {
    if (_isInitialized == false) {
      throw NotInitilizedAuthException();
    }
    if (email == "invalid@gmail.com") {
      throw InvalidEmailAuthException();
    } else if (email == "abcd@gmail.com" && password != "123456") {
      throw WrongPasswordAuthException();
    } else if (email == "abcd@gmail.com" && password == "123456") {
      await Future.delayed(const Duration(seconds: 1));
      _isLoggedIn = true;
      return Future.value(AuthUser(isEmailVerified: _isEmailVerified));
    } else {
      throw UserNotFoundAuthException();
    }
  }

  @override
  Future<void> logout() async {
    if (_isInitialized == false) {
      throw NotInitilizedAuthException();
    }
    if (_isLoggedIn == false) {
      throw UserNotLoggedInAuthException();
    }

    await Future.delayed(const Duration(seconds: 1));
    _isLoggedIn = false;
    return Future.value();
  }

  @override
  Future<void> sendEmailVerification() async {
    if (_isInitialized == false) {
      throw NotInitilizedAuthException();
    }
    if (_isLoggedIn == false) {
      throw UserNotLoggedInAuthException();
    }

    await Future.delayed(const Duration(seconds: 1));
    _isEmailVerified = true;

    return Future.value();
  }
}
