import string
#step1
paragraph = input("enter a paragraph to analyze:\n")

#step2
translator = str.maketrans('', '', string.punctuation)
clean_paragraph = paragraph.translate(translator).lower()

#step3
words = clean_paragraph.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#step4
if word_counts:
    most_freq = max(word_counts, key=word_counts.get)
    count = word_counts[most_freq]

#step5
    unique_word = len(word_counts)

    print(f"most frequent: '{most_freq}' (appears {count} times)")
    print(f"total unique words: {unique_word}")
    print(f"total word count: {len(words)}")
else:
    print("no words found.")

save = input("\nwould you like to save these counts to 'word_report.txt'? (y/n): ").lower()
if save == 'y':
    with open("word_report.txt", "w") as file:
        file.write("word frequencies:\n")
        for word, freq in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
            file.write(f"{word}: {freq}\n")
        print("report saved successfully.")