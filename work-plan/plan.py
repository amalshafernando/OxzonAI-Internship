from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="100-Hour Weekly Study Plan", ln=True, align="C")
pdf.ln(10)

# Intro text
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, txt="""To study 100 hours per week, you will need to allocate time each day. Here’s a plan that helps you achieve your goal while maintaining productivity.

Based on your target of 100 hours, you'll need to study approximately 14.3 hours per day.

The schedule has been divided into manageable study blocks, with breaks to ensure you stay focused and avoid burnout.

Here is a suggested daily schedule for studying:

""")

# Schedule Table
pdf.set_font('Arial', '', 12)
schedule = [
    ("6:00 AM - 9:00 AM", "Study (3 hours) - Focus on high-concentration tasks, such as reading or problem-solving."),
    ("9:00 AM - 9:30 AM", "Break (30 minutes) - Stretch, walk, hydrate, or eat a snack."),
    ("9:30 AM - 12:30 PM", "Study (3 hours) - Continue with difficult topics, take notes, and review key concepts."),
    ("12:30 PM - 1:30 PM", "Lunch (1 hour) - Take a break and nourish yourself."),
    ("1:30 PM - 4:30 PM", "Study (3 hours) - Revise or work on assignments/projects."),
    ("4:30 PM - 5:00 PM", "Break (30 minutes) - Take a break, walk around, or relax briefly."),
    ("5:00 PM - 8:00 PM", "Study (3 hours) - Focus on more challenging or new material."),
    ("8:00 PM - 9:00 PM", "Dinner (1 hour) - Relax and enjoy a meal."),
    ("9:00 PM - 11:00 PM", "Study (2 hours) - Light review or practice exercises."),
    ("11:00 PM - 6:00 AM", "Sleep (7 hours) - Ensure proper rest for productivity.")
]

for time, activity in schedule:
    pdf.cell(0, 10, time, ln=True)
    pdf.multi_cell(0, 10, activity)
    pdf.ln(2)

# Tips Section
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Study Tips for Success:", ln=True, align="L")
pdf.set_font('Arial', '', 12)

tips = [
    "1. Prioritize High-Energy Times: Tackle the most challenging subjects during peak energy times.",
    "2. Stay Consistent: Stick to the schedule and make sure to balance study and rest.",
    "3. Use Active Learning: Engage with the material through problem-solving, teaching, or summarizing.",
    "4. Break Tasks Into Chunks: Divide study time into smaller tasks (e.g., 45-minute sessions).",
    "5. Stay Hydrated & Nourished: Take regular breaks, drink water, and eat healthy snacks.",
    "6. Weekend Adjustments: Shift study hours from weekends to weekdays if needed for flexibility."
]

for tip in tips:
    pdf.multi_cell(0, 10, tip)

# Save PDF
file_path = "/100_Hour_Weekly_Study_Plan.pdf"
pdf.output(file_path)

file_path
