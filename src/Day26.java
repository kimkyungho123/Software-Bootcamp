public class Day26 {
        private String secret = "Day26의 캡슐화된 인스턴스 변수";
        String s = "Day26의 인스턴스 변수";

        class MemberClass {
            String s = "Day26안의 MemberClass의 인스턴스 변수";

            public void show() {
                System.out.println("Inner Class");
                System.out.println(secret); // MemberClass안에 secret 변수가 존재하지 않아서 바깥 스코프의 secret 변수 값을 출력한다.

                System.out.println(s); // MemberClass안에 s 변수가 존재

                System.out.println(Day26.this.s); // Day26의 인스턴스 변수 s의 값을 출력
            }

            // static String s3 = "정적 멤버 필드";
            // static void show2() {}
        }

        public static void main(String[] args) {
            Day26 m = new Day26();
            Day26.MemberClass mc = m.new MemberClass();

            System.out.println(mc.s);
            mc.show();
        }
}
