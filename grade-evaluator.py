mport csv
import os

FILE_NAME = "grades.csv"

def read_csv():
    if not os.path.exists(FILE_NAME):
        print("❌ grades.csv file not found.")
        return []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        if not data:
            print("⚠️ grades.csv is empty.")
            return []

        return data


def validate_scores(data):
    for row in data:
        score = float(row["score"])
        if score < 0 or score > 100:
            print(f"❌ Invalid score: {score}")
            return False
    return True


def validate_weights(data):
    total_weight = 0
    formative = 0
    summative = 0

    for row in data:
        weight = float(row["weight"])
        total_weight += weight

        if row["type"] == "Formative":
            formative += weight
        elif row["type"] == "Summative":
            summative += weight

    if total_weight != 100:
        print("❌ Total weight must be 100")
        return False

    if formative != 60 or summative != 40:
        print("❌ Formative must be 60 and Summative must be 40")
        return False

    return True


def calculate_results(data):
    total = 0
    formative_total = 0
    formative_weight = 0
    summative_total = 0
    summative_weight = 0

    failed_formative = []

    for row in data:
        score = float(row["score"])
        weight = float(row["weight"])
        category = row["type"]

        weighted_score = (score * weight) / 100
        total += weighted_score

        if category == "Formative":
            formative_total += weighted_score
            formative_weight += weight

            if score < 50:
                failed_formative.append(row)

        elif category == "Summative":
            summative_total += weighted_score
            summative_weight += weight

    # GPA
    gpa = (total / 100) * 5.0

    # Category percentages
    formative_percent = (formative_total / formative_weight) * 100
    summative_percent = (summative_total / summative_weight) * 100

    # Pass/Fail
    if formative_percent >= 50 and summative_percent >= 50:
        status = "PASSED"
    else:
        status = "FAILED"

    print(f"\n📊 GPA: {round(gpa, 2)}")
    print(f"📌 Status: {status}")

    # Resubmission
    if status == "FAILED" and failed_formative:
        max_weight = max(float(row["weight"]) for row in failed_formative)

        print("\n🔁 Resubmit these assignments:")
        for row in failed_formative:
            if float(row["weight"]) == max_weight:
                print(f"- {row['assignment']} (Weight: {row['weight']})")


def main():
    data = read_csv()
    if not data:
        return

    if not validate_scores(data):
        return

    if not validate_weights(data):
        return

    calculate_results(data)


if __name__ == "__main__":
    main(
