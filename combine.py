# In this program's project folder, put the LocationGraph.txt file from the new graph you want to add
# and the graph.txt file from the orignal graph. It will create a newer graph file with the locations
# from the new graph added to the original one without changing the weights

with open("LocationGraph.txt") as f:
    newGraph = f.readlines()

stline = ""
edgeList = []

for line in newGraph:
    stline = line.split(" ")
    edgeList.append(stline)

del edgeList[0]
print edgeList

oldGraph = file("graph.txt")
cgraph = open('cgraph.txt', 'w')
i = 0
for line in oldGraph:
    stline = line.split(" ")
    print i
    if i < len(edgeList) and stline[0] == edgeList[i][0]:
        line = line[:-1]
        line = line + edgeList[i][1]
        cgraph.write(line)
        i = i + 1
    else:
        cgraph.write(line)

cgraph.close()
print edgeList[60]
