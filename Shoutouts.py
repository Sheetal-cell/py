import pyttsx3

a = int(input("how many names u wanna shoutout: "))
list =[ ]
for i in range(a):
    name = input("Enter name- ")
    list.append(name)
    
print("\n")
b = pyttsx3.init()


for i in list:
    print(f"Shoutout to {i}")
    b.say(f"Shoutout to {i}")
    b.runAndWait()