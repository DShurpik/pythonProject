def reverse(st):
    words = [word for word in st.split() if word]
    reversed_words = ' '.join(reversed(words))
    return reversed_words

print(reverse('Hello world'))