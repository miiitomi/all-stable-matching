import sys
sys.setrecursionlimit(10**6)

def dfs(G: list[list[int]], v: int, reached: list[bool], lived: list[bool], cycle: list[int]) -> bool:
    reached[v] = True
    lived[v] = True
    cycle.append(v)
    for u in G[v]:
        if reached[u]:
            if lived[u]:
                i = cycle.index(u)
                cycle[:] = cycle[i:]
                return True
        elif dfs(G, u, reached, lived, cycle):
            return True
    cycle.pop()
    lived[v] = False


def find_cycle(G: list[list[int]]) -> list[int] | None:
    reached = [False for _ in range(len(G))]
    lived = [False for _ in range(len(G))]
    for v in range(len(G)):
        if not reached[v]:
            cycle = []
            if dfs(G, v, reached, lived, cycle):
                min_idx = cycle.index(min(cycle))
                cycle = cycle[min_idx:] + cycle[:min_idx]
                return cycle


def find_all_cycles(G: list[list[int]]) -> list[list[int]]:
    all_cycles = []
    reached = [False for _ in range(len(G))]
    lived = [False for _ in range(len(G))]
    for v in range(len(G)):
        if not reached[v]:
            cycle = []
            if dfs(G, v, reached, lived, cycle):
                min_idx = cycle.index(min(cycle))
                cycle = cycle[min_idx:] + cycle[:min_idx]
                all_cycles.append(cycle)
                lived = [False for _ in range(len(G))]
                continue
    return all_cycles



if __name__ == "__main__":
    G = [
        [1],
        [0],
        [3],
        [4],
        [2],
        [4]
        ]
    print(find_cycle(G))
    print(find_all_cycles(G))

