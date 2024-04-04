import pandas as pd

# 1. Merge the data from greek_gods.csv and greek_goddesses.csv based on a common field
greek_gods_df = pd.read_csv('greek_gods.csv')
greek_goddesses_df = pd.read_csv('greek_goddesses.csv')

merged_table = pd.merge(greek_gods_df, greek_goddesses_df, how='outer', left_on='Domain', right_on='Domain', suffixes=('_god', '_goddess'))
print(merged_table)
print("********************************************************************************************************************************")

# 2. Filter the merged table to only include gods and goddesses who are older than 8000 years and sort them based on their ages in descending order
filtered_table = merged_table[(merged_table['Age_god'] > 8000) | (merged_table['Age_goddess'] > 8000)]
filtered_table = filtered_table.sort_values(by=['Age_god', 'Age_goddess'], ascending=False)
print(filtered_table)
print("********************************************************************************************************************************")

# 3. Join the two tables based on the "Domain" field and calculate the average age of gods and goddesses in each domain
domain_avg_age = merged_table.groupby('Domain')[['Age_god', 'Age_goddess']].mean()
print(domain_avg_age)
print("********************************************************************************************************************************")

# 4. Determine which god/goddess has the highest age, and then find out if they are a god or a goddess
max_age_god = filtered_table['Age_god'].max()
max_age_goddess = filtered_table['Age_goddess'].max()

if max_age_god > max_age_goddess:
    oldest_entity = filtered_table[filtered_table['Age_god'] == max_age_god].iloc[0]
    print(f"The oldest is {oldest_entity['God']} (God) with an age of {max_age_god} years.")
elif max_age_goddess > max_age_god:
    oldest_entity = filtered_table[filtered_table['Age_goddess'] == max_age_goddess].iloc[0]
    print(f"The oldest is {oldest_entity['Goddess']} (Goddess) with an age of {max_age_goddess} years.")
else:
    print("There is no god/goddess with the highest age.")

print("********************************************************************************************************************************")

# 5. Create a new column in each table called "Age_Group" and categorize the gods/goddesses into groups
def categorize_age(age):
    if age < 5000:
        return 'Young'
    elif 5000 <= age <= 8000:
        return 'Middle-aged'
    else:
        return 'Old'

greek_gods_df['Age_Group'] = greek_gods_df['Age'].apply(categorize_age)
greek_goddesses_df['Age_Group'] = greek_goddesses_df['Age'].apply(categorize_age)
print(greek_gods_df)
print()
print(greek_goddesses_df)
print("********************************************************************************************************************************")

# 6. Compare the average ages of gods and goddesses
avg_age_gods = greek_gods_df['Age'].mean()
avg_age_goddesses = greek_goddesses_df['Age'].mean()
age_difference = avg_age_gods - avg_age_goddesses
if age_difference > 0:
    print("Yes there is a significant age difference and Gods tend to be older than goddesses.")
elif age_difference < 0:
    print("Yes there is a significant age difference and Goddesses tend to be older than gods.")
else:
    print("The average ages of gods and goddesses are the same.")
print("********************************************************************************************************************************")

# 7. Print out the names of gods/goddesses who are older than 8000 years
older_than_8000 = merged_table[(merged_table['Age_god'] > 8000) | (merged_table['Age_goddess'] > 8000)]
print("Gods/Goddesses older than 8000 years:")
for index, row in older_than_8000.iterrows():
    print(row['God'] if pd.notna(row['God']) else row['Goddess'])
print("********************************************************************************************************************************")

# 8. Find the oldest god/goddess from the merged table using a while loop
merged_table['Age'] = merged_table[['Age_god', 'Age_goddess']].max(axis=1)
oldest_name = None
oldest_age = None
i = 0
while i < len(merged_table):
    row = merged_table.iloc[i]
    if oldest_age is None or row['Age'] > oldest_age:
        oldest_age = row['Age']
        oldest_name = row['God'] if pd.notna(row['God']) else row['Goddess']
    i += 1

print(f"The oldest god/goddess is {oldest_name} with an age of {oldest_age} years.")
