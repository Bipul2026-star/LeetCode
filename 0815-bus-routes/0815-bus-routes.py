class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = {}
        for i, route in enumerate(routes):
            for stop in route:
                graph.setdefault(stop, []).append(i)

        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = set()

        while queue:
            stop, buses = queue.popleft()

            for bus in graph.get(stop, []):
                if bus in visited_buses:
                    continue

                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1

                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses + 1))

        return -1

