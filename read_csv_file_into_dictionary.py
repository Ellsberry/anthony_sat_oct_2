"""This program reads a csv file and puts the data in a dictionary"""



import csv


def main():
    dictionary, dictionary_working = read_csv_file_into_dictionary("HTML Tags and Descriiptions.csv")
    if not dictionary_working:
        exit()
    for key, value in dictionary.items():
        print("{:<15} {:}".format(key, value))



def read_csv_file_into_dictionary(file):
    dictionary = {}
    try:
        with open(file, newline="") as dict_file:
            reader = csv.reader(dict_file)
            dictionary = dict(reader)
            dictionary_working = True
    except FileNotFoundError:
        print("Could not find file:", file)
        dictionary_working = False
    return dictionary, dictionary_working


if __name__ == "__main__":
    main()
