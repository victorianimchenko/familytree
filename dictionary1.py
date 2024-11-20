family_tree_data = {
    "1": {
        "name": "Cornelia Emmersohn",
        "birth_year": 1970,
        "death_year": None,
        "parents": ["3", "4"],  # Посилання на унікальні ID батьків
        "spouses": ["2"],  # Посилання на унікальний ID партнера
        "children": ["5", "6"]  # Посилання на унікальні ID дітей
    },
    "2": {
        "name": "Otto Emmersohn",
        "birth_year": 1968,
        "death_year": None,
        "parents": ["7", "8"],
        "spouses": ["1"],
        "children": ["5", "6"]
    },
    "3": {
        "name": "Anjali Patel",
        "birth_year": 1945,
        "death_year": None,
        "parents": [],
        "spouses": ["4"],
        "children": ["1", '4']
    },
    "4": {
        "name": "Rajiv Patel",
        "birth_year": 1943,
        "death_year": 1999,
        "parents": [],
        "spouses": ["3"],
        "children": ["1"]
    },
    "5": {
        "name": "Child 1",
        "birth_year": 1995,
        "death_year": None,
        "parents": ["1", "2"],
        "spouses": [],
        "children": []
    },
    "6": {
        "name": "Child 2",
        "birth_year": 1998,
        "death_year": None,
        "parents": ["1", "2"],
        "spouses": [],
        "children": []
    },
    "7": {
        "name": "Heinrich Emmersohn",
        "birth_year": 1938,
        "death_year": None,
        "parents": [],
        "spouses": ["8"],
        "children": ["2"]
    },
    "8": {
        "name": "Elisabeth Schmidt",
        "birth_year": 1940,
        "death_year": 2001,
        "parents": [],
        "spouses": ["7"],
        "children": ["2"]
    }
}
