public class Base10tob {
    /*
    Algorithm to covert a base 10 number to a base b number. 
    The algorithm assumes the input number will not produce 
    a cycle ane will terminate to 0.

    Time: O(logn)
    Space: O(1)
    */
    public static void main(String[] args) {
        Base10tob test = new Base10tob();
        System.out.println(test.convert(8, 3289));
    }
    String convert(int b, int x){
        if(x == 0) {
            return "";
        } 
        return convert(b, x/b)+Integer.toString(x%b);
    }

}