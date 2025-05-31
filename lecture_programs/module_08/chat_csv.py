# ChatGPT - CSV File
import csv

test_name = "students.csv"

def write_csv(csv_name, data):
    with open(csv_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f"✅ CSV file '{csv_name}' created!")

def open_csv(csv_name):
    with open(csv_name, "r") as csvfile:
        header = next(csvfile)
        h_name, h_age, h_grade = header.strip().split(",")
        print(f"   {h_name.upper():^10} | {h_age.upper():^6} | {h_grade.upper():^8}")
        print("=" * 29)
        reader = csv.reader(csvfile)
        for line in reader:
            name, age, grade = line
            print(f"👤 {name:<10} | {age:^6} | {grade:^8}")

def grade_stats(csv_name):
    grade_counts = {}
    total_rows = 0

    with open(csv_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skips header

        for row in reader:
            grade = row[2]
            total_rows += 1
            if grade in grade_counts:
                grade_counts[grade] += 1
            else:
                grade_counts[grade] = 1

    print("📊 Grade Counts:")
    for grade, count in grade_counts.items():
        percentage = (count / total_rows) * 100
        print(f"{grade}: {count:>4} ({percentage:.1f}%)")


grade_stats(test_name)
