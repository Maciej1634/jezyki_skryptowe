with open("test.txt", "w") as f:
    f.write("jd")
    with open("test.txt", "r") as f2:
        print(f2.read())
