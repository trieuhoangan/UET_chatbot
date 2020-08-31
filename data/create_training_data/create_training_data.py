import pandas as pd 

class LoadData:
    def __init__(self):
        self.data = {}
        self.entity = {}
        # self.load_instinc_data(filename)
        self.load_entity("entity_list.csv")
    def load_instinc_data(self,filename):
        df = pd.read_csv(filename,delimiter=',',usecols=['intent','q','noisy','a'])
        data_intances =df[['intent', 'q']].values
        for data in data_intances:

            if data[0] not in self.data.keys():
                self.data[data[0]] = [data[1]]
            else:
                if data[1] not in self.data[data[0]]:
                    self.data[data[0]].append(data[1])
    def load_instinc_data_custom(self,filename,intent_col_num:int,text_col_num:int):
        df = pd.read_csv(filename,delimiter=',',usecols=['intent','q','noisy','a'])
        data_intances =df.values
        for data in data_intances:

            if data[intent_col_num] not in self.data.keys():
                self.data[data[0]] = [data[text_col_num]]
            else:
                if data[text_col_num] not in self.data[data[intent_col_num]]:
                    self.data[data[intent_col_num]].append(data[text_col_num].lower())
    def print_training_data(self,filename):
        ##TODO 
        # add instinct path
        with open(filename,'w',encoding='utf-8') as fout:
            list_intent = self.data.keys()
            for intent in list_intent:
                data = self.data[intent]
                fout.write("## intent:{}\n".format(intent))
                for line in data:
                    fout.write("- {}\n".format(self.entity_detection(line)))
    def entity_detection(self,inmessage):
        ##TODO
        # specify entity in the sentence
        list_entity = self.entity.keys()
        for entity in list_entity:
            list_value = self.entity[entity].keys()
            for value in list_value:
                list_antonym = self.entity[entity][value]
                for antonym in list_antonym:
                    if antonym in inmessage:
                        
                        first_pos = inmessage.find(antonym)
                        if first_pos+len(antonym)== len(inmessage) or inmessage[first_pos+len(antonym)] ==' ':
                            inmessage = inmessage[:first_pos] + '[' + antonym + ']({})'.format(value) + inmessage[(first_pos+len(antonym)):]
        return inmessage
    def load_entity(self,filename):
        df = pd.read_csv(filename,delimiter=',',usecols=['entity','value','antonym'])
        entity = df["entity"].values
        value = df["value"].values
        antonym = df["antonym"].values
        number_entity = len(entity)
        for i in range(0,number_entity):
            list_entity = self.entity.keys()
            if entity[i] not in list_entity:
                self.entity[entity[i]] = {}
            if value[i] not in self.entity[entity[i]].keys():
                self.entity[entity[i]][value[i]] = []
                antonyms = antonym[i].split(',')
                for sing_antonym in antonyms:
                    self.entity[entity[i]][value[i]].append(sing_antonym.lower())
        print(self.entity)


if __name__ == "__main__":
    ld = LoadData()
    ld.load_instinc_data_custom("greeting_end.csv",0,2)
    ld.load_instinc_data_custom("ask_intent_data.csv",0,1)
    ld.print_training_data('t.md')
    