from bot import dp

def handler(lfunc=lambda m: True, commands=None,regexp=None, content_types=None, state=None, run_task=None):
    
    def decorator_func(func):
        
        async def wrapper_func(wrapper):
            
            await func(wrapper)
        
        
        
        dp.register_message_handler(
            wrapper_func,
            lfunc,
            commands=commands,
            regexp=regexp, 
            content_types=content_types, 
            state=state, 
            run_task=run_task
            )
        
        return wrapper_func
    
    return decorator_func

