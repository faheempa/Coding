public class Loops {
    public static void main(String args [])
    {
        int i=0;
        System.out.println("while loop start");
        while(i<10)
        {
            System.out.println(i);
            i++;
        }
        System.out.println("while loop end");

        System.out.println("for loop start");
        for(i=0; i<10; i++)
        {
            System.out.println(i);
        }
        System.out.println("for loop end");

        System.out.println("do while loop start");
        do 
        {
            System.out.println(i);
            i++;
        } while(i<10);
        System.out.println("do while loop end");
    }
}
 