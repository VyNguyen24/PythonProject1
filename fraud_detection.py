# Name: Vy Nguyen


import csv
import matplotlib.pyplot as plt
import random


###
#  Problem 1
###


def extract_election_votes(filename, column_names):
    f = open(filename)
    file = csv.DictReader(f)
    int_lst = []
    for row in file:
        for key, value in row.items():
            for j in column_names:
                if j == key:
                    str_num = value.replace(",", "")
                    if str_num != "":
                        int_num = int(str_num)
                        int_lst.append(int_num)
    return int_lst


def file_dict(filename, column_names):
    dict = {}
    numbers = extract_election_votes(filename, column_names)
    histogram = ones_and_tens_digit_histogram(numbers)
    mse = calculate_mse_with_uniform(histogram)
    datapoints = len(numbers)
    dict["mse"] = mse
    dict["datapoints"] = datapoints
    dict["histogram"] = histogram
    return dict

###
# Problem 2
###


def ones_and_tens_digit_histogram(numbers):
    num_lst = []
    for x in numbers:
        i = x % 100
        num_lst.append(int(i // 10))
        num_lst.append(int(i % 10))
    list = [0 for j in range(10)]
    for num in num_lst:
        list[num] += 1
    final_lst = []
    for j in list:
        j = j/len(num_lst)
        final_lst.append(j)
    return final_lst


###
# Problem 3
###

def plot_iran_least_digits_histogram(histogram):
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y1 = histogram
    y2 = [0.1 for i in range(10)]
    plt.plot(x, y2, label="ideal")
    plt.plot(x, y1, label="iran")
    plt.ylabel('Frequency')
    plt.xlabel('Digit')
    plt.title('Distribution of the last two digits in Iranian dataset')
    plt.legend(loc='upper left')
    plt.savefig("iran-digits.png")
    # plt.show()
    plt.clf()


###
# Problem 4
###

def plot_dist_by_sample_size():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_ideal = [0.1 for i in range(10)]
    y_10 = [random.randint(0, 99) for i in range(10)]
    y_50 = [random.randint(0, 99) for i in range(50)]
    y_100 = [random.randint(0, 99) for i in range(100)]
    y_1000 = [random.randint(0, 99) for i in range(1000)]
    y_10000 = [random.randint(0, 99) for i in range(10000)]
    plt.plot(x, ones_and_tens_digit_histogram(y_10), label="10 random numbers")
    plt.plot(x, ones_and_tens_digit_histogram(y_50), label="50 random numbers")
    plt.plot(x, ones_and_tens_digit_histogram(y_100),
             label="100 random numbers")
    plt.plot(x, ones_and_tens_digit_histogram(y_1000),
             label="1000 label numbers")
    plt.plot(x, ones_and_tens_digit_histogram(y_10000),
             label="10000 label numbers")
    plt.plot(x, y_ideal, label="ideal")
    plt.ylabel('Frequency')
    plt.xlabel('Digit')
    plt.title('Distribution of the last two digits in Iranian dataset')
    plt.legend(loc='upper left')
    plt.savefig("random-digits.png")
    # plt.show()
    plt.clf()


###
# Problem 5
###

def mean_squared_error(numbers1, numbers2):
    sum = 0
    for i in range(len(numbers1)):
        y = (numbers1[i]-numbers2[i])**2
        sum += y
    mean = sum / len(numbers1)
    return mean


###
# Problem 6
###

def calculate_mse_with_uniform(histogram):
    list = [0.1 for i in range(len(histogram))]
    result = mean_squared_error(histogram, list)
    return result


def cal_dict(mse, data_points):
    dict = {}
    groups = [[random.randint(0, 99) for i in range(data_points)]
              for j in range(10000)]
    group_mse_lst = []
    for each in groups:
        each_mse = calculate_mse_with_uniform(
            ones_and_tens_digit_histogram(each))
        group_mse_lst.append(each_mse)
    large_count = 0
    small_count = 0
    for value in group_mse_lst:
        if value >= mse:
            large_count += 1
        else:
            small_count += 1
    p = large_count / 10000
    dict["large_count"] = large_count
    dict["small_count"] = small_count
    dict["p"] = p
    return dict


def compare_iran_mse_to_samples(iran_mse, number_of_iran_datapoints):
    dict = cal_dict(iran_mse, number_of_iran_datapoints)
    print("2009 Iranian election MSE:", iran_mse)
    print("Quantity of MSEs larger than or equal"
          + " to the 2009 Iranian election MSE:", dict["large_count"])
    print("Quantity of MSEs smaller than"
          + " the 2009 Iranian election MSE:", dict["small_count"])
    print("2009 Iranian election null hypothesis"
          + " rejection level p:", dict["p"])


def compare_us_mse_to_samples(us_mse, number_of_us_datapoints):
    dict = cal_dict(us_mse, number_of_us_datapoints)
    print("2008 United States election MSE:", us_mse)
    print("Quantity of MSEs larger than or equal"
          + " to the 2008 United States election MSE:", dict["large_count"])
    print("Quantity of MSEs smaller than"
          + " the 2008 United States election MSE:", dict["small_count"])
    print("2008 United States election null hypothesis"
          + " rejection level p:", dict["p"])


# The code in this function is executed when this
# file is run as a Python program


def main():
    # Code that calls functions you have written above
    # e.g. extract_election_vote_counts() etc.
    # This code should produce the output expected from your program.
    iran_dict = file_dict("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "\
        Karrubi", "Mousavi"])
    plot_iran_least_digits_histogram(iran_dict["histogram"])
    plot_dist_by_sample_size()
    compare_iran_mse_to_samples(iran_dict["mse"], iran_dict["datapoints"])
    print()
    us_dict = file_dict("election-us-2008.csv", ["Obama", "McCain", "Nader", "\
        Barr", "Baldwin", "McKinney"])
    compare_us_mse_to_samples(us_dict["mse"], us_dict["datapoints"])


if __name__ == "__main__":
    main()
