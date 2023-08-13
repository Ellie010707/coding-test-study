import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int i = 0;
        int j = N-1;
        int count = 0;

        int[] A = new int[N];

        for (int k = 0; k < N; k++) {
            A[k] = sc.nextInt();
        }

        Arrays.sort(A);

        while (i < j) {
            int sum = 0;
            sum = A[i] + A[j];
            if (sum < M) {
                i++;
            } else if (sum > M) {
                j--;
            } else {
                count++;
                i++;
                j--;
            }
        }
        System.out.println(count);
    }
}
