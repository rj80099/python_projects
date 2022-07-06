
#open weather_data.csv file and read all the strings of the file
#but using open method data will have commas and it will be very difficult to seperate that data
# with open("weather_data.csv") as weather_data:
#     txt_content=weather_data.readlines()
#     print(txt_content)


#another way to get the string data removing those commas is by
# using CSV LIB

# import csv
#
# with open("weather_data.csv")as data_file:
#     data=csv.reader(data_file) #this will return an object now we can loop through to print those data
#     temperature=[]
#     for row in data:
#         if(row[1]!='temp'):
#             temperature.append(int(row[1]))
#     print(temperature)

#from the above line of we can draw an observation that for
#such small number of data we have written this many lines of
#for large data data extration become more complex
#solution to for this is to use pandas library
#which make data reading more easy and fast compare to any other lib

#lets using the our weather_data.csv file
import pandas

#data =pandas.read_csv("weather_data.csv")
#print(type(data))    #returns <class 'pandas.core.frame.DataFrame'> 2D data
#print(type(data["temp"])) #returns <class 'pandas.core.series.Series'> 1D data
#print(data["temp"])

#print(data.to_dict())      #convert all tha data into dictionary
#temp_list=data["temp"].to_list()   #convert entire row as dict

#calculate avg temperature
# avg=sum(temp_list)/len(temp_list)
# print(avg)

#same thing can done using pandas mean method
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# #get the data from the columns
# print(data.condition)

#get data from in row

#print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])
#
# monday=data[data.day == "Monday"]
# monday_temp=int(monday.temp)
# monday_temp_F=monday_temp*9/5 +32
# print(monday_temp_F)

#create dataframe from scratch
# data_dict={
#     "student":["Rohit","Sejal","Prakesh","Anil"],
#     "score":[76,56,65,45]
# }
#
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data")
# print(data)

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color=data[data["Primary Fur Color"]=="Gray"]
gray_squreal=len(gray_color["Primary Fur Color"])

red_color=data[data["Primary Fur Color"]=="Cinnamon"]
red_squreal=len(red_color["Primary Fur Color"])

black_color=data[data["Primary Fur Color"]=="Black"]
black_squreal=len(black_color["Primary Fur Color"])

data_dict={
    "Fur Color":["Gray","Red","Black"],
    "Count":[gray_squreal,red_squreal,black_squreal]
}

df=pandas.DataFrame(data_dict)
df.to_csv("Squeral Color Count Data")