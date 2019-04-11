import java.util.*;
class Node{
	int infor;
	Node next;
	public Node(){}
	public Node(int el){
		this.infor=el;
	}
	public Node(int el,Node n){
		this.infor=el;
		this.next=n;
	}
}

class SLL{
	static Node head,tail;
	public SLL(){
		head=tail=null;

	}
	public boolean isEmpty(){
		return head==null;
	}
	public void addFirst(int el){
		Node p = new Node(el);
		if (isEmpty()) head = p;
		else {
			p.next=head; //lien ket
			head=p;
		} 
	}
	public void addLast(int el){
		Node p = new Node(el);
		if (isEmpty()) head=tail=p;
		else {
			p.next = head;
			
		}
	}
	public void addPos(int pos,int el){
		Node tmp  = head;
		int count=0;
		if (pos < 0 || pos > size()){
			return;
		} else {
			if (pos == 0){
				addFirst(el);
			} else
		
		{
		while (count < pos-1){
			tmp=tmp.next;
			count++;
			}
		Node p= new Node(el);
		p.next= tmp.next;
		tmp.next=p;
		}
	}
	}
	public void removeFirst(){
		if (!isEmpty()){
			head = head.next;
		}
	}
	public void removeAll(){
		if(!isEmpty()){
			head=tail=null;
		}
	}
	public void removeLast(){
		if (!isEmpty()){
			Node tmp=head; 
			int count=0;
			while (count< size()-2){
				tmp=tmp.next;
				count++;
			}
			tail=tmp;
			tmp.next=null;
		}
	}
	public void removePos(int pos){
		if (pos>=0 && pos <=size()-1){
			if (pos==0) {removeFirst();}
				else {
						Node tmp = head;
						int count=0;
						Node pre=null;
						while(count < pos){
							pre=tmp;
							tmp=tmp.next;
							count++;
						}
						pre.next=tmp.next;
	}
	}
}

	public int size(){
		int count=0;
		Node tmp=head;
		while(tmp!=null){
			tmp=tmp.next;
			count++;
		}
		return count;
	}
	
	public void printAll(){
		int count=0;
		Node tmp = head;
		while ( tmp != null){
			System.out.print(tmp.infor +" ");
			tmp=tmp.next;
		}
    }
}
public class unit8{
public static void main(String[] args) {
	SLL sll = new SLL();
	sll.addFirst(6);
	sll.addFirst(7);
	sll.addFirst(8);
	sll.addLast(9);
	sll.addLast(10);
	sll.addPos(1,2);
	sll.removePos(1);
	sll.printAll();
	System.out.println();
	}
}
