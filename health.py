
import pandas as pd
import matplotlib.pyplot as plt
# Create or import a sample patient data
data_dict = {
    'Patient_ID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
    'Age': [45, 52, 38, 61, 33, 58, 42, 55],
    'BMI': [28.5, 35.2, 24.1, 33.8, 22.5, 36.1, 27.3, 34.5],
    'Blood_Pressure': [120, 140, 115, 145, 110, 150, 125, 142],
    'Glucose': [85, 180, 90, 195, 88, 200, 95, 185],
    'Insulin': [15, 25, 12, 28, 10, 30, 14, 26],
    'Diabetes': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data_dict)
print("Data Loaded")
# explore the data
print("\n Data Exploration")
print(df.head())
print("\n Dataset shape(rows,columns)")
print(df.shape)
print("\n Statistical Summary")
print(df.describe())
# **Separate into two groups**
diabetics= df[df['Diabetes'] == 'Yes']
non_diabetics= df[df['Diabetes']== 'No']
# 
# BMI
diabetic_bmi_avg = diabetics['BMI'].mean()
non_diabetic_bmi_avg = non_diabetics['BMI'].mean()

# Blood Pressure
diabetic_bp_avg = diabetics['Blood_Pressure'].mean()
non_diabetic_bp_avg = non_diabetics['Blood_Pressure'].mean()

# Glucose
diabetic_glu_avg = diabetics['Glucose'].mean()
non_diabetic_glu_avg = non_diabetics['Glucose'].mean()

# Insulin
diabetic_ins_avg = diabetics['Insulin'].mean()
non_diabetic_ins_avg = non_diabetics['Insulin'].mean()

# Calculate differences
bmi_diff = diabetic_bmi_avg - non_diabetic_bmi_avg
bp_diff = diabetic_bp_avg - non_diabetic_bp_avg
glu_diff = diabetic_glu_avg - non_diabetic_glu_avg
ins_diff = diabetic_ins_avg - non_diabetic_ins_avg

# difference
# Calculate differences for each metric
# ✅ CORRECT
comparison_data = {
    'Metric': ['BMI', 'Blood_Pressure', 'Glucose', 'Insulin'],
    'Non_Diabetic_Avg': [non_diabetic_bmi_avg, non_diabetic_bp_avg, 
                         non_diabetic_glu_avg, non_diabetic_ins_avg],
    'Diabetic_Avg': [diabetic_bmi_avg, diabetic_bp_avg, 
                     diabetic_glu_avg, diabetic_ins_avg],
    'Difference': [bmi_diff, bp_diff, glu_diff, ins_diff]
}

comparison_df = pd.DataFrame(comparison_data)
# ... and so on for other metrics
print("\nAnalysis:")
print(comparison_df['Difference'])
# sort
df_sorted = comparison_df.sort_values('Difference', ascending = False)
print("\nTop most active")
print(df_sorted.head())
# visualize
print("\n== Visualization==")
top5= df_sorted.head(5)
# Make it LinkedIn-ready
plt.figure(figsize=(12, 7))  # Bigger size
plt.bar(top5['Metric'], top5['Difference'], color='#0077B5')  # LinkedIn blue!

plt.xlabel('Health Metric', fontsize=14, fontweight='bold')
plt.ylabel('Difference (Diabetic - Non-Diabetic)', fontsize=14, fontweight='bold')
plt.title('Key Health Metrics: Diabetic vs Non-Diabetic Patients', 
          fontsize=16, fontweight='bold', pad=20)

# Add value labels on bars
for i, v in enumerate(top5['Difference']):
    plt.text(i, v + 2, f'+{v:.1f}', ha='center', fontweight='bold', fontsize=12)

plt.xticks(rotation=0, fontsize=12)  # Keep labels horizontal
plt.grid(axis='y', alpha=0.3)  # Subtle gridlines
plt.tight_layout()

# Save as high-quality image
plt.savefig('diabetes_analysis.png', dpi=300, bbox_inches='tight')
print("Chart saved!")

