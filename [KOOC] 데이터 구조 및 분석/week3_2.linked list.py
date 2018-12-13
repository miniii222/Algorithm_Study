# -*- coding: utf-8 -*-

class Node :
    nodeNext = "" #variable to reference the next node
    objValue = "" #varaibel to hold a value object
    
    blHead = False #head node인가?
    blTail = False #tail node인가?
    
    def __init__(self, objValue='', nodeNext='', blHead=False, blTail=False) :
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.blHead = blHead
        self.blTail = blTail
        
    def getValue(self) : #value를 가져와서
        return self.objValue
    def setValue(self, objValue) : #저장
        self.objValue = objValue
    def getNext(self) : #다음 reference를 가져와서
        return self.nodeNext
    def setNext(self, nodeNext) : #정의
        self.nodeNext = nodeNext
    def isHead(self) :
        return self.blHead
    def isTail(self) :
        return self.blTail
    
#%%
class SinglyLinkedList :
    nodeHead = ''
    nodeTail = ''
    size = 0
    
    def __init__(self) :
        self.nodeTail = Node(blTail = True)
        self.nodeHead = Node(blHead = True, nodeNext=self.nodeTail)
        
    #linkedlist에서 node 추가
    def insertAt(self, objInsert, idxInsert) :
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1) #넣으려고 하는 곳의 바로 직전
        nodeNext = nodePrev.getNext()
        
        nodePrev.setNext(nodeNew) #전 단계의 노드는 추가하는 노드와 연결
        nodeNew.setNext(nodeNext) #추가하는 노드와 다음 단계의 노드 연결
        self.size = self.size + 1
        
    #linkedlist 에서 node 제거
    def removeAt(self, idxRemove) :
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        
        nodePrev.setNext(nodeNext)
        self.size = self.size - 1
        return nodeRemove.getValue()
    
    def get(self, idxRetrieve) :
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1) :
            nodeReturn = nodeReturn.getNext()
            
        return nodeReturn
    
    def printStatus(self) :
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False :
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue())
    #linkedlist의 node개수 가져오기
    def getSize(self) :
        return self.size        
#%%
list1 = SinglyLinkedList()
list1.insertAt('a',0)
list1.insertAt('b',1)
list1.insertAt('c',2)
list1.insertAt('d',3)
list1.insertAt('e',4)
list1.insertAt('f',5)
list1.printStatus()

list1.insertAt('c',2)
list1.printStatus()

list1.removeAt(2)
list1.printStatus()
