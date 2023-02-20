public class GenericMethodTest {
    static class Prints{
        public static <T> void printArray(T[] arr){
            for(T a : arr)
                System.out.println(a);
        }
    }

    public static void main(String[] args) {
        Double[] d1 = {3.14, 2.71, 9.9};
        Integer[] i1 = {10, 9, 7};
        String[] s1 = {"hi", "hello"};
        Prints.printArray(d1);
        Prints.printArray(i1);
        Prints.printArray(s1);
    }
}
