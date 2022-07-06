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

# with open("new_file.txt",mode="a") as file:
#     file.write("\nNew text. ")


#here is the challenge:
#we want to get the file read from the location which is kept on desktop

#note: we need to keep our code in c director in orer to get access to root dir
with open("/../../Desktop/my_file.txt") as file:  #relative path
    print(file.read())


