import java.util.Arrays;
import java.util.Comparator;

public class StringDemoTest {
    public static void main(String[] args) {
        String[] strings = {"hi", "hello friend", "hello professor"};

//        Arrays.sort(strings);
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o2.length() - o1 .length();
            }
        });
        for(String s : strings)
            System.out.println(s);
    }
}
