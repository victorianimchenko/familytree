from dictionaries import family_tree

class Person:
    def __init__(self, name, birth_date=None, death_date=None):

        self.id = ''
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.parents = []  # Список ID батьків
        self.spouses = []  # Список ID партнерів
        self.children = []  # Список ID дітей
        

    def set_info(self, person_info):
       self.id = person_info.get('id')
       self.name = person_info.get('name')
       self.birth_date = person_info.get("birth_date")
       self.death_date = person_info.get("death_date")
       self.parents = person_info.get("parents") 
       self.spouses = person_info.get("spouses")
       self.children = person_info.get("children")

   #  def find_id_by_name(self, name):
   #      for person_id, details in family_tree.items():
   #        if details.get("name") == name:
   #          return person_id
   #        else:
   #            return None
          
   #  def find_person_by_id(self, person_id):

   #      for id, details in family_tree.items():

   #         if id == person_id:
   #            return {**details}
    
    
   #  def find_person(self, name):
   #      for person_id, details in family_tree.items():

   #        if details.get("name") == name:
   #            return {'id': person_id, **details}
          
    
    def __str__(self):
        return f"{self.name} (b. {self.birth_date}" + (f", d. {self.death_date}" if self.death_date else "") + ")"

class FamilyMember(Person):
    def __init__(self, family_tree):
        super().__init__(self, family_tree)
        self.family_tree_data = family_tree
        self.members = {}

    def find_person_by_name(self, name):
       for person_id, details in self.family_tree_data.items():
          if details.get("name") == name:
              return {'id': person_id, **details}
       
    def find_person(self, name):
        for person_id, details in family_tree.items():

          if details.get("name") == name:
              self.set_info({'id': person_id, **details})
              return {'id': person_id, **details}
    
    def find_parents_ids(self, person):
        return person.get('parents')
    
    def find_children(self, person):
       self.children = person.get('children')
       return person.get('children')
    
   #  def find_spouses_ids(self, person):
   #     return person.get('spouses')
    
   #  use UNI FUN
    def find_list_ids(self, person, type_member):
       return person.get(f'{type_member}')

    def get_aunt_ids(self, person):
       list_aunts = []
       parents = person.get('parents')

       for parent_id in parents:

          parent_info = self.family_tree_data[parent_id]
          sibling = self.find_siblings(parent_info)
          sibling.remove(parent_id)

          for sibling_id in sibling:
             list_aunts.append(sibling_id)
       return list_aunts

    
   #  use universal FUNCTION
    def find_member_list_names(self, person, type_member):
       list_ids = []


       if type_member == 'sibling':
          list_ids = self.find_siblings(person)
          list_ids.remove(self.id)

       elif type_member == 'aunt':

          list_ids = self.get_aunt_ids(person)

       elif type_member == 'cousin':

          list_aunt_ids = self.get_aunt_ids(person)
          list_ids = self.find_cousin(list_aunt_ids)
          
       else:
          list_ids = person.get(f'{type_member}')

       name_list = []
       for id in list_ids:
          parent_data = self.family_tree_data[id]
          parent_name = parent_data.get('name')
          name_list.append(parent_name)
       return name_list
   

    def filtered_alive_member(self, list_names):
      list = []
      for name in list_names:
         data = self.find_person_by_name(name)
         death_date = data.get("death_date")
         if death_date is None:
            list.append(name)
      return list
                   

    def find_siblings(self, person):
      siblings = []  # Змінюємо на список


    # Отримуємо список ідентифікаторів батьків
      parents_ids = person.get('parents', []) if person else self.parents

     
    # Перевіряємо, чи є батьки
      if not parents_ids:
          print('No parents found.')
          return siblings  # Повертаємо порожній список, якщо батьків немає
    
    # Проходимо по всіх батьках
      for parent_id in parents_ids:
          parent_info = family_tree.get(parent_id)
        
          if parent_info:
            # Знаходимо дітей для кожного з батьків
            children = self.find_children(parent_info)
            siblings.extend(children)  # Додаємо знайдених дітей до списку
          else:
             print(f'Parent ID {parent_id} not found in family_tree.')
    
    # Видаляємо ідентифікатор самої особи, якщо він є
      if self.id in siblings:
          siblings.remove(self.id)
      

    
    # Уникнення дублікатів, якщо це потрібно
      siblings = list(set(siblings))
    
      return siblings

    def find_aunt(self, list_sibling):
      list = []

      for parent in list_sibling:
        person_info = self.find_person(parent)

        sibling_person = self.find_siblings(person_info)

        for sibling in sibling_person:
            list.append(sibling)
      return list  
    
    def find_cousin(self, list_aunts):
      list_cousin = []

      for aunt in list_aunts:
        cousin_info = self.family_tree_data[aunt]
        cousin_children = cousin_info.get('children')

        for child in cousin_children:
            list_cousin.append(child)
            
      return list_cousin
    
    def get_grandchildren(self):
           children = self.children
           granchildren = None
    
           for child in children:
             child_info = self.family_tree_data[child]
             granchildren = self.find_member_list_names(child_info, 'children')

           self.print_family_names(self.name, granchildren, 'grandchilren')
           return granchildren
    
    def immediate_family(self, member_types):
       print('IMMEDIATE FAMILY')

       for member in member_types:
         list = self.find_member_list_names(self.family_tree_data[self.id], member)
         self.print_family_names(self.name, list, member)

    def extended_family(self, person, member_types):
      print('EXTENDED FAMILY')
     
      for member in member_types:
   
         list = self.find_member_list_names(person, member)
         filtered_list = self.filtered_alive_member(list)
         self.print_family_names(self.name, filtered_list, member)

    
    def print_family_names(self, name, list_names, type_member):
      print(f"{name} has {type_member}:")
      if not list_names:
        print('Not found')
      else:
        for item in list_names:
           print(item)
           
    def print_member(self):
        print(self.name)

    

