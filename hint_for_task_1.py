if __name__ == "__main__":
    print("cur_1.execute('ROLLBACK;')")

    response = input("Do you need to know the line number? (Y/N): ")

    if response.upper() == 'Y':
        print("Implementation at line 49")
    else:
        print("Run this script again if you change your mind")