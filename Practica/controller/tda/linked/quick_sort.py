
class QuickSort:
    
    def sort_quick_atribute(self, arr, attribute, orden=1):
            return self.quick_sort_with_attribute(arr, attribute, orden)

    def sort_quick_number(self, arr, orden=1):
            return self.quick_sort_numbers(arr, orden)

    def quick_sort_numbers(self, arr, orden):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if (orden == 1 and x < pivot) or (orden != 1 and x > pivot)]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if (orden == 1 and x > pivot) or (orden != 1 and x < pivot)]
        return self.quick_sort_numbers(left, orden) + middle + self.quick_sort_numbers(right, orden)
    
    def quick_sort_with_attribute(self, arr, attribute, orden):
        if len(arr) <= 1:
            return arr
        pivot = getattr(arr[len(arr) // 2], attribute)
        left = [x for x in arr if (orden == 1 and getattr(x, attribute) < pivot) or (orden != 1 and getattr(x, attribute) > pivot)]
        middle = [x for x in arr if getattr(x, attribute) == pivot]
        right = [x for x in arr if (orden == 1 and getattr(x, attribute) > pivot) or (orden != 1 and getattr(x, attribute) < pivot)]
        return self.quick_sort_with_attribute(left, attribute, orden) + middle + self.quick_sort_with_attribute(right, attribute, orden)
