from main import create_array, set_, get_, append_, remove_, insert_


def test_set_get_():
    arr = create_array(3)
    set_(array=arr, index=0, value=1)
    set_(arr, 1, 2)
    set_(arr, 2, 3)
    assert get_(array=arr, index=0) == 1
    assert get_(arr, 1) == 2
    assert get_(arr, 2) == 3


def test_append_():
    arr = create_array(0)
    arr = append_(arr, 1)
    arr = append_(arr, 2)
    arr = append_(arr, 3)
    arr = append_(arr, 4)
    arr = append_(arr, 5)
    assert get_(arr, 0) == 1
    assert get_(arr, 1) == 2
    assert get_(arr, 2) == 3
    assert get_(arr, 3) == 4
    assert get_(arr, 4) == 5


def test_remove():
    arr = create_array(0)
    arr = append_(arr, 1)
    arr = append_(arr, 2)
    arr = append_(arr, 3)
    arr = append_(arr, 4)
    arr = append_(arr, 5)
    arr = append_(arr, 6)
    arr = append_(arr, 7)

    arr = remove_(arr, 0)
    arr = remove_(arr, 1)
    arr = remove_(arr, 2)
    arr = remove_(arr, 3)
    assert get_(arr, 0) == 2
    assert get_(arr, 1) == 4
    assert get_(arr, 2) == 6
    assert get_(arr, 3) is None


def test_insert():
    arr = create_array(0)
    arr = insert_(arr, 0, 10)
    assert get_(arr, 0) == 10
    arr = insert_(arr, 0, 1)
    assert get_(arr, 0) == 1
    arr = insert_(arr, 1, 11)
    assert get_(arr, 1) == 11
    arr = insert_(arr, 3, 11)
    assert get_(arr, 3) == 11
    arr = insert_(arr, 1, 13)
    assert get_(arr, 1) == 13
