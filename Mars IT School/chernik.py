with open("alice.txt", encoding='utf-8') as alice_text:
    alice_read = alice_text.read()
    line = alice_text.readline()
    print(alice_read.count(readline()))