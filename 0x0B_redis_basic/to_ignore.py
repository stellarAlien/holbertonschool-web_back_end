def replay(fn):
        '''display calls of a particular function'''
        @wraps(fn)
        def replayer(*args):
            count = count_calls(fn)
            print('Cache.{:} was called {:} times:'.format(fn.__qualname__, count))
            inputs = args[0]._redis.get(f'{fn.__qualname__}:inputs')
            outputs = args[0]._redis.get(f'{fn.__qualname__}:outputs')
            for i, o in zip(inputs, outputs):
                print('Cache.store(*({:},)) -> {:}'.format(i, o))
        return replayer