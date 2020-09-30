from PyQt5.QtCore import QThread, pyqtSignal, QObject


class EmailThread(QThread):
    finishSignal = pyqtSignal(bool)

    def __init__(self, func, args):
        super(EmailThread, self).__init__()
        self.func = func
        self.args = args
        self.ret = None

    def run(self):
        self.ret = self.func(*self.args)
        self.finishSignal.emit(self.ret)


class outEmailThread(QThread):
    finishSignal = pyqtSignal(int, int)

    def __init__(self, func, args):
        super(outEmailThread, self).__init__()
        self.func = func
        self.args = args
        self.suc = 0
        self.fail = 0

    def run(self):
        self.suc, self.fail = self.func(*self.args)
        self.finishSignal.emit(self.suc, self.fail)


# class EmailObject(QObject):
#     finishSignal = pyqtSignal(bool)
#
#     def __init__(self, func, args):
#         super(EmailObject, self).__init__()
#         self.func = func
#         self.args = args
#         self.ret = None
#
#     def email(self):
#         print("Hi")
#         self.ret = self.func(*self.args)
#         print("Hello")
#         self.finishSignal.emit(self.ret)
