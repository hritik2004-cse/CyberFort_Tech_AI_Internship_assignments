fruit_tuple = ("apple","mango","grapes","banana","watermelon","strawberry","peaches","papaya","guava","kiwi");
print(fruit_tuple[3:7]);

fruit_tuple = list(fruit_tuple);
fruit_tuple[0]="Avocado";
print(fruit_tuple);
print("fruit_tuple changed type is :" , type(fruit_tuple));

againChange = tuple(fruit_tuple);
print(fruit_tuple);
print("again type is :",type(fruit_tuple));

fruit_quantity = (
    ("apple",24),
    ("mango",43),
    ("grapes",46)
    );

aiStudents = {"ankit","shyam","govind","aayan","ashwani","shivam","nikhil"};
mlStudents = {"aayan","ajay","shyam","nikhil","aarti","mohit","shivam"};

bothCourseStudents = aiStudents.intersection(mlStudents);
print(bothCourseStudents);

oneCourseStudents = aiStudents.symmetric_difference(mlStudents);
print(oneCourseStudents);

atLeastOneCourse = aiStudents.union(mlStudents);
print(atLeastOneCourse);