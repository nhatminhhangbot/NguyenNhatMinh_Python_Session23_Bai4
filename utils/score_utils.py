def calculate_average(scores):
    """
    Input: scores (danh sách điểm của một sinh viên - list)
    Output: điểm trung bình của sinh viên (float, làm tròn 2 chữ số thập phân)
    Module chứa hàm: utils/score_utils.py
    """
    if not scores or not isinstance(scores, list):
        return 0.0

    valid_scores = [s for s in scores if isinstance(s, (int, float))]

    if not valid_scores:
        return 0.0

    return round(sum(valid_scores) / len(valid_scores), 2)


def classify_student(average):
    """
    Input: average (điểm trung bình - float)
    Output: xếp loại học lực ("Giỏi", "Khá", "Trung bình", "Yếu")
    Module chứa hàm: utils/score_utils.py
    """
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
