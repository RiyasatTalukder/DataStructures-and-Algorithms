import java.util.HashMap;

public class LRUCache_java {
    /*
    The following is an implementation of a LRU Cache in jave with get and put operations.
    It utilizes a Hashmap with values inserted into a doubly linkedlist.
    This allows for efficient lookup and removal.

    Time: O(1) for both get and put operations
    Space: O(capacity)
    */
    public class DLNode {
        int key;
        int value;
        DLNode prev;
        DLNode next;
    }
    private int capacity;
    private int length;
    private DLNode head;
    private DLNode tail;

    public LRUCache_java(int capacity) {
        this.capacity = capacity;
        head = new DLNode();
        tail = new DLNode();
        
        head.next = tail;
        head.prev = null;
        tail.prev = head;
        tail.next = null;
    }

    private void addNode(DLNode node) {
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }
    
    private void removeNode(DLNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void moveToHead(DLNode node) {
        this.removeNode(node);
        this.addNode(node);
    }

    private DLNode removeTail() {
        DLNode last = tail.prev;
        this.removeNode(tail);
        return last;
    }

    private HashMap<Integer, DLNode> cache = new HashMap<Integer, DLNode>();

    public int get(int key) {
        DLNode node = this.cache.get(key);
        if(node == null) {
            return -1;
        }
        this.moveToHead(node);
        return node.value;
    }

    public void put(int key, int value) {
        DLNode node = this.cache.get(key);
        if(node == null) {
            node = new DLNode();
            node.key = key;
            node.value = value;
            if(++this.length > this.capacity) {
                DLNode lru = this.removeTail();
                this.cache.remove(lru.key);
                this.length--;
            }
            this.addNode(node);
        } else {
        node.value = value;
        this.moveToHead(node);
        }
    }
}