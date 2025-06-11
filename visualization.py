# visualization.py
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP', 'Swift']
popularity = [85, 79, 65, 55, 50, 45, 40]
job_demand = [90, 88, 75, 60, 65, 40, 38]
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(languages)))

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Programming Language Analysis', fontsize=18, fontweight='bold', color='#2a4a7c')

# Horizontal bar chart
bars = ax1.barh(languages, popularity, color=colors, edgecolor='black')
ax1.set_title('Developer Popularity (2023)', fontsize=14, pad=15)
ax1.set_xlabel('Popularity Index (%)', fontsize=12)
ax1.set_ylabel('Programming Language', fontsize=12)
ax1.grid(axis='x', linestyle='--', alpha=0.7)
ax1.invert_yaxis()  # Most popular at top

# Add value labels to bars
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 1, bar.get_y() + bar.get_height()/2, 
            f'{width:.0f}%', 
            ha='left', va='center',
            fontsize=10)

# Pie chart with explosion
explode = [0.1 if lang == 'Python' else 0 for lang in languages]
wedges, texts, autotexts = ax2.pie(job_demand, 
                                   labels=languages, 
                                   autopct='%1.0f%%', 
                                   startangle=90,
                                   colors=colors,
                                   explode=explode,
                                   shadow=True,
                                   textprops={'fontsize': 10})
ax2.set_title('Job Market Demand', fontsize=14, pad=15)

# Customize pie chart labels
plt.setp(autotexts, size=10, weight='bold', color='white')

# Add annotation
fig.text(0.5, 0.01, 
         'Data Visualization: Humans process visuals 60,000x faster than text | Source: Developer Survey 2023', 
         ha='center', fontsize=10, style='italic', alpha=0.7)

# Adjust layout and save
plt.tight_layout()
plt.subplots_adjust(top=0.9, bottom=0.1)
plt.savefig('language_analysis.png', dpi=300, bbox_inches='tight')
plt.show()