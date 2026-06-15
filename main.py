from data.students import student_records  # Kiểu import 1: from... import...
from utils import random_utils             # Kiểu import 2: from... import module
import utils.string_utils                  # Kiểu import 3: import package.module
# Kiểu import 4: import module as alias
import reports.report_generator as report


def main():
    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")

        try:
            choice = input("Chọn chức năng (1-5): ").strip()
            if not choice:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5!")
                continue
            choice = int(choice)

            if choice == 1:
                report.display_student_scores(student_records)
            elif choice == 2:
                utils.string_utils.normalize_student_names(student_records)
            elif choice == 3:
                print("\n--- SINH MÃ BÀI TẬP ---")
                code = random_utils.generate_assignment_code()
                print(f"Mã bài tập của bạn là: {code}")
            elif choice == 4:
                report.export_learning_report(student_records)
            elif choice == 5:
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5!")
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5!")


if __name__ == "__main__":
    main()
