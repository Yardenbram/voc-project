# === Main Menu ===
def main():
    while True:
        print("""
Vocabulary Trainer
1. Editing Mode
2. Training Mode
3. Testing Mode
4. Exit
        """)
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            unit = input("Unit: ")
            print("1. Add | 2. Delete | 3. Update | 4. List")
            action = input("Choose action: ")
            if action == '1':
                word = input("Word (English): ")
                meaning = input("Meaning (Translation): ")
                add_word(unit, word, meaning)
            elif action == '2':
                word = input("Word to delete: ")
                delete_word(unit, word)
            elif action == '3':
                old = input("Current word: ")
                new = input("New word: ")
                new_meaning = input("New meaning: ")
                update_word(unit, old, new, new_meaning)
            elif action == '4':
                list_words(unit)

        elif choice == '2':
            unit = input("Unit to practice: ")
            full = input("Practice full unit? (y/n): ")
            if full.lower() == 'y':
                train_unit(unit)
            else:
                start = input("Start word: ")
                end = input("End word: ")
                train_unit(unit, start, end)

        elif choice == '3':
            unit = input("Unit to test: ")
            test_unit(unit)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
