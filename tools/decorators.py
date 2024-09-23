from project.tools.logging import Logger


def exception_handling(function):
    def inner(self, *args, **kwargs):
        try:
            output = function(self, *args, **kwargs)
            if not "find" in function.__name__ :
                Logger.info(f"{function.__qualname__}{args} [RETURNED] : {output}")
            else:
                Logger.info(f"{function.__qualname__}{args}")
            return output
        except Exception as e:
            # e.with_traceback()
            Logger.error(f"{function.__qualname__}{args} [RAISED EXCEPTION] : {e}")
            return False, str(e)
    return inner

