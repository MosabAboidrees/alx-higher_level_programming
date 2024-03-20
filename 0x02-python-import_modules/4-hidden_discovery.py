#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)  # Retrieve a list of names defined in hidden_4
    for name in names:
        if not name.startswith("__"):  # Filter out names starting with "__"
            print(name)
