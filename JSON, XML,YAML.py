import json

def employees_rewrite(sort_type):
    try:
        with open('employees.json', 'r') as file:
            data = json.load(file)

        if sort_type not in ('firstname', 'lastname', 'department', 'salary'):
            raise ValueError('Bad key for sorting')

        key_to_sort = sort_type.lower()
        if key_to_sort == 'salary':
            key_to_sort = 'salary' if isinstance(data['employees'][0]['salary'], int) else 'salary_str'
        else:
            key_to_sort = key_to_sort.replace('name', 'Name')

        sorted_data = sorted(data['employees'], key=lambda x: x[key_to_sort])

        for i, employee in enumerate(sorted_data):
            employee['id'] = i

        with open(f'employees_{sort_type}_sorted.json', 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f'Error: {e}')

# Test the function
employees_rewrite('lastname')