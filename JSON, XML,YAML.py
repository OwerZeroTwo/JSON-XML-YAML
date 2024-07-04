import json

def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        data = json.load(file)

    sort_type = sort_type.lower()

    for employee in data['employees']:
        if sort_type in [key.lower() for key in employee.keys()]:
            break
    else:
        raise ValueError('Bad key for sorting')

    data['employees'].sort(key=lambda x: x.get(sort_type.capitalize(), x.get(sort_type.upper(), x.get(sort_type, ''))), reverse=sort_type.isdigit())

    with open(f'employees_{sort_type}_sorted.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open(f'employees_{sort_type}_sorted_2.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open(f'employees_{sort_type}_sorted_3.json', 'w') as file:
        json.dump(data, file, indent=4)

# Test the function
employees_rewrite('lastname')