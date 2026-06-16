# utils.py -- 매출 분석 함수 모음

# 1. A등급 성과급률 5.0으로 수정 완료
INCENTIVE_TABLE = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "F": 0.0}

def total_sales(branch):
    """지점 총매출."""
    return branch["1분기"] + branch["2분기"] + branch["3분기"]

def average_sales(branch):
    """지점 평균."""
    # 2. 딕셔너리 길이(4)가 아닌 정확한 분기 수(3)로 나누도록 수정
    return total_sales(branch) / 3

def to_grade(avg):
    """평균을 등급으로 변환."""
    if avg >= 120: return "A"
    elif avg >= 100: return "B"
    elif avg >= 80: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def grade_to_incentive(grade):
    """등급을 성과급률로 변환."""
    return INCENTIVE_TABLE[grade]

def quarter_average(branches, quarter):
    """분기 평균."""
    if not branches: return 0.0
    total = 0
    for b in branches:
        # 3. "1분기" 하드코딩 삭제, 요청받은 분기(quarter) 변수 사용
        total += b[quarter]
    return total / len(branches)

def quarter_top(branches, quarter):
    """분기 최고."""
    if not branches: return 0
    top = 0
    for b in branches:
        # 4. 기존 top보다 클 때만 갱신 (부등호 방향 정상화)
        if b[quarter] > top: 
            top = b[quarter]
    return top

def grade_distribution(branches):
    """등급별 지점 수."""
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for b in branches:
        g = to_grade(average_sales(b))
        dist[g] += 1
    return dist

def rank_list(branches):
    """총매출 기준 정렬."""
    # 5. 총매출이 높은 순서대로 1위가 되도록 내림차순(reverse=True) 적용
    return sorted(branches, key=lambda x: total_sales(x), reverse=True)

def achievement_rate(branches, target=90):
    """목표 달성 비율(%)."""
    if not branches: return 0.0
    count = 0
    for b in branches:
        if average_sales(b) >= target:
            count += 1
    return (count / len(branches)) * 100
