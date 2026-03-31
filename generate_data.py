import pandas as pd
import random

n_students = 100

first_names = [
    "Anna", "Bo", "Clara", "David", "Evelina", "Filip", "Greta", "Hugo",
    "Ida", "Johan", "Klara", "Leo", "Maja", "Noah", "Olivia", "Pelle",
    "Rasmus", "Sara", "Tobias", "Vera"
]

last_names = [
    "Andersson", "Johansson", "Karlsson", "Nilsson", "Eriksson",
    "Larsson", "Olsson", "Persson", "Svensson", "Gustafsson"
]

courses = ["Matematik", "Svenska", "Engelska", "Historia", "Programmering"]

grades = ["A", "B", "C", "D", "E", "F"]

def generate_base_attendance():
    return max(50, min(100, random.gauss(90, 10)))

def vary_attendance(base):
    # liten variation per kurs
    return max(50, min(100, base + random.gauss(0, 5)))

def weighted_grade(attendance):
    weights = {
        "A": 5,
        "B": 15,
        "C": 40,
        "D": 20,
        "E": 15,
        "F": 5
    }
    
    boost = (attendance - 90) / 10

    weights["A"] += 5 * boost
    weights["B"] += 3 * boost
    weights["D"] -= 3 * boost
    weights["E"] -= 4 * boost
    weights["F"] -= 5 * boost

    weights = {k: max(1, v) for k, v in weights.items()}

    return random.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]

rows = []

for _ in range(n_students):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    age = random.randint(15, 20)
    base_attendance = generate_base_attendance()
    
    for course in courses:
        attendance = vary_attendance(base_attendance)
        
        rows.append({
            "name": name,
            "age": age,
            "course": course,
            "attendance": round(attendance, 1),
            "grade": weighted_grade(attendance)
        })

df = pd.DataFrame(rows)

df.to_csv('student_data.csv',index=False)