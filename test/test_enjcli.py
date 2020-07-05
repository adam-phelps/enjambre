import subprocess

def test_add_robot():
    cmd = ["python","src/enjcli.py","--add-robot","TestUnit-Robot"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    assert 'TestUnit-Robot' in str(result.stdout)

def test_list_robot():
    cmd = ["python","src/enjcli.py","--list-robot","all"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    assert 'all' in str(result.stdout)
 