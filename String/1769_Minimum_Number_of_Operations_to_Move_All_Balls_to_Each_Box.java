class Solution {
    
    public int[] minOperations(String boxes) {
        
        int[] operations = new int[boxes.length()];
        int ballCount = 0; // How many balls we're currently moving to the left or right, depending on which loop we are in
        int opsPerIncrement = 0; // How many operations per increment in array
        
        // Move balls to the right -->
        for(int i = 0; i < boxes.length(); i++) {
            operations[i] += opsPerIncrement;
            if(boxes.charAt(i) == '1') {
                ballCount++;
            }
            opsPerIncrement += ballCount;
            
        }
        
        ballCount = 0;
        opsPerIncrement = 0;
        
        // Move balls to the left <--
        for(int i = boxes.length() - 1; i >= 0; i--) {
            operations[i] += opsPerIncrement;
            if(boxes.charAt(i) == '1') {
                ballCount++;
            }
            opsPerIncrement += ballCount;
        }
        
        return operations;
    }
}