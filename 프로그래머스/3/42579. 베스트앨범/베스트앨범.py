# 7: 46
from collections import defaultdict

def solution(genres, plays):
    songs = []
    
    genre_info = defaultdict(int) #장르, 재생 횟수
    for k, v in zip(genres, plays): genre_info[k] += v    
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        songs.append((genre_info[genre], play, -(i+1)))
        
    songs.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)
    
    genre_count = defaultdict(int)
    answer = []
    for genre, song, k in songs:
        if genre_count[genre] < 2:
            answer.append(-(k+1))
            genre_count[genre] += 1
            
        
    return answer