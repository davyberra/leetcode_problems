def longest_common_prefix(strs: list) -> str:
    output = ""
    prev_letter = ""
    for i, letter in enumerate(strs[0]):
        for word in strs:
            if word[i] != prev_letter and strs.index(word) > 0:
                return output
            else:
                prev_letter = word[i]
        output += letter

    return output



print(longest_common_prefix(["flower", "flow", "flight"]))
