def main():
    type(input("File name: ").lower())

def type(prompt):
    if ".gif" in prompt:
        print("image/gif")

    elif ".jpg" in prompt:
        print("image/jpeg")

    elif ".jpeg" in prompt:
        print("image/jpeg")

    elif ".pdf" in prompt:
        print("application/pdf")

    elif ".png" in prompt:
        print("image/png")

    elif ".txt" in prompt:
        print("text/plain")

    elif ".zip" in prompt:
        print("application/zip")

    else:
        print("application/octet-stream")

main()
