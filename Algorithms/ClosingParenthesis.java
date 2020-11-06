public class ClosingParenthesis {
    /*
    Given a string with parenthesis, the algorothm finds the closing parenthesis
    of an opening parenthesis at index i. 

    Time: O(n)
    Space: O(1)
    */
    public static void main(String args[]) {
        String test = "This author (unnamed (anonymous) because he is bashful (shy (kinda))) loves brackets.";
        ClosingParenthesis k = new ClosingParenthesis();
        System.out.println(Integer.toString(k.findClosingParenthesis(test.toCharArray(), 12)));

    }
    public int findClosingParenthesis(char []s, int i) {
        int counter = 1;
        while(counter > 0 && i < s.length) {
            if(s[++i] == '(') {
                counter +=1;
            } else if (s[i] == ')') {
                counter -=1;
            }
        }
        return i;
    }
}