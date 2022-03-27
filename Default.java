class Default {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();    // 문자열
        int count = Integer.parseInt(br.readLine());    // 정수
        
        StringTokenizer st = new StringTokenizer(br.readLine()); // 한줄에 입력값 여러개 있을 때

        int arr[] = new int[count];
        for(int i = 0; i < count; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        bw.write(str);  //문자열
        bw.write(String.valueOf(count)); //정수
        
        
        bw.flush();   
        bw.close();
        br.close();
}
