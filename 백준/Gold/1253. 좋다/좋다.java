
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];

        for (int k = 0; k < N; k++) {
            A[k] = sc.nextInt();
        }

        Arrays.sort(A);
        int count = 0;
        for (int k = 0; k < N; k++) {
            int i = 0;
            int j = N - 1;

            while (i < j) {
                int sum = A[i] + A[j];
                if (sum > A[k]) {
                    j--;
                } else if (sum < A[k]) {
                    i++;
                }
                else {
                    if (i != k && j != k) {
                        count++;
                        break;
                    } else if (i == k) {
                        i++;
                    } else if (j == k) {
                        j--;
                    }
                }
            }
        }

        System.out.println(count);
    }
}
