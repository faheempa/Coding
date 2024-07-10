class Student
{
    int rollno;
    String name;
    int marks;

    Student(int rollno, String name, int marks)
    {
        this.name=name;
        this.rollno=rollno;
        this.marks=marks;
    }
}

public class Arrays {
    public static void main(String args[]) {
        int arr[][] = new int[3][4];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        for (int num[] : arr) {
            for (int value : num) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
        System.out.println();

        // jagged arrays
        int jarr[][] = new int[3][];
        jarr[0] = new int[3];
        jarr[1] = new int[4];
        jarr[2] = new int[5];

        for (int i = 0; i < jarr.length; i++) {
            for (int j = 0; j < jarr[i].length; j++) {
                System.out.print(jarr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
        for (int num[] : jarr) {
            for (int value : num) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
        System.out.println();

        // array of objects
        Student student_arr[] = new Student[3];
        student_arr[0]=new Student(1, "Faheem", 92);
        student_arr[1]=new Student(2, "Pranav", 95);
        student_arr[2]=new Student(3, "Alan", 78);
        for (Student stud: student_arr)
        {
            System.out.println(stud.name + ": " + stud.marks);
        }
    }
}
