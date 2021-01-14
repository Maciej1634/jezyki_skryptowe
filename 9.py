try:
    with open("file.txt", "r") as f:
        with open("file2.txt", "w") as f2:
            for a in f.readlines():
                f2.write(a)
except Exception:
    print("wystapil wyjatek")
finally:
    print("przepisano pliki")
