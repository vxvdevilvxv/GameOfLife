import time


def candy_wrapper(func):
    def wrap():
        temp = func()
        print('------------')
        print(temp)
        print('------------')

    return wrap


def stop_watch(func):
    def wrap():
        start = time.time()
        func()
        finish = time.time()
        print(finish - start)

    return wrap


@stop_watch
@candy_wrapper
def ask():
    return input("Input phrase: ")


ask()
