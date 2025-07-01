# ✅ Tasks:
# 🟣 Tuples
# Create a tuple with 5 favorite movies.

fav_movies = ("Stranger Things","Squid Game","Money Heist","Alice in Borderland","The Lion King");

# Access and print the third movie.
print(fav_movies[2]);

#Try modifying one element of the tuple and observe the error (write the error message in a comment).
# fav_movies[1]="Avengers Endgame"; 
print(fav_movies);#This will throw error

# 🟢 Sets
# Take a list with duplicate numbers and convert it to a set.
lst = [1,2,3,3,2,4,5,6];
new_set = set(lst);#converting list into set
print(new_set);

# Perform the following operations:

# Add a new number to the set
new_set.add(7);
print(new_set);

# Remove a number from the set (using .remove())
new_set.remove(2);
print(new_set);

# Find the union of two sets: {1, 2, 3} and {3, 4, 5}
set_1 = {1,2,3};
set_2 = {4,5,6};

set_union = set_1.union(set_2);
print(set_union);

# 🟠 Dictionaries
# Create a dictionary for a student with keys: name, roll_no, and marks.
student = {
     "Name":"Hritik Sharma",
     "Roll_no":1234,
     "Marks":560
 };

# Add a new key grade and assign a value.
student["Branch"]= "CSE";

# Update the marks key with new marks.
print("before update Marks :",student["Marks"]);
student.update({"Marks":570});
print("after update Marks :",student["Marks"]);

# Loop through the dictionary and print all keys and their values.
for keys in student:
    print(student[keys]);

# 🎯 Bonus Challenge (Optional):
# Create a dictionary with subject names as keys and marks as values.

stu_subjects={
    "Hindi":37,
    "English":31,
    "Maths":29,
    "Science":41,
    "Sst":39
};

print(stu_subjects);

# Write a loop to calculate and print the average marks.
total= 0;

for stu_marks in stu_subjects.values():
    total += stu_marks;

avg = total/len(stu_subjects);
print(f"average of marks is {avg}");    
    
