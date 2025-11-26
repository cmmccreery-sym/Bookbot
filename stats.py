def count_words(content: str) -> int:
    return len(content.split())


def get_character_count(content: str) -> dict[str,int]:
    char_stats = {} 
    for char in list(content.lower()):
        char_stats[char] = char_stats.get(char, 0) + 1

    return char_stats


def sort_dict(character_count: dict[str, int]) -> list[dict[str, int]]:
    result = [] 
    for key in character_count:
        char_dict = {
            "char": key,
            "num": character_count[key]
        }

        result.append(char_dict)

    result.sort(key=lambda x: x["num"], reverse=True)
    return result
