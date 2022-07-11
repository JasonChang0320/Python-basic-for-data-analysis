import re

#example 1

txt = "The rain in Spain"
x = re.match(r"^The.*Spain", txt)
#Check if the string starts with "The" and ends with "Spain":

if (x):
    print("YES! We have a match!")
else:
    print("No match")

txt = "ABC123 The rain in Spain"
x = re.match(r"^The.*Spain$", txt)

if (x):
    print("YES! We have a match!")
else:
    print("No match")

#example 2
txt = "The rain in Spain 123 The sun in "
x = re.search(r"^The.*Spain$", txt)

if (x):
    print("YES! We have a match!")
else:
    print("No match")

#differences between match & search
print(re.match(r'super', 'superstition'))
print(re.match(r'super', 'insuperable'))

print(re.search(r'super', 'superstition'))
print(re.search(r'super', 'insuperable'))

#.span .string .group
txt = "The rain in Spain"
x = re.search(r"S\w+", txt)
print(x.string)
print(x.span())
print(x.group())

#find all
pattern=r'abc'
string='123321 abc abc abc'
match = re.findall(pattern,string)
print(match)

#address
pattern = r"\..{2}"
string = 'www.yahoo.com.tw , www.ntu.edu.tw , www.test.gov.tw'
match = re.findall(pattern, string)
print(match)

#email
pattern = r"([A-Za-z0-9._]+@[A-Za-z.]+)"
string = 'isaac60103@gmail.com, isaac60103@hotmail.com, kevin@yahoo.com'
match = re.findall(pattern, string)
print(match)

#How modify the following example to include cat?
#Origin code
animals="1.cat, 2 dog, 03 pig, 4 duck"
regex=r"\d+\s\w+"
obj=re.findall(regex,animals)
print(obj)

#answer:
regex=r"\d+\.?\s?\w+"
new_obj=re.findall(regex,animals)
print(new_obj)

#pandas read ascii data
import pandas as pd

file_name="201801071953_CHKH_13071953.P18.asc"
waveform=pd.read_csv(file_name,sep=r"\s+",header=None)
waveform
