class ShellSort:
    
    def sort_shell_atribute(self, arr, attribute, orden=1):
        return self.shell_sort_with_attribute(arr, attribute, orden)

    def sort_shell_number(self, arr, orden=1):
        return self.shell_sort_numbers(arr, orden)

    def shell_sort_numbers(self, arr, orden):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and ((orden == 1 and arr[j - interval] > temp) or (orden != 1 and arr[j - interval] < temp)):
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr

    def shell_sort_with_attribute(self, arr, attribute, orden):
        interval = len(arr) // 2
        while interval > 0:
            for i in range(interval, len(arr)):
                temp = arr[i]
                j = i
                while j >= interval and ((orden == 1 and getattr(arr[j - interval], attribute) > getattr(temp, attribute)) or \
                                         (orden != 1 and getattr(arr[j - interval], attribute) < getattr(temp, attribute))):
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = temp
            interval //= 2
        return arr
