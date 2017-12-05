import sys


def test():
    print("[Step] Test")
    assert 1 == 1


def parse():
    print("[Step] Parse")
    assert 1 == 1


def deploy():
    print("[Step] Deploy")
    assert 1 == 1


def go_to_prod():
    print("[Step] Go to PROD")


if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test()
    elif sys.argv[1] == 'parse':
        parse()
    elif sys.argv[1] == 'deploy':
        deploy()
    elif sys.argv[1] == 'go_to_prod':
        go_to_prod()
