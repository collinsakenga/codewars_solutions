def search_substr(full_text, search_text, allow_overlap=True):
    if not full_text or not search_text:
        return 0
    if not allow_overlap:
        return full_text.count(search_text)
    count = 0
    for i in range(len(full_text)-len(search_text)+1):
        if full_text[i:i+len(search_text)] == search_text:
            count += 1
    return count
