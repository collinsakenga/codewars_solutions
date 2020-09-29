def norm_index_test(seq, ind):
    return seq[ind % len(seq)] if seq else None
