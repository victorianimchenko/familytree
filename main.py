from person import Person, FamilyMember

def display_parents_name(person_info, name):
    list_ids = FamilyMember(name).find_parents_ids(person_info)
    names_list = FamilyMember(name).find_parents_name(list_ids)

    for item in names_list:
         print(item)

    return names_list

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
    print(f"{name}'s Parents:")
    names_list = display_parents_name(data, name)


# find grandparents
    print(f"{name}'s grandparents:")
    for parent_name in names_list:
        parent_info = Person(name).find_person(parent_name)
        display_parents_name(parent_info, name)
        
  





if __name__ == "__main__":
    main()

    