public class DynamicArray_java {
    public static void main(String args[]) {
        DynamicArray_java arr = new DynamicArray_java();
        for(int x = 0; x < 10; x++) {
            arr.add(x);
        }
        arr.add(10);
        System.out.println(arr.toString());
        arr.remove(0);
        System.out.println(arr.toString());
        arr.remove(1);
        System.out.println(arr.toString());
    
    }
    private int[] array = new int[10];
    private int length = 10;
    private int curr_length = 0;

    public void add(int item) {
        if(this.curr_length < this.length) {
            this.array[this.curr_length] = item;
            this.curr_length++;
        }
        else {
            this.expand();
            this.array[this.curr_length] = item;
            this.curr_length+=1;
        }
    }
    public void remove(int index) {
        if(index >= 0 && index < this.curr_length) {
            for(int x = index; x < this.curr_length-1; x++){
                this.array[x] = this.array[x+1];
            }
            this.curr_length--;
        }
        if(this.curr_length < this.length/2) {
            this.shrink();
        }
    }
    public void remove() {
        this.array[this.curr_length-1] = 0;
    }
    public String toString(){
        String array_str = "";
        for(int i = 0; i < this.curr_length; i++) {
            array_str = array_str.concat(Integer.toString(this.array[i]));
        }
        return array_str;
    }

    private void expand() {
        this.length = 2*this.length;
        int[] new_arr = new int[this.length];
        for(int i = 0; i < this.curr_length; i++) {
            new_arr[i] = this.array[i];
        }
        this.array = new_arr;
    }
    private void shrink() {
        this.length = this.length/2;
        int[] new_arr = new int[this.curr_length];
        for(int i = 0; i < this.curr_length; i++) {
            new_arr[i] = this.array[i];
        }
        this.array = new_arr;
    }
    

}
    
    