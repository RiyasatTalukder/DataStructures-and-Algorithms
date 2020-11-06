public class ClosingParenthesis {
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