def recursive(n):
    if n == 1:
        print(n, "finished")
        return False
    else:
        print(n, "else")
        recursive(n - 1)
        return True

print(recursive(1))