class Node:
    def  __init__(self, data):
         self.data = data 
         self.next = None 

head = None

def insertNodeAtTheBeginning(data):
    global head 
    newNode = Node(data)
    
    if(head == None):
        head  = newNode 
    else:
        newNode.next = head
        head = newNode
 
def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next

def insertNodeAtTheEnd(data):
   global head
   newNode = Node(data)
    
   if(head == None):
        head = newNode
   else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode
        
def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        current = head.next
        prev = head
        while(prev.data != node):
            prev = current
            current = current.next
            
            if(prev == None):
                print('The node does not exist')
                return
            
    newNode.next = current
    prev.next = newNode
    
insertNodeAtTheBeginning('will of the wind by jhino ')
insertNodeAtTheBeginning('sparkle by radwimps')
insertNodeAtTheBeginning('if i were a boy by beyonce')

insertNodeAtTheEnd('ngiti by juans')
insertNodeAtTheEnd('halik sa hangin by kz tandingan')

insertNodeAfterGivenNode('kalapastangan by fitterkarma', 'ngiti by juans')
insertNodeAfterGivenNode('Ill be by edwin mcCain', 'kalapastangan by fitterkarma')

traverseLinkedList()
