public class HelloWorld {

public static void main(String args[]) {
        // hello world
        System.out.println("hello world");

        // variables in java
        int num1 = 5;
        int num2 = 10;
        int result = num1 + num2;
        System.out.println(result);

        // datatypes
        byte by = 127; // 1 byte
        short sh = 558; // 2 byte
        long ln = 2443l; // 8 byte, l is needed

        double db = 10.5; // 8 byte
        float fl = 10.5f; // 4 byte, f is needed

        char ch = 'a'; // 2 byte
        boolean bl = true; // 1 bit, only true and false

        // conversions
        byte a = 127;
        int b = 1000;
        a = (byte) b; // 1000%256 => 232 => 232 > 127 => 232-256 => -24
        System.out.println(a);

        // type promotion
        byte x = 5, y = 100;
        int res = x * y;
        System.out.println(res);

        // short hand operator
        int c = 10;
        c = c + 2;
        c += 2;
        c++;
        System.out.println(c++);
        System.out.println(c);

        // conditional statements
        int x1 = 10, x2 = 15, x3 = 20;
        if (x1 > x2 && x1 > x3) {
            System.out.println(x1);
        } else if (x2 > x1 && x2 > x3) {
            System.out.println(x2);
        } else {
            System.out.println(x3);
        }

        // ternary operator
        int number = 24;
        boolean isEven = (number % 2 == 0) ? true : false;
        System.out.println(isEven);

        // switch
        int dayNo=4;
        switch(dayNo)
        {
        case 1: System.out.println("Monday");
                break;
        case 2: System.out.println("Tuesday");
                break;
        case 3: System.out.println("Wednesday");
                break;
        case 4: System.out.println("Thusrday");
                break;
        case 5: System.out.println("Friday");
                break;
        case 6: System.out.println("Saturday");
                break;
        case 7: System.out.println("Sunday");
                break;
        default:
                System.out.println("Wrong number!");
        }

        // switch updated
        String dayName = switch(dayNo)
        {
            case 1 -> "Monday";
            case 2 -> "Tuesday";
            case 3 -> "Wednesday";
            case 4 -> "Thursday";
            case 5 -> "Friday";
            case 6 -> "Saturday";
            case 7 -> "Sunday";
            default -> "Wrong number";
        };
        System.out.println(dayName);
        // '->' can replaced with a colon and yield keyword (eg: case 1: yield "Monday;")
    }
}
