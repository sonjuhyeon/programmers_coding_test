from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_plays = defaultdict(int)
    genre_plays = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_plays[genre] += play
        genre_plays[genre].append(i)
    
    total_plays = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in total_plays:
        genre_dict = defaultdict(dict)
        for i in genre_plays[genre]:
            genre_dict[i] = plays[i]
        sorted_genre = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(2):
            answer.append(sorted_genre[i][0])
            if len(sorted_genre) == 1:
                break
    
    return answer