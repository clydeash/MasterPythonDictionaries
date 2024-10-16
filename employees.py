employee_object1 = {
    "name": "John Doe",
    "job_title": "Software Engineer"
}
employee_object2 = {
    "name": "Jane Doe",
    "job_title": "Data Scientist"
}
employee_object3 = {
    "name": "Peter Pan",
    "job_title": "Project Manager"
}
employee_object4 = {
    "name": "Wendy Darling",
    "job_title": "Product Designer"
}
employee_object5 = {
    "name": "Captain Hook",
    "job_title": "CEO"
}

employees = [employee_object1, employee_object2, employee_object3, employee_object4, employee_object5]

for employee in employees:
    print(f"Employee Name: {employee['name']}, Job Title: {employee['job_title']}")
