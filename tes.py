# """
# web scrapping ke csv 
# buat jaadi dictionary
# sorting 



# """
# arr = {}
# arr["pacar petra"] = 10
# arr["pacar alfandi"] = 5
# arr["pacar albert"] = 20
# arr["pacar alvern"] = 15

# print(len(arr))

# list1 = []
# list2 = []
# for i in arr: 
#     list1.append(arr[i])
#     list2.append(i)

# print(list1, list2)


# # def dict_sort (key,value):
# #         for check in range(len(value)):
# #             for order in range(len(value)-1):
# #                 if value[order] < value[order+1]:
# #                     temp = value[order]
# #                     value[order] = value[order+1]
# #                     value[order+1] = temp
# #                     temp2 = key[order]
# #                     key[order] = key[order+1]
# #                     key[order+1] = temp2
# #                 else:
# #                     pass
# #         return key,value


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr 
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x > pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x < pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort(list1))


import threading
class Monitor:
    def __init__(self):
        self.mutex = threading.Lock()
        # Mutex for controlling access to the shared resource
        self.condition = threading.Condition(self.mutex)
        # Condition variable for synchronization
        self.shared_resource = None
    def write_data(self, data):
        with self.mutex:
        # Critical section
            while self.shared_resource is not None:
                self.condition.wait() # Wait until the resource is available
            self.shared_resource = data
            self.condition.notify() #
    def read_data(self):
        with self.mutex:
        # Critical section
            while self.shared_resource is None:
                self.condition.wait() # Wait until there is data to read
            data = self.shared_resource
            self.shared_resource = None
            self.condition.notify()
        # Notify waiting threads that the resource is available for writing
        return data
def producer(monitor):
    for i in range(1, 6):
        print(f"Producing data {i}")
        monitor.write_data(f"Data {i}")
def consumer(monitor):
    for i in range(1, 6):
        data = monitor.read_data()
        print(f"Consuming {data}")
if __name__ == "__main__":
    monitor = Monitor()
    producer_thread = threading.Thread(target=producer, args=(monitor,))
    consumer_thread = threading.Thread(target=consumer, args=(monitor,))
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()