def compare(a,b):
    comm = set(a).intersection(set(b))
    num_comm = len(comm)

    uniq = set(a).union(set(b))
    num_uniq = len(uniq)

    return (num_comm / num_uniq) * 100

