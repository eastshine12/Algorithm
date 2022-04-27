import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int count = Integer.parseInt(br.readLine());

        StringTokenizer st;
        
        Integer arr[] = new Integer[count];
        Integer arr2[] = new Integer[count];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < count; i++) {  
            arr[i] = Integer.parseInt(st.nextToken());
        };
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < count; i++) {  
            arr2[i] = Integer.parseInt(st.nextToken());
        };
        
        Arrays.sort(arr);
        Arrays.sort(arr2, Collections.reverseOrder());

        int result = 0;
        for (int i = 0; i < count; i++) {
            result += arr[i] * arr2[i];
        }
        
        bw.write(String.valueOf(result));
        bw.flush();   
        bw.close();
        br.close();
    }
}