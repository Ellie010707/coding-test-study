import java.util.Map;
import java.util.TreeMap;


class Solution {
    
    public final int LASTTIME = 1439;
    
    public int[] solution(int[] fees, String[] records) {
       
        Map<String, Integer> map = new TreeMap<>();        

        int default_time = fees[0]; //기본 시간
        int default_fee = fees[1];  //기본 요금
        int unit_time = fees[2];    //단위 시간
        int unit_fee = fees[3];     //단위 요금
        
        for (String record : records) {
            String[] split_record = record.split(" ");
            String[] split_time = split_record[0].split(":");
            int tmp_time = (split_record[2].equals("IN") ? -1 : 1) * ((Integer.parseInt(split_time[0])*60) + Integer.parseInt(split_time[1]));
            String car = split_record[1];
            map.put(car, map.getOrDefault(car, 0) + tmp_time);
        }
        
        int i = 0;
        int[] answer = new int[map.size()];
        for (String key : map.keySet()) {
            int total_time = map.get(key);
            total_time = total_time <= 0 ? total_time + LASTTIME : total_time;
            double time = total_time - default_time < 0 ? 0 : total_time - default_time;
            int price = default_fee + (int)Math.ceil(time/unit_time) * unit_fee;
            answer[i++] = price;
        }
        
        return answer;
    }
}