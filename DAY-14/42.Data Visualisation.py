import matplotlib.pyplot as plt

# 1. Simple Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [45, 50, 58, 65, 72, 78, 81, 83, 84, 85]

# 2. Initialize the plot with a clean, clear size
plt.figure("Student Study Efficiency",figsize=(8, 5))

# 3. Plot the data line with a distinct color and markers
plt.plot(study_hours, exam_scores, color='#1d4ed8', marker='o', linewidth=2.5, label='Student Score')

# 4. STORYTELLING: Highlight the key takeaway (The Diminishing Returns point)
# We highlight that studying past 6 hours yields very small score improvements.
plt.scatter(6, 7, color='#dc2626', s=120, zorder=5) # Red dot marker

plt.annotate(
    'Scores level off after 6 hours',
    xy=(6, 78),
    xytext=(2, 75),
    arrowprops=dict(facecolor='#334155', arrowstyle='->', lw=1.5),
    fontsize=10,
    fontweight='bold',
    color='#334155'
)

# 5. Clean and Clear Typography
plt.title('Study Efficiency: More Hours Do Not Always Mean Better Grades', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Hours Spent Studying', fontsize=11)
plt.ylabel('Final Exam Score (%)', fontsize=11)

# 6. Set proper limits and grids for readability
plt.xlim(0, 11)
plt.ylim(30, 100)
plt.grid(True, linestyle='--', alpha=0.5)

# Show the clean plot
plt.tight_layout()
plt.show()
