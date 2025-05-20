# === Testing Mode ===
def test_unit(unit):
    vocab = load_vocab()
    unit = unit.lower().strip()
    if unit not in vocab:
        print("\nUnit does not exist.")
        return

    words = vocab[unit]
    correct = 0
    total = len(words)
    incorrect_list = []

    for entry in words:
        answer = input(f"\nWhat is the meaning of: {entry['word']}? ").strip().lower()
        if answer == entry['meaning'].strip().lower():
            correct += 1
        else:
            incorrect_list.append((entry['word'], entry['meaning']))

    print(f"\nTest complete: {correct}/{total} correct answers ({(correct/total)*100:.1f}%)")
    if incorrect_list:
        print("\nIncorrect answers:")
        for word, meaning in incorrect_list:
            print(f"- {word} : {meaning}")