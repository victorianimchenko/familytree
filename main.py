from person import Person, FamilyMember

def get_parents_name(person_info, name):
    list_ids = FamilyMember(name).find_parents_ids(person_info)
    names_list = FamilyMember(name).find_parents_name(list_ids)
    return names_list

def get_children_name(person_info, name):
    list_ids = FamilyMember(name).find_children(person_info)
    names_list = FamilyMember(name).find_children_name(list_ids)
    return names_list


def get_siblings(sibling_info, name):
   siblings_ids = FamilyMember(name).find_siblings(sibling_info)
   siblings_name = FamilyMember(name).find_sibling_names(siblings_ids)
   return siblings_name

def get_spouses(person_info, name):
    spouses_ids = FamilyMember(name).find_spouses_ids(person_info)
    spouses_name = FamilyMember(name).find_spouses_name(spouses_ids)
    return spouses_name


def print_family_names(name, list_names, type_member):
   print(f"{name} has {type_member}:")
   if not list_names:
      print('Not found')
   else:
      for item in list_names:
         print(item)


def immediate_family(person, name):
   list_parents = get_parents_name(person, name)
   print_family_names(name, list_parents, "parents")

   list_children = get_children_name(person, name)
   print_family_names(name, list_children, "children")
         
         
   list_siblings = get_siblings(person, name)
   print_family_names(name, list_siblings, "siblings")
   
   list_spouses = get_spouses(person, name)
   print_family_names(name, list_spouses, "spouses")
 
  



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
    sibling_list = get_siblings(data, name)
    print_family_names(name, sibling_list, 'sibling')

# find parents
    
    parents_list = get_parents_name(data, name)
    print_family_names(name, parents_list, 'parents')


# find grandchildren    
    children = get_children_name(data, name)
    granchildren = None
    
    for child in children:
        child_info = Person(name).find_person(child)
        granchildren = get_children_name(child_info, child)

    print_family_names(name, granchildren, 'grandchildren')
        
# immediate family (parents, children, spouse, siblings)
    immediate_family(data, name)
  





if __name__ == "__main__":
    main()

    