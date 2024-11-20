from dictionary1 import family_tree_data

class FamilyTree:
    def __init__(self):
        self.members = family_tree_data

    def add_member(self, person):
        """
        Додати нового члена родини до словника.
        :param person: Об'єкт Person
        """
        self.members[person.person_id] = person

    def find_person(self, person_id):
        """
        Знайти особу за унікальним ідентифікатором.
        :param person_id: Унікальний ідентифікатор
        :return: Об'єкт Person або None
        """
        return self.members.get(person_id)

    def get_siblings(self, person_id):
        """
        Знайти братів та сестер для особи.
        :param person_id: Унікальний ідентифікатор особи
        :return: Список об'єктів Person
        """
        person = self.find_person(person_id)
        if not person:
            return []

        siblings = set()
        for parent_id in person.parents:
            parent = self.find_person(parent_id)
            if parent:
                siblings.update(parent.children)
        siblings.discard(person_id)  # Виключити самого себе
        return [self.find_person(sibling_id) for sibling_id in siblings]

    def get_cousins(self, person_id):
        """
        Знайти двоюрідних братів і сестер (кузенів) для особи.
        :param person_id: Унікальний ідентифікатор особи
        :return: Список об'єктів Person
        """
        person = self.find_person(person_id)
        if not person:
            return []

        cousins = set()
        for parent_id in person.parents:
            parent = self.find_person(parent_id)
            if parent:
                for sibling_id in parent.parents:
                    sibling = self.find_person(sibling_id)
                    if sibling:
                        cousins.update(sibling.children)
        return [self.find_person(cousin_id) for cousin_id in cousins]

    def display_siblings(self, person_id):
        """
        Вивести список братів та сестер особи.
        :param person_id: Унікальний ідентифікатор особи
        """
        siblings = self.get_siblings(person_id)
        person = self.find_person(person_id)
        if siblings:
            print(f"Siblings of {person.name}: {[str(sibling) for sibling in siblings]}")
        else:
            print(f"{person.name} has no siblings.")

    def display_cousins(self, person_id):
        """
        Вивести список двоюрідних братів та сестер.
        :param person_id: Унікальний ідентифікатор особи
        """
        cousins = self.get_cousins(person_id)
        person = self.find_person(person_id)
        if cousins:
            print(f"Cousins of {person.name}: {[str(cousin) for cousin in cousins]}")
        else:
            print(f"{person.name} has no cousins.")
