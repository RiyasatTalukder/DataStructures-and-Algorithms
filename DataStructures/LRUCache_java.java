public class LRUCache_java {
    private int capacity;
    public class DLNode {
        int key;
        int value;
        DLNode pre;
        DLNode next;
    }
    public LRUCache_java(int capacity) {
        this.capacity = capacity;
    }
}