def main():
    integer_list = []
    ls = input("Please enter a list of positive integers (comma separated): ")
    for i in ls.split(","):
        if i < 0:
            print("Error: Negative integer entered")
            return
        integer_list.append(i)
    return largest_number(integer_list)

def largest_number(i_list):
    list_of_lists = []
    for i in i_list:
        inner_list = []
        for j in str(i):
            inner_list.append(int(j))
        inner_list.append(i)
        list_of_lists.append(inner_list)
        
    list_of_lists = sorted(list_of_lists)
    list_of_lists.reverse()
    output = ""
    for i in range(0, len(list_of_lists)):
        output = output + str(list_of_lists[i][-1])
    return int(output)

        
