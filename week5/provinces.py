def main():
    entire_list = province_list("provinces.txt")

    #Print the entire list.
    print(entire_list)

    #Remove the first element from the list.
    del entire_list[0]
    #Remove the last element from the list.
    del entire_list[-1]

    list_count = len(entire_list)
    for i in range(list_count):
        if entire_list[i] == "AB":
            entire_list[i] = "Alberta"

    count = 0
    for province in entire_list:
        if province == "Alberta":
            count += 1

    print(f"Alberta occurs {count} times in the modified list.")

def province_list(file_provinces):
    entire_province_list = []
    with open("week5/provinces.txt", "rt") as province_file:
        for line in province_file:
            clean_line = line.strip()
            entire_province_list.append(clean_line)
    return entire_province_list

# Call main to start this program.
if __name__ == "__main__":
    main()