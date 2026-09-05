class StudentPerformanceAgent:

    def __init__(self, attendance, internal_marks, assignment_marks):
        self.attendance = attendance
        self.internal_marks = internal_marks
        self.assignment_marks = assignment_marks

    def predict(self):

        if (self.attendance >= 75 and
            self.internal_marks >= 75 and
            self.assignment_marks >= 75):

            return "Excellent Performance"

        elif (self.attendance >= 60 and
              self.internal_marks >= 50 and
              self.assignment_marks >= 50):

            return "Good Performance"

        else:
            return "Needs Improvement"

    def improvement_suggestions(self):

        suggestions = []

        if self.attendance < 75:
            suggestions.append(
                "Improve attendance to at least 75%."
            )

        if self.internal_marks < 75:
            suggestions.append(
                "Improve internal marks by studying regularly."
            )

        if self.assignment_marks < 75:
            suggestions.append(
                "Complete assignments properly and improve assignment marks."
            )

        if not suggestions:
            suggestions.append(
                "Excellent! Maintain your current performance."
            )

        return suggestions

    def display_result(self):

        result = self.predict()
        suggestions = self.improvement_suggestions()

        print("\n--- Student Performance Report ---")

        print("Attendance:", self.attendance, "%")
        print("Internal Marks:", self.internal_marks)
        print("Assignment Marks:", self.assignment_marks)

        print("\nPerformance Prediction:", result)

        print("\nWhat You Need to Improve:")

        for suggestion in suggestions:
            print("-", suggestion)


# Get student input
attendance = float(input("Enter attendance percentage: "))
internal_marks = float(input("Enter internal marks: "))
assignment_marks = float(input("Enter assignment marks: "))


# Create the AI agent
agent = StudentPerformanceAgent(
    attendance,
    internal_marks,
    assignment_marks
)

# Display result
agent.display_result()