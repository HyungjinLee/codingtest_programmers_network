# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def solution(n, computers):
    answer = 0
    visited = [[0] * n for _ in range (n)]
    k = 0
    # dfs
    def dfs(node) :
        stack = [node]
        while stack :
            cur = stack.pop()
            for i in range (len(computers)) :
                if not visited[cur][i] and computers[cur][i] :
                    stack.append(i)
                    visited[cur][i] = 1
                    visited[i][cur] = 1
    for i in range (len(computers)) :
        if not visited[i][i] :
            dfs(i)
            answer+=1
    return answer