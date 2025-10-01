class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        sorted_words = sorted(freq.keys(), key=lambda x: (-freq[x], x))
        return sorted_words[:k]
