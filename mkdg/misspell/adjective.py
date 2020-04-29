"""
형용사
"""
from mkdg.utils.chgword import chg_word
from mkdg.utils.getmisspell import misspell_single_data


def load_adjective():
    """
    Load adjective data

    Returns: adjective dictionary, alternative list
    """
    filename = "data/adjective.csv"
    adjective = misspell_single_data(filename)
    alternative = {

    }
    return adjective, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    adjective, alt = load_adjective()
    result = chg_word(test, adjective)  # , alt)
    print("Result: ", result)
