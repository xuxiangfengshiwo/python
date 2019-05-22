

def keyword_args(*args, **kwargs):
    print('args type',type(args),'-'*33)
    for i in args:
        print(i)

    print('kargs type',type(kwargs),'-'*33)
    for key in kwargs:
        print(key, ':',kwargs[key])

if __name__ == '__main__':
    keyword_args('hello','xxf',age = 28)