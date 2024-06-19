class MergeSort:
            
    def sort_merge_atribute(self, arr, attribute=None, orden=1):
            return self.merge_sort_with_attribute(arr, attribute, orden)

    def sort_merge_number(self, arr, orden=1):
            return self.merge_sort_numbers(arr, orden)

    def merge_sort_numbers(self, arr, orden):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort_numbers(arr[:mid], orden)
        right = self.merge_sort_numbers(arr[mid:], orden)
        
        result = []
        while left and right:
            if (orden == 1 and left[0] < right[0]) or (orden != 1 and left[0] > right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        result += left
        result += right
        
        return result

    def merge_sort_with_attribute(self, arr, attribute, orden):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = self.merge_sort_with_attribute(arr[:mid], attribute, orden)
        right = self.merge_sort_with_attribute(arr[mid:], attribute, orden)
        
        result = []
        while left and right:
            if (orden == 1 and getattr(left[0], attribute) < getattr(right[0], attribute)) or \
               (orden != 1 and getattr(left[0], attribute) > getattr(right[0], attribute)):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        result += left
        result += right
        
        return result
