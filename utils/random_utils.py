import random
import string


def generate_assignment_code():
    """
    Input: không có
    Output: mã bài tập định dạng PY-[4 ký tự chữ hoa hoặc số] (str)
    Module chứa hàm: utils/random_utils.py
    """
    pool = string.ascii_uppercase + string.digits
    random_chars = random.choices(pool, k=4)
    suffix = "".join(random_chars)
    return f"PY-{suffix}"
