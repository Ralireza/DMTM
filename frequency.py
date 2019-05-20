import collections as col


def relative_frequency(number_list, number, is_in_percent):
    count_dict = col.Counter(number_list);
    N = sum(count_dict.values())
    relative_freq = count_dict.get(number) / N
    relative_freq = relative_freq * 100 if is_in_percent else relative_freq
    return relative_freq


def absolute_frequency(number_list, number):
    count_dict = col.Counter(number_list)
    f = count_dict.get(number)
    return f


# my_list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10]
my_list = [1,1,2,2,3,3]
print(absolute_frequency(my_list, 2))


