class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
class linkedlist:
   def __init__(self): #head
      self.head=None
      
   def printlist(self):
      temp=self.head
      while(temp):
         print (temp.data)
         temp=temp.next
         
   def reverse(self):
      prev=None
      current=self.head
      while(current is not None):
         next=current.next
         current.next=prev
         prev=current
         current=next
      self.head=prev
      
   def push(self,new_data):
      new_node=Node(new_data)
      new_node.next=self.head
      self.head=new_node
      
n=int(input("enter the number of elements"))
llist=linkedlist()
print("enter the elements")
for i in range(0,n):
   l=int(input())
   llist.push(l)
   

llist.reverse()
print ("reversed linkedlist is")
llist.printlist()


