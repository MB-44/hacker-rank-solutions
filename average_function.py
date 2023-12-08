def avg(values):
    args = [int(value) for value in values]
    output = f"{(sum(args) / len(args)):.2f}"
    return output

if __name__ == "__main__":
    arg = input("Enter here: ").split()
    result = avg(arg)
    print(result)

