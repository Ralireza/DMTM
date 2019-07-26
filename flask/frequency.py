import collections as col


def relative_frequency(number_list, number, is_in_percent):
    count_dict = col.Counter(number_list);
    N = sum(count_dict.values())
    if number in count_dict:
        relative_freq = count_dict.get(number) / N
        relative_freq = relative_freq * 100 if is_in_percent else relative_freq
    else:
        relative_freq=0
    return relative_freq


def absolute_frequency(number_list, number):
    count_dict = col.Counter(number_list)
    f = count_dict.get(number)
    if f is None:
        f=0
    return f

