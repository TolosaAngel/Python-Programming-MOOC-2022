class Task:
    id = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__task_track = False
        
        Task.id += 1
        self.id = Task.id

    def mark_finished(self):
        self.__task_track = True
        
    def is_finished(self):
        return self.__task_track
    
    def __str__(self):
        task_track = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {task_track}"

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        new_task = Task(description, programmer, workload)
        self.orders.append(new_task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([order.programmer for order in self.orders]))
    
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def mark_finished(self, id: int):
        id_list = [order.id for order in self.all_orders()]

        if id not in id_list:
            raise ValueError
        else:
            for order in self.unfinished_orders():
                if id==order.id:
                    order.mark_finished()

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError
        
        list_of_finished = [order for order in self.finished_orders() if order.programmer==programmer]
        list_of_unfinished = [order for order in self.unfinished_orders() if order.programmer==programmer]

        hs_of_finished = sum([task.workload for task in list_of_finished]) 
        hs_of_unfinished =sum([task.workload for task in list_of_unfinished]) 

        return (len(list_of_finished), len(list_of_unfinished), hs_of_finished, hs_of_unfinished)
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)