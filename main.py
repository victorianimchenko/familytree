from person import Person, FamilyMember


def main():
  
    print("Welcome to the Green Witch Hall!")
    # name = Person('Baba Calaba', 1990, 1991)
    # print(name)
    # x = FamilyMamber('Baba Calaba', 1990).print_member()

    # person = input('Enter individual name to show siblings: ')
    name = 'Cornelia Emmersohn'
    # age = input('Enter individual name to show siblings: ')
    # Cornelia Emmersohn

# find person by name
    data = Person(name).find_person(name)
    
    print(data, 'Find person')


# find siblings
    siblings_ids = FamilyMember(name).find_siblings(data)
    siblings_name = FamilyMember(name).find_sibling_names(siblings_ids)

# find parents
    parents_ids = FamilyMember(name).find_parents_ids(data)
    names_list = FamilyMember(name).find_parents_name(parents_ids)

    print(f"{name}'s Parents:")
    for name in names_list:
        print(name)





if __name__ == "__main__":
    main()

    