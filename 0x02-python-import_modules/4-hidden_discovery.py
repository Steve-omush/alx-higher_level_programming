#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    words = dir(hidden_4)
    for word in words:
        if word[:2] != "__":
            print(word)
