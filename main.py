from dictionaries import family_tree
from person import Person, FamilyMember


def main():
  
    print("Welcome to the Green Witch Hall!")
    IMMEDIATE_TYPES= ['spouses', 'children', 'parents', 'sibling']
    EXTENDED_TYPES = ['spouses', 'children', 'parents', 'sibling', 'aunt', 'cousin']

    name = 'Cornelia Emmersohn'

    tree = FamilyMember(family_tree)
    data = tree.find_person(name)

    print(data, 'Find person')

    # find siblings
    siblings_name = tree.find_member_list_names(data, 'sibling')
    tree.print_family_names(name, siblings_name, 'sibling')

    #  find grandchildren    
    grandchildren = tree.get_grandchildren()



    tree.immediate_family(IMMEDIATE_TYPES)
    tree.extended_family(data, EXTENDED_TYPES)

if __name__ == "__main__":
    main()