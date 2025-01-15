class Class:
    def __init__(self):
      self.msg_1 = 'message 1'
      print(self.msg_1)

class NewClass(Class):
    def __init__(self):
      super().__init__()
      self.msg_1 = 'message 2'
      print(self.msg_1)