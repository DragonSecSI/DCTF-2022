import re

def appendix_solution(image):
    regex = re.compile("DCTF{.*}")
    text = ""

    with open(image, "rb") as f:
        for line in f:
            text += get_ascii(line)

    matches = regex.findall(text)

    if matches is None:
        raise Exception("Flag not found!")

    return matches[0]

def get_ascii(binary):
    text = ""
    for c in binary:
        if c < 128:
            text += chr(c)
    return text

if __name__ == '__main__':
    print(appendix_solution("chall/appendix.jpg"))
