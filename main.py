from person import Person, FamilyMember


def main():
    print('h')
    # name = Person('Baba Calaba', 1990, 1991)
    # print(name)
    # x = FamilyMamber('Baba Calaba', 1990).print_member()

    # person = input('Enter individual name to show siblings: ')
    person = 'Cornelia Emmersohn'
    age = input('Enter individual name to show siblings: ')
    # Cornelia Emmersohn
    data = Person(person).find_person(person)

    siblings_ids = FamilyMember(person).find_siblings(data)
    siblings_name = FamilyMember(person).find_sibling_names(siblings_ids)


if __name__ == "__main__":
    main()

    