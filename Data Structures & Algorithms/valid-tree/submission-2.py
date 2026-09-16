class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()

        edge_dict = {}

        for edge in edges:
            if edge[0] not in edge_dict:
                edge_dict[edge[0]] = []
            edge_dict[edge[0]].append(edge[1])

            if edge[1] not in edge_dict:
                edge_dict[edge[1]] = []
            edge_dict[edge[1]].append(edge[0])


        for i in range(n):
            if i not in seen and i == 0:

                queue = [[None, i]]

                while queue:
                    ele = queue.pop()
                    x = ele[1]
                    if x in seen and x != ele[0]:
                        #print(x)
                        return False
                    seen.add(x)
                    if x in edge_dict:
                        for newele in edge_dict[x]:
                            if newele not in seen:
                                queue.append([x, newele])
            elif i not in seen:
                return False
                    

        


        return True