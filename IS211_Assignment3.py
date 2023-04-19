import pandas as pd
import re

def image_format_func(text):
    image_format = ['.jpg', '.png', '.gif']
    for i in image_format:
        if bool(re.search(i , text)) == True:
            return True
    return False

def browser_func(text):
    if bool(re.search('Firefox' , text)) == True:
        return 'Mozilla Firefox'
    elif bool(re.search('Chrome' , text)) == True:
        return 'Google Chrome'
    elif bool(re.search('Explorer' , text)) == True:
        return 'Internet Explorer'
    elif bool(re.search('Safari' , text)) == True:
        return 'Safari'
    
def hour_func(text):
    return list(text.split())[-1][:2]

#PART II
df = pd.read_csv('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')


#PART III
#Now we find out which cell in path_to_file column has image format and store that value in another column named 'image_bool'

df['image_bool'] = df['path_to_file'].apply(lambda x: image_format_func(x), axis = 1)

percentage = (len(df[df['image_bool']==True])/len(df['image_bool']))*100
print('Image requests account for {} of all requests'.format(percentage))

#PART IV
#Now we find out which record has which browser stored

df['browser'] = df['browser'].apply(lambda x: browser_func(x), axis = 1)

#Now we have all the records with their browser name in the 'browser' column

print('Browsers with maximum occurences: ', df['browser'].mode().to_list())

#PART VI
#extra credits question:

df['hour'] = df['datetime_accessed'].apply(lambda x: hour_func(x), axis = 1)

#Now I'm making a dictionary to store numbers of hits for each hour
hour_dict = df['hour'].value_counts().to_dict()

#Now I'm printing the key-value pairs of the dictionary in the given format

for hour, hits in hour_dict.items():
    print('Hour {} has {} hits'.format(hour, hits))
