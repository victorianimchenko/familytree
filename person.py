from dictionaries import family_tree

class Person:
    def __init__(self, name, birth_year=None, death_year=None):
        """
        Ініціалізація об'єкта Person.

        :param person_id: Унікальний ідентифікатор особи
        :param name: Ім'я особи
        :param birth_year: Рік народження
        :param death_year: Рік смерті (або None, якщо особа ще жива)
        """

        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
        self.parents = []  # Список ID батьків
        self.spouses = []  # Список ID партнерів
        self.children = []  # Список ID дітей
        self.members = family_tree

    def find_id_by_name(self, name):
        for person_id, details in family_tree.items():
          if details.get("name") == name:
            return person_id
          else:
              return None
          
    def find_person_by_id(self, person_id):

        for id, details in family_tree.items():

           if id == person_id:
              return {**details}
    
    
    def find_person(self, name):
        for person_id, details in family_tree.items():

          if details.get("name") == name:
              return {'id': person_id, **details}
          
    
    def __str__(self):
        return f"{self.name} (b. {self.birth_year}" + (f", d. {self.death_year}" if self.death_year else "") + ")"

class FamilyMember(Person):
    def __init__(self, name, birth_year=None):
        super().__init__(name, birth_year)

    def find_parents_ids(self, person):
        return person.get('parents')
    
    def find_parents_name(self, parents_ids):
       name_list = []
       for id in parents_ids:
          parent_data = self.find_person_by_id(id)
          parent_name = parent_data.get('name')
          name_list.append(parent_name)
       return name_list
          
    
    def find_children(self, person):
       return person.get('children')
    
    def find_children_name(self, children_ids):
       name_list = []
       for id in children_ids:
          children_data = self.find_person_by_id(id)
          children_name = children_data.get('name')
          name_list.append(children_name)
       return name_list
       
    def find_siblings(self, person):
       siblings = set()

       parents_ids = self.find_parents_ids(person)

       for id in parents_ids:
         parent_info = self.find_person_by_id(id)
         children = self.find_children(parent_info)
         siblings.update(children)
       
       siblings.discard(person["id"])

       return siblings
    
    def find_sibling_names(self, sibling_ids):
       for id in sibling_ids:
          print(self.find_person_by_id(id))


       
        
    
    def print_member(self):
        print(self.name)

    

