import numpy as np


def form_report_data(key: str,
                     value: str,
                     general_data: tuple[int, int, list[tuple[str, str]]]) -> \
        tuple[int, int, list[tuple[str, str]]]:
    """
    Form the report data
    :param key: Attribute
    :param value: Result
    :param general_data: General data (max_len_lf, max_len_rt, data_list(key, value))
    """
    max_len_lf = general_data[0]
    max_len_rt = general_data[1]
    data_list = general_data[2]
    max_len_lf = max(max_len_lf, len(key))
    max_len_rt = max(max_len_rt, len(value))
    data_list.append((key, value))
    return max_len_lf, max_len_rt, data_list


def print_report_string(row: tuple[str, str], general_data: tuple[int, int]) -> None:
    """
    Print the report string
    :param row: tuple of data
    :param general_data: General data (max_len_lf, max_len_rt)
    """
    max_len_lf = general_data[0]
    max_len_rt = general_data[1]
    print(f" {f"{row[0]}":<{max_len_lf}} | {f"{row[1]}":<{max_len_rt}}")


def print_line_splitter(general_data: tuple[int, int]) -> None:
    """
    Print line splitter
    """
    max_len_lf = general_data[0]
    max_len_rt = general_data[1]
    print("-" * (max_len_lf + max_len_rt + 5))


def calc_cosine_similarity(v1, v2) -> tuple[float, float]:
    """
    Calculate the cosine similarity between two vectors
    :param v1: vector 1
    :param v2: vector 2
    :return: (cos(alpha), alpha_deg)
    """
    if min(len(v1), len(v2)) == 0:
        raise ValueError("At least one vector has zero dimension!")
    elif len(v1) != len(v2):
        raise ValueError("Vectors have different dimensions!")
    else:
        scalar_prod = v1 @ v2
        norm_v1 = np.linalg.norm(v1)
        norm_v2 = np.linalg.norm(v2)
        norm_v1_prod_norm_v2 = norm_v1 * norm_v2
        cos_alpha = scalar_prod / norm_v1_prod_norm_v2
        alpha_rad = np.arccos(cos_alpha)
        alpha_deg = np.degrees(alpha_rad)
    return cos_alpha, alpha_deg


def compare_values(val1, val2) -> str:
    """
    Comparing 2 values
    :param val1: value 1
    :param val2: value 2
    :return: sign "<", or ">", or "=="
    """
    if val1 == val2:
        return "=="
    elif val1 > val2:
        return ">"
    else:
        return "<"


def condition_check(val1: float, val2: float) -> str:
    """
    Checking the condition between 2 values
    :param val1: value 1
    :param val2: value 2
    :return: sign "==" or "!="
    """
    return "==" if val1 == val2 else "!="

def calc_vec_projection_and_residue(vec1: np.ndarray, vec2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculate the projection and residue of the vector 1 onto vector 2
    :param vec1: vector 1
    :param vec2: vector 2
    :return: (projection, residue)
    """
    projection = ((vec1 @ vec2) / (vec2 @ vec2)) * vec2
    residue = vec1 - projection
    return projection, residue
