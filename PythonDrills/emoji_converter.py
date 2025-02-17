# Simple drill that converts emojis into real ones using function

emojis = {
    ":)" : "😊",
    ":(" : "😢"
}

def emoji_converter(message):
    words = message.split(" ")
    output = ""
    for word in words:
        output = output + " " + emojis.get(word,word)

    return output


input = input("> ")
output = emoji_converter(input)
print(output)