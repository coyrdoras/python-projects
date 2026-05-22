questions = {
    "Azərbaycanin paytaxti?": "Baki",
    "Pythonu kim yaratdi?": "Guido van Rossum",
    "2 ** 8 = ?": "256",
    "Dünyanin ən böyük okeani?": "Sakit okean",
    "HTML nəyin abbreviaturasidir?": "HyperText Markup Language",
    "Ən sürətli heyvan?": "Gepard",
    "Python neçənci ildə yaradildi?": "1991",
    "Dünyanin ən böyük ölkəsi?": "Rusiya"
}

score = 0

for question, answer in questions.items():
    for i in range(1, len(questions.keys()) + 1):
        a = i
        user_answer = input(f"Sual {a}. " + question + " ")
        i += 1
        if user_answer == answer:
            print("Düzgündür! ✅\n")
            score += 1
            break
        else:
            print(f"Yanlişdir! ❌\nDüzgün cavab: {answer}\n")
            break

print(f"\nNəticə: {score}/{len(questions)}")

if score == 8:
    print("\n Canavarsan!🔥🔥🔥\n")
elif 8 > score > 4:
    print("\nNetice eladir!\n")
elif score == 4:
    print("\nNetice ortadir!\n")
elif 1 < score < 4:
    print("\nNetice pisdir!\n")
else:
    print("\nTupoysan!\n")