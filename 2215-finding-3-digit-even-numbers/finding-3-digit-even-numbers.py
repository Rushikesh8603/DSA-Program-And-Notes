class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        result_set = set()      
        used_indices = set()  
        
        def build_number(current_combo):

            if len(current_combo) == 3:
                if current_combo[0] != 0 and current_combo[-1] % 2 == 0:
                    number = current_combo[0] * 100 + current_combo[1] * 10 + current_combo[2]
                    result_set.add(number)         
                return 
        
            for i in range(len(digits)):
                
                if i not in used_indices:
                    used_indices.add(i)               
                    current_combo.append(digits[i])   
                    build_number(current_combo)                               
                    current_combo.pop()                 
                    used_indices.remove(i)   
            return       
                    
        build_number([])
        return sorted(list(result_set))



