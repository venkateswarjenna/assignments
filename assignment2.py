n=int(input("Enter the no of message: "))
chat={}
for i in range(n):
    name,message=input().split(':')
    if name in chat:
        chat[name].append((i,message))
        
    else:
        chat[name]=[(i,message)]
print(chat)


while True:
    print("1.Count total number of message")
    print("2.Identify unique users in the chat")
    print("3.Count total words in the chat")
    print("0.Exit")

    ch=int(input("enter your choice: "))
    if ch==1:
        print(f"Count total number of message{len(chat)}")
    elif ch==2:
        print(f"Identify unique users in the chat{chat.keus()}")
    elif ch==3:
        print(f"Count total words in the chat: ")
    
    elif ch==0:
        break
    else:
        print("Invalid input")
