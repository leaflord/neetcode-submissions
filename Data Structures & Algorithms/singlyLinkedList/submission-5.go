type LinkedList struct {
	head *Node
}

type Node struct {
	data int
	next *Node
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (ll *LinkedList) Get(index int) int {
	out := ll.at(index)
	if out == nil {
		return -1
	}
	return out.data
}

func (ll *LinkedList) InsertHead(val int) {
	oldNode := ll.head
	ll.head = &Node{data: val, next: oldNode}
}

func (ll *LinkedList) InsertTail(val int) {
	tail := &Node{data: val, next: nil}
	curr := ll.head
	if curr == nil {
		ll.head = tail
	} else {
		for curr.next != nil {
			curr = curr.next
		}
		curr.next = tail
	}

}

func (ll *LinkedList) Remove(index int) bool {
	if index == 0 {
		if ll.head != nil {
			ll.head = ll.head.next
			return true
		} else {
			return false
		}
	} else if node := ll.at(index - 1); node != nil && node.next != nil {
		node.next = node.next.next
		return true
	}
	return false

}

func (ll *LinkedList) GetValues() []int {
	out := make([]int, 0)
	for curr := ll.head; curr != nil; curr = curr.next {
		out = append(out, curr.data)
	}
	return out
}

func (ll *LinkedList) at(index int) *Node {
	curr := ll.head
	i := 0
	for i < index && curr != nil {
		curr = curr.next
		i++
	}
	return curr
}
