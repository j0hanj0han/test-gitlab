from mypypipackage.subfolder1.subfile1 import hello_world


def test_hello_world():
    # given
    # when
    result = hello_world()
    # then
    assert result == 'this is hello from subfile 1'
