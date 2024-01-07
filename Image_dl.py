from urllib import request
import time
import random
import links


url_file = 'urls.txt'
path = "Images/"
urls = []

try: 
    with open(url_file, 'r') as file_descripter :

        print("\nAccess Gained! to URL file\n")
        time.sleep(2)
        
        counter = 0 
        while True :
            url = file_descripter.readline()
            urls.append(url)
            counter += 1
            print(counter, "URL Listed\n")

            if not url :
                break

except:
    print("URL file not found!\n")

name_gen = 'abcdefghijklmnopqrstuvwxyz'

def image_data_request(urls, path) :

    for index , url in enumerate(urls) :
        file_name = str(index) + str(random.choices(name_gen, k = 10))
        full_file_name = path + file_name + ".jpg"
        try:
            request.urlretrieve(url, full_file_name)
            print(f"Image {index} has been downloaded sucsessfully !\n")

        except:
            print(f"Image {index} has been not downloaded !\n")
    

image_data_request(urls, path)

