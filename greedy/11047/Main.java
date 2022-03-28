import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = Integer.parseInt(st.nextToken());
        int total = Integer.parseInt(st.nextToken());
        Integer arr[] = new Integer[count];
        for (int i = 0; i < count; i++) {
            arr[count-1-i] = Integer.parseInt(br.readLine());
        };
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            result += total / arr[i];
            total -= arr[i] * (total / arr[i]);
        }

        bw.write(String.valueOf(result));
        bw.flush();   
        bw.close();
        br.close();
    }
}