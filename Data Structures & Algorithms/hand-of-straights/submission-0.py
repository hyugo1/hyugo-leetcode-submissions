class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hashmap = {} # key, freq
        for h in hand:
            hashmap[h] = 1 + hashmap.get(h, 0)
        for n in sorted(hashmap):
            while hashmap[n] > 0: #while freq is not 0
                for i in range(groupSize):
                    if hashmap.get(n + i, 0) == 0:
                        return False
                    hashmap[n + i] -= 1
        return True