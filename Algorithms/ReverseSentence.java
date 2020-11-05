public class ReverseSentence {
    public static void main(String args[]) {
        String test = "   i like programming   ";
        ReverseSentence k = new ReverseSentence();
        System.out.println(k.reverseSentence(test));

    }
    public void reverse(char []s, int start, int end) {
        char temp;
        while(end > start) {
            temp = s[start];
            s[start++] = s[end];
            s[end--] = temp;
        }
    }
    String cleanSpaces(char[] a, int n) {
        int i = 0, j = 0;
        while (j < n) {
          while (j < n && a[j] == ' ') j++;             
          while (j < n && a[j] != ' ') a[i++] = a[j++]; 
          while (j < n && a[j] == ' ') j++;            
          if (j < n) a[i++] = ' ';                      
        }
      
        return new String(a).substring(0, i);
    }

    public String reverseSentence(String s) {
        char []characters = s.toCharArray();
        int start = 0;
        for(int end = 0; end < characters.length; end++) {
            if(characters[end] == ' ') {
                //reverse individual words
                reverse(characters, start, end-1);
                start = end+1;
            }
        }
        //reverse last word
        reverse(characters, start, characters.length-1);
        //reverse whole string
        reverse(characters, 0, characters.length-1);

        //clean up spaces
        return cleanSpaces(characters, characters.length);

    }
}