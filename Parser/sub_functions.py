def dict_preprocessing(dict_last_iteration: dict, dict_new_itrearion: dict) -> dict:
    utility_dict: dict = dict_new_itrearion.copy()
    dict_new_itrearion: dict = {**utility_dict, **dict_last_iteration}
    return dict_new_itrearion
