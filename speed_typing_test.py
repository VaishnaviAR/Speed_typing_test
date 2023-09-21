import random
import time

def generate_words(word_count):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.sample(words, word_count)

def main():
    word_count = 10
    words_to_type = generate_words(word_count)
    typed_words = []

    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    start_time = time.time()

    for word in words_to_type:
        print(f"Type the word: {word}")
        user_input = input()
        typed_words.append(user_input)

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_count = sum(1 for typed, original in zip(typed_words, words_to_type) if typed == original)
    accuracy = (correct_count / word_count) * 100
    words_per_minute = (word_count / elapsed_time) * 60

    print("\nTest results:")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
