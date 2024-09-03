import pandas as pd
import matplotlib.pyplot as plt

# User input for data
num_entries = int(input("Enter the number of entries: "))

data = {
    "ID": [],
    "Age": [],
    "Gender": [],
    "Salary": [],
    "Purchased": []
}

for i in range(num_entries):
    data["ID"].append(i + 1)
    age = int(input(f"Enter Age for entry {i + 1}: "))
    gender = input(f"Enter Gender (Male/Female) for entry {i + 1}: ")
    salary = int(input(f"Enter Salary for entry {i + 1}: "))
    purchased = input(f"Purchased? (Yes/No) for entry {i + 1}: ")
    
    data["Age"].append(age)
    data["Gender"].append(gender)
    data["Salary"].append(salary)
    data["Purchased"].append(purchased)

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
df.groupby('Gender')['Salary'].mean().plot(kind='bar', color=['blue', 'orange'])
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.legend(['Average Salary'])
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Age'], df['Salary'], marker='o', linestyle='-', color='green')
plt.title('Salary by Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(['Salary'])
plt.grid(True)
plt.show()
