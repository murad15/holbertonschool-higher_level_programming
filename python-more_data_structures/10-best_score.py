#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) < 1:
        return None
    else:
        new_dict = {k: v for k, v in sorted(a_dictionary.items(), key = lambda item: item[1], reverse = True)}
        best_key = list(new_dict.keys())[0]
        return best_key
