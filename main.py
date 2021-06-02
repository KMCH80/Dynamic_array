def create_array(num):
    array = {'len': 0, 'array': [None] * num}
    return array


def set_(array, index, value):
    array['array'][index] = value


def get_(array, index):
    return array['array'][index]


def append_(array, value):
    capacity = len(array['array'])
    if capacity == array['len']:
        new_array = create_array(max(capacity, 1) * 2)
        for index, item in enumerate(array['array']):
            new_array['array'][index] = item
        new_array['array'][array['len']] = value
        new_array['len'] = array['len'] + 1
        return new_array
    array['array'][array['len']] = value
    array['len'] += 1
    return array


def remove_(array, remove_index):
    for index in range(array['len']):
        if index >= remove_index:
            if index != array['len'] - 1:
                array['array'][index] = array['array'][index + 1]
            else:
                array['array'][index] = None
    array['len'] -= 1
    return array


def insert_(array, insert_index, value):
    if len(array['array']) == 0:
        array = append_(array, value)
        return array
    capacity = len(array['array'])
    if capacity == array['len']:
        new_array = create_array(max(capacity, 1) * 2 + 2)
        for index in range(array['len']):
            if index == insert_index:
                new_array['array'][index] = value
            if index >= insert_index:
                new_arr_index = index + 1
            else:
                new_arr_index = index
            new_array['array'][new_arr_index] = array['array'][index]
        new_array['len'] = array['len'] + 1
        return new_array
    else:
        for index in range(array['len'] + 1):
            if index == insert_index:
                shift_value = array['array'][index]
                array['array'][index] = value
                continue
            if index > insert_index:
                array['array'][index] = shift_value
                if index != array['len']:
                    shift_value = array['array'][index + 1]
        array['len'] += 1
        return array
