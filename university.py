university_object1 = {
    "name": "University of California, Berkeley",
    "location": "Berkeley, California"
}
university_object2 = {
    "name": "Stanford University",
    "location": "Stanford, California"
}
university_object3 = {
    "name": "Massachusetts Institute of Technology",
    "location": "Cambridge, Massachusetts"
}
university_object4 = {
    "name": "Harvard University",
    "location": "Cambridge, Massachusetts"
}
university_object5 = {
    "name": "University of Oxford",
    "location": "Oxford, England"
}

universities = [university_object1, university_object2, university_object3, university_object4, university_object5]

for university in universities:
    print(f"University Name: {university['name']}, Location: {university['location']}")
