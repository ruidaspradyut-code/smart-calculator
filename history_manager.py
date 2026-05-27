import json

class HistoryManager:
    def __init__(self,history_file='history.json'):
        self.history_file= history_file

        def save(self,expression,result):
            record = f"{expression} = {result}"
            try:
                with open(self.history_file,'r') as file:
                    history = json.load(file)
            except:
                history = {"history":[]}
            
            history["history"].append(record)

            with open(self.history_file,'w') as file:
                json.dump(history,file,indent=4)

        def show_history(self):

            try:
                with open(self.history_file,'r') as file:
                    history = json.load(file)

                for item in history["History"]:
                    print(item)
                
            except:
                print("No History Found")

        def one_record(self,index):
            try:
                with open(self.history_file,'r') as file:
                    history = json.load(file)
                index = index-1
                if 0<= index < len(history["history"]):
                    removed = history["history"].pop(index)

                    with open(self.history_file,'w') as file:
                        json.dump(history,file,indent=4)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid syntax!")
            
            except:
                print("NO HISTORY FOUND")
        
        def clear_history(self):
            history = {"history":[]}
            with open(self.history_file,'w') as file:
                json.dump(history,file,indent=4)
            print("all history cleared")