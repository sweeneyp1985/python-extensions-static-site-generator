_callbacks = {}

def register(hook, order=0):
   def  register_callback(func)
        _callbacks.setdeafult(hook,{}).setdefault(order, []).append(func)
        return func

  return register_callback
