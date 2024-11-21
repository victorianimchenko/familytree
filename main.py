from person import Person, FamilyMember

def get_parents_name(person_info, name):
    list_ids = FamilyMember(name).find_parents_ids(person_info)
    names_list = FamilyMember(name).find_parents_name(list_ids)
    return names_list

def get_children_name(person_info, name):
    list_ids = FamilyMember(name).find_children(person_info)
    names_list = FamilyMember(name).find_children_name(list_ids)
    return names_list


def main():
  
    print("Welcome to the Green Witch Hall!")
    # name = Person('Baba Calaba', 1990, 1991)
    # print(name)
    # x = FamilyMamber('Baba Calaba', 1990).print_member()

    # person = input('Enter individual name to show siblings: ')
    name = 'Suki Gandi'
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
    parents_list = get_parents_name(data, name)
    if not parents_list:
      print('Not found')
    else:
        for item in parents_list:
         print(item)


# find grandchildren
    print(f"{name}'s grandchildren:")
           
    children = get_children_name(data, name)
    granchildren = None
    for child in children:
        child_info = Person(name).find_person(child)
        print('child info', child_info)
        granchildren = get_children_name(child_info, child)

    if not granchildren:
      print('Not found')
    else:
        for item in granchildren:
         print(item)
        
        
  





if __name__ == "__main__":
    main()

    