#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    val = dir(hidden_4)

    for i in val:
        if i[:2] != "__":
            print(i)
