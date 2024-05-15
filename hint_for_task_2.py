if __name__ == "__main__":
    print("Commit needs to be added to the first sql statement")

    response = input("Do you need to know the new sql statement? (Y/N): ")

    if response.upper() == 'Y':
        print('''
            BEGIN;
            UPDATE my_table
            SET v='a' WHERE id=1;
            COMMIT;
        ''')
    else:
        print("Run this script again if you change your mind")