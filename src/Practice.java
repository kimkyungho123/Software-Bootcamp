import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
        int result = 1;
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.print("팩토리얼 값을 구할 정수 : ");
        n = sc.nextInt();

        while (true) {
            result *= n;
            n--;
            if (n==0)
                break;
        }
        System.out.println(result);
    }
}
