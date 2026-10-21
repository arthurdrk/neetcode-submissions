class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for x in tasks:
            count[x]+=1
        heap=[]
        for x in count:
            heapq.heappush(heap,(-count[x],x))

        cooldown = deque()  # (cycle de retour, fréquence négative, tâche)
        time = 0

        while heap or cooldown:
            # Remettre les tâches dont le cooldown est terminé
            while cooldown and cooldown[0][0] <= time:
                _, freq, task = cooldown.popleft()
                heapq.heappush(heap, (freq, task))

            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1  # Une occurrence en moins : -3 devient -2

                if freq < 0:
                    cooldown.append((time + n + 1, freq, task))

            # Si aucune tâche n'est disponible, ce cycle est idle
            time += 1

        return time