from anagram_checker import AnagramChecker

anagram_checker = AnagramChecker("sowpods.txt")

def get_user_menu_choice():
    while True:
        print("Type a word you  with to find an anagram for or type 'x' to exit.")
        user_word = input(": ").strip().upper()
        if (len(user_word.split()) != 1):
            print("You should write only a 'single' word!")
            continue
        else:
            break
    return user_word

def check_for_anagrams(word):
    if (anagram_checker.is_valid_word(word)):
        print(f"{word} is a valid English word.")
        list_result = anagram_checker.get_anagrams(word)
        result = " ".join(list_result)
        print(f"Anagrams for your word: {result}")
    else:
        print(f"{word} is not a valid English word.")

def main():
    while True:
        word = get_user_menu_choice()
        print(f"Your word: {word}")
        if word == 'x'.upper():
            print('thanks for playing')
            return
        check_for_anagrams(word)

main()