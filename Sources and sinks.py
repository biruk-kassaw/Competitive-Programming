n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = []
sink = []

for i in range(len(graph)):
    is_source = True
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            is_source = False
    if is_source:
        source.append(i+1)

for i in range(len(graph[0])):
    is_sink = True
    for j in range(len(graph)):
        if graph[j][i] == 1:
            is_sink = False
    if is_sink:
        sink.append(i+1)

print(len(sink), *sink)
print(len(source), *source)
