"""This program reads a web page and count the HTML elements on the page."""
# Anthony has not yet read an HTML file.
import requests
import read_csv_file_into_dictionary as r_csv


def main():
    get_page = r"https://a-z-animals.com/animals/"
    html_code = read_html_page(get_page)
    dictionary, dictionary_working = r_csv.read_csv_file_into_dictionary("HTML Tags and Descriiptions.csv")
    if not dictionary_working:
        print("Bad csv elements file.")
        quit()
    for key, value in dictionary.items():
        count = html_code.count(key[:-1])
        if count != 0:
            print("{:<15}, {:<10}, {:}".format(key, count, value))


def read_html_page(page_url):
    try:
        temp_object = requests.get(page_url)
        data = temp_object.text
        # print(data)
    except Exception as e:
        print("There is something wrong  ", str(e))
        quit()
    return data


if __name__ == "__main__":
    main()
