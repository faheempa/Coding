class Calc {
    public int add(int a, int b)
    {
        return a+b;
    }
    public int add(int a, int b, int c)
    {
        return a+b+c;
    }
    public double add(double a, double b)
    {
        return a+b;
    }
}

public class Calculator {

    public static void main(String args []) {
        Calc calc = new Calc();
        System.out.println(calc.add(1.3, 3.3));
        System.out.println(calc.add(1, 3));
        System.out.println(calc.add(1, 3, 5));
    }
}

