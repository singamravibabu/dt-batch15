address = {
    "E01": {"name": "anand", "age": 40, "dept": "sales", "skill": "training", "city": "hyd"},
    "E02": {"name": "raju", "age": 38, "dept": "hr", "skill": "recruitment", "city": "amr"},
    "E03": {"name": "kiran", "age": 42, "dept": "it", "skill": "excel", "city": "che"},
    "E04": {"name": "suman", "age": 35, "dept": "finance", "skill": "payrolls", "city": "blr"}
}

# Accessing specific employee details
print(address["E01"])  # {'name': 'anand', 'age': 40, 'dept': 'sales', 'skill': 'training', 'city': 'hyd'}
print(address["E02"])  # {'name': 'raju', 'age': 38, 'dept': 'hr', 'skill': 'recruitment', 'city': 'amr'}

# Accessing specific fields of an employee
print(address["E01"]["name"])  # 'anand'
print(address["E01"]["city"])  # 'hyd'
print(address["E01"]["dept"])  # 'sales'
print(address["E02"]["age"])   # 38
