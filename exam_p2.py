import csv

yobs = {}

def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    f = open("babynames/" + file_name, 'r')
    reader = csv.reader(f)
    return list(reader)


def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    yob = yobs[str(year)]
    total = 0
    for record in yob:
        total += int(record[2])
    return total    


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    yob = yobs[str(year)]
    
    total = 0
    for record in yob:
        if record[1] == gender:
            total += int(record[2])
    
    for record in yob:
        if record[0] == name and record[1] == gender:
            return int(record[2]) / total * 100


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    highest_value = 0
    h_year = 0
    for year in range(1880, 2011):
        p = proportion(name, gender, year)
        if p > highest_value:
            highest_value = p
            h_year = year
    
    return h_year


def main():
    for year in range(1880, 2011):
        yobs[str(year)] = process_file("yob" + str(year) + ".txt")
    
    print("In 1981, %.4f%% of baby girls were named 'Shirley'" % proportion('Shirley', 'F', 1981))
    print("In 1982, %.4f%% of baby girls were named 'Shirley'" % proportion('Shirley', 'F', 1982))
    print("In 1959, %.4f%% of baby girls were named 'Shirley'" % proportion('Shirley', 'F', 1959))
    print("The highest year of Shirley's birth is " + str(highest_year('Shirley', 'F')))

if __name__ == '__main__':
    main()
