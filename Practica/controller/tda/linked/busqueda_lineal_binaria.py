class Busqueda_Lineal_Binaria:
    
    def busqueda_binaria_lineal_atribute(self, array, attribute, value):
        results = []
        left = 0
        right = len(array) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if getattr(array[middle], attribute) == value:
                i = middle
                while i >= left and getattr(array[i], attribute) == value:
                    results.append(array[i])
                    i -= 1
                
                i = middle + 1
                while i <= right and getattr(array[i], attribute) == value:
                    results.append(array[i])
                    i += 1
                
                return results
            
            elif getattr(array[middle], attribute) < value:
                left = middle + 1
            else:
                right = middle - 1
        
        return results
    
    def busqueda_binaria_lineal_number(self, array, value):
        results = []
        left = 0
        right = len(array) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if array[middle] == value:
                i = middle
                while i >= left and array[i] == value:
                    results.append(i)
                    i -= 1
                
                i = middle + 1
                while i <= right and array[i] == value:
                    results.append(i)
                    i += 1
                
                return results
            
            elif array[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        
        return results
