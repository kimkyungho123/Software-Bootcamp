//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class SimpleEchoClient {
    public SimpleEchoClient() {
    }

    public static void main(String[] args) {
        System.out.println("에코 클라이언트 시작됨");

        try {
            Socket clientSocket = null;
            PrintWriter pw = null;
            BufferedReader br = null;

            try {
                clientSocket = new Socket("165.246.115.165", 20000);
                pw = new PrintWriter(clientSocket.getOutputStream(), true);
                br = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                System.out.println("서버에 연결됨");
                Scanner sc = new Scanner(System.in);

                while(true) {
                    System.out.print("전송 메세지 입력 : ");
                    String line = sc.nextLine();
                    if ("exit".equalsIgnoreCase(line)) {
                        break;
                    }

                    pw.println(line);
                    System.out.println("서버로 부터 받은 메아리 : " + br.readLine());
                }
            } catch (IOException var10) {
                System.out.println("입출력 예외 발생");
            } finally {
                clientSocket.close();
                pw.close();
                br.close();
            }

        } catch (IOException var12) {
            throw new RuntimeException(var12);
        }
    }
}
