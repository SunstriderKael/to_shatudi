import random


def init_list(list_len):
    output = list()
    for idx in range(list_len):
        item = random.randint(0, 100)
        output.append(item)
    return output


def bubble_sort(input_list):
    # 请百度冒泡排序，并添加快速排序方法
    for idx in range(len(input_list)):
        for idy in range(len(input_list) - idx - 1):
            item1 = input_list[idy]
            item2 = input_list[idy + 1]
            if item2 < item1:
                tmp = item2
                item2 = item1
                item1 = tmp
                input_list[idy] = item1
                input_list[idy + 1] = item2
    return input_list


def delete_repeat_item(input_list):
    output_list = list()
    original = -1
    for item in input_list:
        if item != original:
            output_list.append(item)
            original = item
    return output_list


if __name__ == '__main__':
    my_list = init_list(100)
    sorted_list = bubble_sort(my_list)
    no_repeat_list = delete_repeat_item(sorted_list)
    print('initial list: {}'.format(my_list))
    print('sorted list: {}'.format(sorted_list))
    print('no-repeat list: {}'.format(no_repeat_list))
