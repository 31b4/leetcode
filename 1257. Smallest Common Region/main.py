class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        place_to_next_place = defaultdict(lambda : "")
        def construct_graph(regions):
            for region in regions:
                reversed_region = region[::-1]
                for i,place in enumerate(reversed_region):
                    if i == len(reversed_region) - 1:
                        continue
                    
                    place_to_next_place[reversed_region[i]] = reversed_region[len(reversed_region) - 1]

        construct_graph(regions)

        # construct graph 1
        graph1 = []
        graph2 = []
        def dfs(region,graph):
            graph.append(region)
            if region in place_to_next_place.keys():
                dfs(place_to_next_place[region],graph)

        dfs(region1, graph1)
        dfs(region2, graph2)
        min_options = []
        graph1_set = set(graph1)
        min_possible1 = (None, None)
        for i,v in enumerate(graph2):
            if v in graph1_set:
                min_options.append((i,v))
                break

        graph2_set = set(graph2)
        min_possible2 = (None, None)
        for i,v in enumerate(graph1):
            if v in graph2_set:
                min_possible2 = (i,v)
                min_options.append(min_possible2)
                break
        
        sorted_list = sorted(min_options,key=lambda x: x[0])
        return sorted_list[0][1]


        
