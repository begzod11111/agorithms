class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }

    setNextNode(node) {
        if (node instanceof Node || node === null) {
            this.next = node;
        } else {
            throw new Error('Next node must be a member of the Node class');
        }
    }
}


class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

}