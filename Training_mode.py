# === Training Mode ===
def train_unit(unit, start_word=None, end_word=None):
    vocab = load_vocab()
    unit = unit.lower().strip()
    if unit not in vocab:
        print("\nUnit does not exist.")
        return

    word_list = vocab[unit]

    if start_word and end_word:
        try:
            start_index = next(i for i, w in enumerate(word_list) if w['word'] == start_word)
            end_index = next(i for i, w in enumerate(word_list) if w['word'] == end_word)
            word_list = word_list[start_index:end_index + 1]
        except StopIteration:
            print("\nStart or end word not found.")
            return

    for _ in range(7):
        for word in word_list:
            print(f"\nWord: {word['word']}")
            time.sleep(3)
            print(f"Meaning: {word['meaning']}")
