from collections import defaultdict, deque

NQvlaues = input()
NQvlaues = NQvlaues.split()
N = int(NQvlaues[0])
Q = int(NQvlaues[1])


#그래프 저장할 딕셔너리 선언
graph_dict = defaultdict(list)

#유사도 받기 n-1 반복
for i in range(N-1):
    usadoVal = input()
    usadoVal = usadoVal.split()
    nodeP = int(usadoVal[0])
    nodeQ = int(usadoVal[1])
    betweenUsado = int(usadoVal[2])
    #nodeP,Q 사이의 usado 저장
    graph_dict[nodeP-1].append((nodeQ-1,betweenUsado))
    graph_dict[nodeQ-1].append((nodeP-1,betweenUsado))
print(graph_dict)

def find_video(K,showNode,graph_dict):

    visited = [False]*(N)
    need_visit = [[showNode, 1000000000]] #확인해야할 번호와 유사도(일단 최대로 초기화)
    #추천받으면 True / 못받은 것들은 False => true 개수 읽고 출력
    
    while need_visit:
        for nextNode, 
        visitNode, usado = need_visit.pop()
        if visited[visitNode] == False and usado > graph_dict[1][0][0]

__

#그래프 저장할 딕셔너리 선언
graph_dict = defaultdict(list)

#유사도 받기 n-1 반복
for i in range(N-1):
    usadoVal = input()
    usadoVal = usadoVal.split()
    nodeP = int(usadoVal[0])
    nodeQ = int(usadoVal[1])
    betweenUsado = int(usadoVal[2])
    #nodeP,Q 사이의 usado 저장
    graph_dict[nodeP-1].append((nodeQ-1,betweenUsado))
    graph_dict[nodeQ-1].append((nodeP-1,betweenUsado))
print(graph_dict)
question_dict= defaultdict(list)
#(usado 기준 k , 현재 보고있는 동영상 )==> 몇개의 동영상 추천이 될까? Q번 물어봄
for i in range(Q):
    question = input()
    question = question.split()
    K = int(question[0])
    showNode = int(question[1])

    #질문저장 딕셔너리
    
    print(find_video(K,showNode,graph_dict))


print(question_dict[1][0][0])

