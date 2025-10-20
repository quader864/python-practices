def queranumeric(order: list[str], words: list[str]) -> list[str]:
    rank = {ch: i for i, ch in enumerate(order)}
    max_rank = len(order)
    def key_func(word: str):
        return [rank.get(ch, max_rank) for ch in word]
    return sorted(words, key=key_func)

