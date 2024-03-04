letters = ['a','b','c','d','e','f','g'
           ,'h','i','j','k','l','m','n','o','p'
           ,'q','r','s','t','u','v','w',
           'x','y','z']

userMessage = str(input('Write your message: '))
key = int(input('Write your prefered key: '))

#We have to change every character of the message to its index
messageIndex = [] #List of all message's indexes
for char in userMessage:
    messageIndex.append(
        letters.index(char) + 1
        #I have added number 1 because the first index is zero 
    )

print(messageIndex)

newIndex = [] #for new indexes
for p in messageIndex:
    c = (p + key) % 26 #The formula of Cesear
    newIndex.append(c)

print(newIndex)

encrypted_message = []
for index in newIndex:
    encrypted_message.append(
        letters[index-1]
    )


final_message = "".join(encrypted_message)
print(final_message)
