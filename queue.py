#Name: Jude
#Date: 9/19/18
#the purpose of this lab is to learn about stacks and queues together
#Collaborators: None
#On My Honor: JB

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer
    def getData(self):#returns data object
        return(self.data)
    def changeData(self, newData):#changes data to newData
        self.data = newData
    def addPoint(self, newNode):#adds newNode to the end of the pointer array
        self.pointer.append(newNode)
    def addPointAtIndex(self, newNode, index):#adds newNode to the end of the pointer array
        self.pointer[index] = newNode
    def rmPoint(self, index):#removes pointer at index in array
        if(index < len(self.pointer)):
            del self.pointer[index]
    def setPoint(self, index, node):#sets pointer at index in array
        self.pointer[index] = node
    def getNode(self, index):#returns pointer at index
        if(index < len(self.pointer)):
            return self.pointer[index]
    def pointerCount(self):
        return len(self.pointer)
    def __repr__(self):
        left = 'None'
        if self.pointer[0] != None:
            left = self.pointer[0].data
        right = 'None'
        if len(self.pointer) > 2 and self.pointer[1] != None:
            right = self.pointer[1].data
        return "{data:"+str(self.data)+", pointers:"+str(self.pointerCount())+", Left Pointer:"+str(left)+" Right Pointer:"+str(right)+"}";



class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, data):
        if self.isEmpty():
            self.top = Node(data, [None])
            self.size += 1
        else:
            newNode = Node(data, [self.top])
            self.top = newNode
            self.size += 1

    def pop(self):
        if self.isEmpty():
            pass
        else:
            tempNode = self.top
            self.top = self.top.getNode(0)
            self.size -= 1
            return tempNode.getData()

    def isEmpty(self):
        return self.top == None

    def getSize(self):
        return self.size

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.getData()


class Queue:

    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def enqueue(self, data):
        self.input.push(data)

    def dequeue(self):
        data = self.peek()
        self.output.pop()
        return data

    def peek(self):
        if (not self.output.isEmpty()):
            return self.output.peek()
        else:
            for node in range(self.input.getSize()):
                self.output.push(self.input.pop())
            return self.output.peek()

    def getSize(self):
        return self.input.getSize() + self.output.getSize()

    def isEmpty(self):
        return self.getSize == 0

if __name__ == '__main__':
        testQueue = Queue()


        print("without adding anything to the queue, the size is:")
        print(testQueue.getSize())
        print()

        print("now i'm going to peak with an empty queue, it should show that the queue is empty:")
        print(testQueue.peek())
        print()

        print("enqueueing two Nodes to queue, FIRST --> hello, LAST --> there")
        testQueue.enqueue("hello")
        testQueue.enqueue("there")
        print()

        print("now i'm going to peak, it should be 'hello':")
        print(testQueue.peek())
        print()

        print('testing getSize, should be 2:')
        print(testQueue.getSize())
        print()

        print("now i'm going to dequeue, it should say 'hello':")
        print(testQueue.dequeue())
        print()

        print("now i'm going to peek, it should be 'there':")
        print(testQueue.peek())
        print()

        print("now i'm going to dequeue again, the queue should be empty now, it should say there:")
        print(testQueue.dequeue())
        print()

        print("now i'm going to dequeue with an empty queue, nothing should happen:")
        testQueue.dequeue()
        print()
