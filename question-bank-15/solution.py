class ExceptionProxy(Exception):
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function


def transform_exceptions(func_ls):
    results = []

    for f in func_ls:
        try:
            f()  # اجرای تابع
            # اگر بدون خطا بود:
            results.append(ExceptionProxy("ok!", f))
        except Exception as e:
            # اگر خطا داد، متن خطا و تابع رو ذخیره کن
            results.append(ExceptionProxy(str(e), f))

    return results
