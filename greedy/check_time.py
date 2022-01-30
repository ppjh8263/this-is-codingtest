import time

def check_time(origin_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        
        result = origin_fn(*args, **kwargs)
        
        run_time = time.time() - start_time
        
        print(f"Function : {origin_fn.__name__} // Running Time: {run_time:.5f} sec")
        return result
    return wrapper_fn