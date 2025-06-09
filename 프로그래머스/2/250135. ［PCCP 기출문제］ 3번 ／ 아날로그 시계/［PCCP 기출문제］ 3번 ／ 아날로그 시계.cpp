#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int get_second(int h, int m, int s) {
    return (h * 3600) + (m * 60) + s;
}

int get_count(int sec) {
    int res = 1;

    double hour = (sec * 719.0) / 43200;   // 초침-시침 만남 (12시간에 719회)
    double minute = (sec * 59.0) / 3600;   // 초침-분침 만남 (1시간에 59회)

    res += floor(hour) + floor(minute);

    if (sec >= 43200) res -= 1;  // 정오 보정
    return res;
}

double get_hour_position(int h, int m) {
    return (h % 12) * 5.0 + (m * 5.0 / 60);
}

double get_minute_position(int m, int s) {
    return m + (s / 60.0);
}

int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
    int midnight_to_sec1 = get_second(h1, m1, s1);
    int midnight_to_sec2 = get_second(h2, m2, s2);

    int count1 = get_count(midnight_to_sec1);
    int count2 = get_count(midnight_to_sec2);

    int answer = count2 - count1;

    double hour_position = get_hour_position(h1, m1);
    double minute_position = get_minute_position(m1, s1);

    if (fabs(s1 - hour_position) < 1e-6 || fabs(s1 - minute_position) < 1e-6) {
        answer += 1;
    }

    return answer;
}
