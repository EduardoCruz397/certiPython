from turtle import forward


def reverse_name(backward_name):
    forward_name = ""
    length = len(backward_name)
    while length > 0:
        forward_name += backward_name[length-1]
        length = length - 1
    return forward_name


print(reverse_name("odraudE aloh"))