def count_letter(letter, word_list):
    count=0
    for word in word_list:
        if letter in word:
            count += 1
    return count

word_list = ["hola", "Como", "Estas", "en", "este", "dia"]

letter = input("Ingresa la letra a buscar: ")
letter_count = count_letter(letter, word_list)
print(letter_count)