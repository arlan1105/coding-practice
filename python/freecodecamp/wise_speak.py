def wise_speak(sentence):
    aux = ["have", "must", "are", "will", "can"]
    punctuation = sentence[-1]
    sentence = sentence.split()

    for word in sentence[:]:
        if word not in aux:
            sentence.append(sentence.pop(0))
        else:
            sentence.append(sentence.pop(0))
            break
            
    sentence = ' '.join(sentence).lower().capitalize().replace(punctuation, ',') + punctuation
    
    return sentence

print(wise_speak("You must speak wisely."))


# def wise_speak(sentence):
#     aux = ["have", "must", "are", "will", "can"]
#     punctuation = sentence[-1]
#     words = sentence[:-1].split()

#     i = next(i for i, w in enumerate(words) if w in aux)

#     front = ' '.join(words[:i + 1]).lower()
#     back = ' '.join(words[i + 1:])
#     back = back[0].upper() + back[1:]

#     return f"{back}, {front}{punctuation}"