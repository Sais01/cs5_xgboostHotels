import numpy as np
import datetime

class Formatter:
    """
    Classe para formatar os dados de entrada para o modelo de machine learning.

    :param data: dados de entrada
    :type data: dict

    :return: array com os valores numéricos
    """
    
    def __init__(self, data):
        self.data = data

    def map_categorical_values(self):
        """
        Mapear os valores categóricos para valores numéricos.

        :return: array com os valores numéricos
        """
        
        category_mappings = {
            "type_of_meal_plan": {
                "Meal Plan 1": 0,
                "Meal Plan 2": 0,
                "Meal Plan 3": 0,
                "Not Selected": 0,
            },
            "room_type_reserved": {
                "Room_Type 1": 0,
                "Room_Type 2": 0,
                "Room_Type 3": 0,
                "Room_Type 4": 0,
                "Room_Type 5": 0,
                "Room_Type 6": 0,
                "Room_Type 7": 0,
            },
            "market_segment_type": {
                "Aviation": 0,
                "Complementary": 0,
                "Corporate": 0,
                "Offline": 0,
                "Online": 0,
            },
            "booking_status": {
                "Canceled": 0,
                "Not Canceled": 0,
            }
        }

        result = []

        for key in self.data:
            if key in category_mappings:
                mapping = category_mappings[key]
                if self.data[key] in mapping:
                    mapping[self.data[key]] = 1
                result.extend(list(mapping.values()))
            else:
                result.append(self.data[key])

        return np.array(result)


class Validator:
    """
    Classe para validar a data de entrada.

    :param data: data de entrada
    """

    def __init__(self, data):
        self.data = data

    def validate_data(self):
        """
        Verificar se a data de chegada é maior que a data atual.

        :return: boolean com o resultado da verificação
        """
        
        # pega a data atual
        atual_date = datetime.datetime.now().strftime('%Y-%m-%d')

        year = self.data['arrival_year']
        month = '0' + str(self.data['arrival_month']) if '0' not in str(self.data['arrival_month']) else str(self.data['arrival_month'])
        day = '0' + str(self.data['arrival_date']) if '0' not in str(self.data['arrival_date']) else str(self.data['arrival_date'])

        complete_date = f'{year}-{month}-{day}'

        # verificar se a data de chegada é maior que a data atual
        if complete_date < atual_date:
            return False
        
        return True