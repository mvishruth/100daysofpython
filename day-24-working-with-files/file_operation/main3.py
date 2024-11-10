# windows absolute path
with open("/users/muthyalv/desktop/my_file2.txt") as file:
    contents = file.read()
    print(contents)

# windows absolute path
# C:\Users\muthyalv\OneDrive - Hewlett Packard Enterprise\Projects\Training\100daysofpython\day-24-working-with-files\file_operation
with open("../../../../../../desktop/my_file2.txt") as file:
    contents = file.read()
    print(contents)

