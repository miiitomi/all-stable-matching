import sys
sys.setrecursionlimit(10**6)

def rec(G: list[list[int]], v: int, reached: list[bool], lived: list[bool], cycle: list[int]) -> bool:
    reached[v] = True
    lived[v] = True
    cycle.append(v)
    for u in G[v]:
        if reached[u]:
            if lived[u]:
                i = cycle.index(u)
                cycle[:] = cycle[i:]
                return True
        elif rec(G, u, reached, lived, cycle):
            return True
    cycle.pop()
    lived[v] = False


def dfs(G: list[list[int]]) -> list[int] | None:
    reached = [False for _ in range(len(G))]
    lived = [False for _ in range(len(G))]
    for v in range(len(G)):
        if not reached[v]:
            cycle = []
            if rec(G, v, reached, lived, cycle):
                return cycle


if __name__ == "__main__":
    G = [
        [1],
        [2],
        [3],
        [4],
        [3]
        ]
    res = dfs(G)
    print(res)
