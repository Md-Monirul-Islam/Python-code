class Queue:
    def __init__(self,contents):
        self._hidden_list = list(contents)

    def push(self,value):
        self._hidden_list.insert(0,value)

    def pop(self):
        return self._hidden_list.pop(-1)
    def _show_list(self):
        return self._hidden_list

queue = Queue([1,2,3])
print(queue._hidden_list)

queue.push(0)
print(queue._hidden_list)

queue.pop()
print(queue._hidden_list)

print(queue._show_list())