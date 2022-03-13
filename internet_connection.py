import requests
import os


def main():
    file = 'animals_starting_with_c.txt'
    download_all(file)


def one_url(animal_name):
    """this obtains the url for the inputted animal's picture"""
    url = 'https://a-z-animals.com/animals/' + animal_name.replace(' ', '-')

    try:
        # print(url)
        r = requests.get(url)
        data = r.text
        search_for = 'meta property="og:image" content="https://'
        lchar = data.find(search_for)
        slice_object = slice(lchar + 34, lchar + 250)
        new_string = r.text[slice_object]
        rchar = new_string.find(".jpg")
        url3 = new_string[:rchar + 4]

        count = url3.count("https://")
        if count > 1:
            url3 = url3[7:]

        r = requests.get(url3)

        file_name = os.getcwd() + '\\image\\' + animal_name.replace(' ', '-') + '.jpg'

        open(file_name, 'wb').write(r.content)

    except requests.RequestException:
        if url3 == "":
            print("Blank")
        print(url3)
        pass


def download_all(file):
    """downloads images of all animals in a given file"""

    # open the file with the animal names
    with open(file, "r") as f:
        contents = f.readlines()

    # loop through all the names and query the internet for each one
    for line in contents[:]:
        line = line.rstrip()
        one_url(line)


# program starts here
if __name__ == "__main__":
    main()
