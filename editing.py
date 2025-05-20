# vocabulary_trainer.py
import json
import time
import os

data_file = 'vocab_hebrew.json'

def load_vocab():
    if not os.path.exists(data_file):
        return {}
    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_vocab(vocab):
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)

# === Editing Mode ===
def add_word(unit, word, meaning):
    vocab = load_vocab()
    unit = unit.lower().strip()
    word = word.lower().strip()
    meaning = meaning.strip()

    if unit not in vocab:
        vocab[unit] = []

    for entry in vocab[unit]:
        if entry['word'] == word:
            print(f"\nThe word '{word}' already exists in unit '{unit}'!")
            return

    vocab[unit].append({"word": word, "meaning": meaning})
    save_vocab(vocab)
    print(f"\nThe word '{word}' was added to unit '{unit}' successfully!")

def delete_word(unit, word):
    vocab = load_vocab()
    unit = unit.lower().strip()
    word = word.lower().strip()

    if unit not in vocab:
        print("\nUnit does not exist.")
        return

    original_len = len(vocab[unit])
    vocab[unit] = [entry for entry in vocab[unit] if entry['word'] != word]

    if len(vocab[unit]) < original_len:
        save_vocab(vocab)
        print(f"\nThe word '{word}' was deleted from unit '{unit}'!")
    else:
        print("\nWord not found.")

def update_word(unit, old_word, new_word, new_meaning):
    vocab = load_vocab()
    unit = unit.lower().strip()
    old_word = old_word.lower().strip()
    new_word = new_word.lower().strip()
    new_meaning = new_meaning.strip()

    if unit not in vocab:
        print("\nUnit does not exist.")
        return

    for entry in vocab[unit]:
        if entry['word'] == old_word:
            entry['word'] = new_word
            entry['meaning'] = new_meaning
            save_vocab(vocab)
            print(f"\nWord '{old_word}' was updated to '{new_word}'!")
            return

    print("\nWord not found.")

def list_words(unit):
    vocab = load_vocab()
    unit = unit.lower().strip()

    if unit not in vocab or not vocab[unit]:
        print("\nNo words found in this unit.")
        return

    print(f"\nWords in unit '{unit}':")
    for entry in vocab[unit]:
        print(f"- {entry['word']} : {entry['meaning']}")
