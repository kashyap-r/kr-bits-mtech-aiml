import time
import collections

#读取地图，压缩为一维矩阵
def graph():
    map=[]
    for i in range(4):
        num = input().split()
        for j in range(4):
            map.append(int(num[j]))
    return tuple(map)

#得到邻居节点
def getNeighbour(map):
    for i in range(16):
        if map[i] == 0:
            break
    neighbour = []
        #空白格的移动方向
    move = {
            'left': -1,
            'down': 4,
            'up': -4,
            'right': 1
            }
    for direc in move:
        if i + move[direc] < 16 and i + move[direc] >= 0:
            if i + move[direc] > i:
                x,y = i,i+move[direc]
            else:
                x,y = i+move[direc],i
            map_ = map[:x]+map[y:y+1]+map[x+1:y]+map[x:x+1]+map[y+1:]
            if solvable(map_):
                neighbour.append((map_,map_[i]))
    return sorted(neighbour,key=lambda x:[manhatten(x[0])])

#计算曼哈顿距离
def manhatten(map):
    dist = 0
    for i in range(16):
        if map[i] != 0:
            j = map[i]-1
            dist += abs(i-j)/4
            dist += abs((i % 4) - (j % 4))
    return dist*1.014

#通过逆序性判断有无解
def solvable(map):
    cnt = 0
    flag = 0
    for i in range(16):
            if map[i] == 0:
                flag = int(i/4)
                continue
            for j in range(i,16):
                if map[j] == 0:
                    continue
                if map[i] > map[j]:
                    cnt+=1
    return (cnt + flag) % 2 != 0   

#深度遍历搜索
count = 0
def dfs(path,g,bound,visited):
    #判断有无解
    node = list(path.keys())[-1]
    f = g + manhatten(node)
    if f > bound:
        return f
    if node == goal:
        return -1
    min = 9999
    global count
    nei = getNeighbour(node)
    for n in nei:
        if n[0] not in visited or visited[n[0]] >= g:
            visited.update({n[0]:g})    
            if n[0] not in path:
                path.update({n[0]:n[1]})
                t = dfs(path,g+1,bound,visited)
                count += 1
                print(count,t,sep=' ')
                if t == -1:
                    return -1
                if t < min:
                    min = t
                path.pop(n[0])
    return min

def IDAstar(map):
    bound = manhatten(map)
    path = collections.OrderedDict({map:0})
    visited = {}
    while(True):
        t = dfs(path, 0, bound, visited)
        if t == -1:
            return (path, bound)
        if t > 70:
            return ([], bound)
        bound += 2

        
    
                
    
    
goal = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0)
def main():
    map = graph()
    time_start=time.time()
    path,bound = IDAstar(map)
    time_end=time.time()
    cnt = 0
    print('bound:',bound,sep=' ')
    for p in path:
        #print('step',cnt,sep=' ',end=' ')
        cnt+=1
        if cnt == 1:
            continue
        print(path[p],end=' ')
        #for i in range(4):
            #for j in range(4):
                #print(p[i*4+j],end=' ')
            #print()
    print('\nA optimal solution',cnt-1,'moves',sep=' ')
    print('It cost ',time_end-time_start,'s',sep='') #此处单位为秒
        
    
    
    

main()