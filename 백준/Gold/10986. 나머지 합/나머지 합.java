import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] S = new long[N]; // 합 배열
        long[] C = new long[M]; // 같은 나머지 인덱스를 카운트하는 배열

        long answer = 0;

        S[0] = sc.nextInt();

        for (int i = 1; i < N; i++) {
            S[i] = S[i-1] + sc.nextInt();
        }

        for (int i = 0; i < N; i++) {
            int remainder = (int) (S[i] % M);

            if (remainder == 0) answer++; // 0~i까지의 구간 합 자체가 0이면 정답에 더하기

            C[remainder]++; // 나머지가 같은 인덱스의 개수 카운팅
        }
        for (int i = 0; i < M; i++) {
            if (C[i] > 1) {
                answer = answer + (C[i] * (C[i] - 1) / 2); //나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
            }
        }
        System.out.println(answer);
    }
}
