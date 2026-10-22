
def parse_student(line):
    parts = line.strip().split(',')
    if len(parts) != 2:
        raise ValueError("字段数量不对")

    name = parts[0].strip()
    if not name:
        raise ValueError("姓名为空")

    try:
        score = int(parts[1].strip())
    except ValueError:
        raise ValueError("成绩不是整数")

    if score < 0 or score > 100:
        raise ValueError("成绩超出0-100范围")

    return {"name": name, "score": score}
