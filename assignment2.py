
num_messages = int(input("Enter number of messages: "))


chat = {}

all_messages = []

for i in range(num_messages):
    entry = input("Enter message (Name:Message): ")
    name, message = entry.split(":", 1)
    name = name.strip()
    message = message.strip()

    if name in chat:
        chat[name].append((i, message))
    else:
        chat[name] = [(i, message)]

    all_messages.append((name, message))


def count_words(msg):
    return len(msg.split())


while True:
    print("\nMenu:")
    print("1. Total number of messages")
    print("2. Unique users in the chat")
    print("3. Total words in the chat")
    print("4. Average words per message")
    print("5. Longest message")
    print("6. Most active user")
    print("7. Message count by specific user")
    print("8. Most frequent word by a specific user")
    print("9. First and last message by a user")
    print("10. Check if user is in the chat")
    print("11. Commonly repeated words")
    print("12. User with longest average message")
    print("13. Messages mentioning a user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Show all questions asked")
    print("17. Reply ratio between two users")
    print("18. Check for deleted messages")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Total messages:", len(all_messages))

    elif choice == 2:
        print("Unique users:", list(chat.keys()))

    elif choice == 3:
        total_words = 0
        for name, message in all_messages:
            total_words += count_words(message)
        print("Total words in chat:", total_words)

    elif choice == 4:
        total_words = sum(count_words(msg) for _, msg in all_messages)
        avg = total_words / len(all_messages)
        print("Average words per message: {:.2f}".format(avg))

    elif choice == 5:
        longest = max(all_messages, key=lambda x: len(x[1]))
        print("Longest message:", longest[0] + ": " + longest[1])

    elif choice == 6:
        most_active = max(chat.items(), key=lambda x: len(x[1]))
        print("Most active user:", most_active[0], "(", len(most_active[1]), "messages)")

    elif choice == 7:
        user = input("Enter username: ")
        if user in chat:
            print("Messages sent by", user, ":", len(chat[user]))
        else:
            print("User not found.")

    elif choice == 8:
        user = input("Enter username: ")
        if user in chat:
            words = []
            for _, msg in chat[user]:
                words.extend(msg.lower().split())
            from collections import Counter
            word_freq = Counter(words)
            if word_freq:
                most_common = word_freq.most_common(1)[0]
                print("Most frequent word by", user, ":", most_common[0])
            else:
                print("No words found.")
        else:
            print("User not found.")

    elif choice == 9:
        user = input("Enter username: ")
        if user in chat and chat[user]:
            print("First message:", user + ": " + chat[user][0][1])
            print("Last message:", user + ": " + chat[user][-1][1])
        else:
            print("User not found.")

    elif choice == 10:
        user = input("Enter username: ")
        if user in chat:
            print("User", user, "is present in chat.")
        else:
            print("User", user, "not found.")

    elif choice == 11:
        from collections import Counter
        all_words = []
        for _, msg in all_messages:
            all_words.extend(msg.lower().split())
        word_count = Counter(all_words)
        repeated = [word for word, count in word_count.items() if count > 1]
        print("Common repeated words:", set(repeated))

    elif choice == 12:
        user_averages = {}
        for user in chat:
            total_words = sum(count_words(msg) for _, msg in chat[user])
            average = total_words / len(chat[user])
            user_averages[user] = average
        best_user = max(user_averages.items(), key=lambda x: x[1])
        print("User with longest average message:", best_user[0], "(avg {:.2f} words)".format(best_user[1]))

    elif choice == 13:
        mention_name = input("Enter name to check mentions: ").lower()
        mention_count = sum(1 for _, msg in all_messages if mention_name in msg.lower())
        print("Messages mentioning", mention_name, ":", mention_count)

    elif choice == 14:
        seen = set()
        unique = []
        for pair in all_messages:
            if pair not in seen:
                unique.append(pair)
                seen.add(pair)
        print("Unique messages count:", len(unique))
        for u in unique:
            print(u[0] + ": " + u[1])

    elif choice == 15:
        sorted_msgs = sorted([name + ": " + msg for name, msg in all_messages])
        print("Messages sorted A-Z:")
        for m in sorted_msgs:
            print(m)

    elif choice == 16:
        questions = []
        for name, msg in all_messages:
            if "?" in msg:
                questions.append(name + ": " + msg)
        print("Questions asked in chat:")
        for q in questions:
            print(q)

    elif choice == 17:
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        user1_msgs = [i for i, (name, _) in enumerate(all_messages) if name == user1]
        user2_msgs = [i for i, (name, _) in enumerate(all_messages) if name == user2]
        replies = sum(1 for i in user2_msgs if any(j < i for j in user1_msgs))
        print("Reply ratio from", user2, "to", user1, ":", replies, "replies")

    elif choice == 18:
        deleted = [name + ": " + msg for name, msg in all_messages if msg.lower() == "this message was deleted"]
        print("Deleted messages found:", len(deleted))
        for d in deleted:
            print(d)

    elif choice == 0:
        print("Goodbye!")
        break

    else:
        print("Invalid input.")
