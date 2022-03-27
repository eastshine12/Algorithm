import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        // int a = Integer.parseInt(br.readLine());
        
        int answer = 2500;
        char arr[][] = new char[a][b];
        for (int i = 0; i < arr.length; i++) {
            String str = br.readLine();
            for (int j = 0; j < arr[i].length; j++) {
                arr[i][j] = str.charAt(j);
            }    
        }

        boolean bool = true;
        int aCount = 0;
        int bCount = 0;
        int caseB = 0;
        int caseW = 0;
        while(bool) {
            int a2 = a - 8;
            int b2 = b - 8;
            caseB = 0;
            caseW = 0;
            for (int i = 0 + aCount; i < 8 + aCount; i++) {
                for (int j = 0 + bCount; j < 8 + bCount; j++) {

                    if(arr[0+aCount][0+bCount] == 'B') {
                        if(j % 2 == 0 && arr[i][j] != 'B') {
                            caseB++;
                        } else if(j % 2 == 1 && arr[i][j] != 'W') {
                            caseB++;
                        }
                    } else {
                        if(j % 2 == 0 && arr[i][j] != 'W') {
                            caseW++;
                        } else if(j % 2 == 1 && arr[i][j] != 'B') {
                            caseW++;
                        }
                    }
                }
                
            }

            System.out.println("caseB="+caseB + " caseW=" +caseW);
            if (answer > caseB) {
                answer = caseB;
            } else if (answer > caseW) {
                answer = caseW;
            } 

            if(a2 != 0) {
                a2--;
                aCount++;
            } else {
                bool = false;
            }
            
            if(b2 != 0) {
                b2--;
                bCount++;
            } else {
                bCount = 0;
            }

        }

        
        System.out.println(answer);



    }
}