def normalize_student_names(records):
    """
    Input: records (danh sách toàn bộ sinh viên - list[dict])
    Output: cập nhật trực tiếp tên đã chuẩn hóa vào records, in kết quả ra terminal
    Module chứa hàm: utils/string_utils.py
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for record in records:
        raw_name = record.get("name", "")
        clean_name = " ".join(raw_name.split()).title()
        record["name"] = clean_name
        print(f"{record['student_id']}: {clean_name}")
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")
