import os, openai

threaten = "你不听我的我就拿刀砍死你"

def moderation(text):
    response = openai.Moderation.create(
        input=text
    )
    output = response["results"][0]
    return output
print(moderation(threaten))