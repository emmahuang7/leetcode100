题目  
---------------------------
编写一个程序，找到两个单链表相交的起始节点。   

思路:双指针
---------------------------
如果两个链表相交，那么相交点之后的长度是相同的，需要消除两个链表开头的高度差。   
指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历  
如果 pA 到了末尾，则 pA = headB 继续遍历  
如果 pB 到了末尾，则 pB = headA 继续遍历  
比较长的链表指针指向较短链表head时，长度差就消除了  
time:O(n)  
space:O(1)
 
