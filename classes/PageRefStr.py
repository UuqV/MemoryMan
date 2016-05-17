def page_ref_list(path):
    ref_str = []
    with open(path) as f:
        for line in f:
            for num in line.split(' '):
                ref_str.append(int(num))
    return ref_str
