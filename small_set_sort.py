def small_set_sort(values):
    """ sort small set """
    elements = ['< 3 months', '6 months', '1-2 years', '2-4 years', '4-8 years']
    final_list = [0] * len(elements)

    for val in values:
        if val in elements:
            final_list[elements.index(val)] = val

    final_list.remove(0)
    return final_list



if __name__=="__main__":
    values = ['4-8 years', '6 months', '< 3 months', '1-2 years']
    print(small_set_sort(values))
