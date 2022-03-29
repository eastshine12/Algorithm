import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int count = Integer.parseInt(br.readLine());

        StringTokenizer st;
        
        Integer arr[][] = new Integer[count][2];

        for (int i = 0; i < arr.length; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        };
        
        Arrays.sort(arr,(o1,o2)->(o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]));

        int result = 0;
        int startTime = -1;
        int endTime = 0;
        for (int i = 0; i < arr.length; i++) {
            int c = 0;
            for (int j = i; j < arr.length; j++) {
                if(arr[j][0] != startTime && arr[j][0] > endTime) {
                    startTime = arr[j][0];
                    endTime = arr[j][1];
                    c++;
                }
            }
            if(c > result) result = c;
        }
        

        bw.write(String.valueOf(result));
        bw.flush();   
        bw.close();
        br.close();
    }
}