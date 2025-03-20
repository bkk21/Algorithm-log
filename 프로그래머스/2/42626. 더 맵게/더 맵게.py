import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 최소 힙으로 변환 (O(N))
    answer = 0

    while scoville[0] < K:
        if len(scoville) < 2:  # 섞을 음식이 부족하면 -1 반환
            return -1

        # 가장 맵지 않은 두 개의 음식 섞기
        first = heapq.heappop(scoville)  # 최소값 추출 (O(log N))
        second = heapq.heappop(scoville)  # 두 번째 최소값 추출 (O(log N))
        new_scoville = first + (second * 2)

        heapq.heappush(scoville, new_scoville)  # 새로운 음식 추가 (O(log N))

        answer += 1

    return answer
