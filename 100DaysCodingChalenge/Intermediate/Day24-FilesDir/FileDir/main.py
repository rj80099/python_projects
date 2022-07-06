#Read the content of the file
# with open("my_file.txt") as file:       #we don't have to remember to close the tab
#     contents=file.read()
#     print(contents)

#Write content to the file
# "w"-delete and replaced the text present in the file
# "a"-append new text to the file
# with open("my_file.txt",mode="a") as file:
#     file.write("\nNew text. ")


#if no file exist with the named in file paramenter
# python we go ahead and make a new empty file with the name specified

with open("new_file.txt",mode="a") as file:
    file.write("\nNew text. ")