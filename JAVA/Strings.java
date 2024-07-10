public class Strings {
    public static void main(String[] args) {
        String name = new String("Faheem");
        System.out.println(name);
        System.out.println(name.length());
        System.out.println(name.charAt(2));
        System.out.println(name + " PA");
        System.out.println(name.substring(0, 3));
        System.out.println(name.toLowerCase());
        System.out.println(name.toUpperCase());
        System.out.println(name.hashCode());
        
        String name2 = "Faheem";
        System.out.println(name==name2); // compare addresses, they are different
        System.out.println(name.equals(name2)); // compare content
        
        String name3 = "Faheem";
        System.out.println(name3==name2); // compare addresses, they are same
        System.out.println(name3.equals(name2)); // compare content

        // why?
        // In Java, the == operator checks whether two references point to the same object in memory. In your code:
        // String name = new String("Faheem"); creates a new String object in memory, regardless of whether the string literal "Faheem" already exists.
        // String name2 = "Faheem"; uses the string literal "Faheem", which is stored in the string pool (a special memory region for string literals).
        // When you compare name and name2 using ==, you're comparing their memory addresses, not their content. 
        // Since name is a new String object, it has a different memory address from name2, which points to the interned string literal.
        // Therefore, System.out.println(name == name2); will print false because name and name2 do not reference the same object in memory.
    }
}
