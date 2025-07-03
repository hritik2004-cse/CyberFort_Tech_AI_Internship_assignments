# 1. Tuple Operations – Immutable Data in Action
# Create a tuple of 10 fruits.
fruit_tuple = ("apple","mango","grapes","banana","watermelon","strawberry","peaches","papaya","guava","kiwi");

# Print fruits from index 3 to 7
print(fruit_tuple[3:7]);

# Use a loop to print the tuple in reverse order without using slicing.
for i in range(len(fruit_tuple)-1,-1,-1):
    print(fruit_tuple[i]);
    
# Convert the tuple into a list, update one item, and convert it back to a tuple.
fruit_tuple = list(fruit_tuple);
fruit_tuple[0]="Avocado";
print(fruit_tuple);
print("fruit_tuple changed type is :" , type(fruit_tuple));

againChange = tuple(fruit_tuple);
print(fruit_tuple);
print("again type is :",type(fruit_tuple));

# Create a nested tuple of (fruit, quantity) pairs and access quantities.
fruit_quantity = (
    ("apple",24),
    ("mango",43),
    ("grapes",46)
    );

for fruit,qty in fruit_quantity:
    print(qty);
    
# 2. Advanced Set Logic
# Create two sets of students enrolled in “AI” and “ML” courses respectively.
aiStudents = {"ankit","shyam","govind","aayan","ashwani","shivam","nikhil"};
mlStudents = {"aayan","ajay","shyam","nikhil","aarti","mohit","shivam"};

 # Find students:
# Enrolled in both courses
bothCourseStudents = aiStudents.intersection(mlStudents);
print(bothCourseStudents);

# Enrolled in only one course (either AI or ML but not both)
oneCourseStudents = aiStudents.symmetric_difference(mlStudents);
print(oneCourseStudents);

# Enrolled in at least one course
atLeastOneCourse = aiStudents.union(mlStudents);
print(atLeastOneCourse);

# Not enrolled in either course (from a full class list)

fullClassList = ["ananya","ankit","shyam","govind","aayan","shivam","ajay","amit","ashwani","nikhil","aayan","ajay","aarti","mohit","shivam","amit","punit","raja"];
changedList = set(fullClassList);
notEnrolledStudents = changedList.symmetric_difference(atLeastOneCourse);
print(notEnrolledStudents);

# Remove duplicate student entries from a long list using sets.
print(changedList);