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
    
class Application:
    def __init__(self):
        self.__order_book = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        
        programmer_and_workload = input("programmer and workload estimate: ")
        programmer_and_workload = programmer_and_workload.split(" ")

        if len(programmer_and_workload)!=2 or not programmer_and_workload[1].isdigit():
            print("erroneous input\n")
            return

        programmer = programmer_and_workload[0]
        workload = int(programmer_and_workload[1])

        self.__order_book.add_order(description, programmer, workload)

        print("added!")

    def list_finished_tasks(self):
        finished_tasks = self.__order_book.finished_orders()

        if len(finished_tasks)==0:
            print("no finished tasks")
        
        for task in finished_tasks:
            print(task)

    def list_unfinished_tasks(self):
        unfinished_tasks = self.__order_book.unfinished_orders()

        if len(unfinished_tasks)==0:
            print("no unfinished tasks")
        
        for task in unfinished_tasks:
            print(task)
        
    def mark_as_finished(self):
        id = (input("id: "))

        if not id.isdigit() or int(id)>Task.id:
            print("erroneous input\n")
            return
        
        self.__order_book.mark_finished(int(id))
        
        print("marked as finished")

    def programmers(self):
        for programmer in self.__order_book.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")

        if programmer not in self.__order_book.programmers():
            print("erroneous input\n")
            return

        task_finished, task_unfinished, hours_done, hours_left = self.__order_book.status_of_programmer(programmer)
        print(f"tasks: finished {task_finished} not finished {task_unfinished}, hours: done {hours_done} scheduled {hours_left}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_as_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()

application = Application()
application.execute()