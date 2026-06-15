import datetime
from colorama import Fore, Style, init

# Import hàm từ package utils
from utils.score_utils import calculate_average, classify_student

init(autoreset=True)


def display_student_scores(records):
    """
    Input: records (danh sách toàn bộ sinh viên - list[dict])
    Output: in danh sách điểm và xếp loại ra terminal
    Module chứa hàm: reports/report_generator.py
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for index, record in enumerate(records, start=1):
        scores = record.get("scores", [])
        avg = calculate_average(scores)
        rank = classify_student(avg)

        print(
            f"{index}. [{record["student_id"]}] {record["name"]} | Điểm: {scores} | ĐTB: {avg:.2f} - {rank}")
    print("---------------------------------")


def export_learning_report(records):
    """
    Input: records (danh sách toàn bộ sinh viên - list[dict])
    Output: ghi file learning_report.txt, hiển thị thông báo thành công có màu trên terminal
    Module chứa hàm: reports/report_generator.py
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    pass_count = 0
    need_improve_count = 0

    for record in records:
        avg = calculate_average(record.get("scores", []))
        if avg >= 5.0:
            pass_count += 1
        else:
            need_improve_count += 1

    now = datetime.datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")

    filename = "learning_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=========================================\n")
        file.write("           BÁO CÁO HỌC TẬP               \n")
        file.write(f"Thời gian tạo: {current_time}\n")
        file.write("=========================================\n")
        file.write(f"Tổng số sinh viên: {total_students}\n")
        file.write(f"Số sinh viên đạt yêu cầu (ĐTB >= 5.0): {pass_count}\n")
        file.write(
            f"Số sinh viên cần cải thiện (ĐTB < 5.0): {need_improve_count}\n")
        file.write("=========================================\n")

    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {pass_count}")
    print(f"Số sinh viên cần cải thiện: {need_improve_count}")
    print(f"{Fore.GREEN}>> Đã xuất báo cáo ra file {filename}{Style.RESET_ALL}")
