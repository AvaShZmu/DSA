def move_to_end(lst, val):
    ans = []

    def subfunc(lst, val, ans):
        for i, temp_val in enumerate(lst):
            if temp_val != val:
                new_lst = lst[:i] + lst[i + 1:]
                return ans + [temp_val] + subfunc(new_lst, val, ans)
        else:
            return ans + lst

    return subfunc(lst, val, ans)


gemstones = ["Ruby", "Ruby", "Sapphire", "Ruby", "Emerald", "Sapphire", "Ruby"]
val = "Ruby"
print(move_to_end(gemstones, val))
