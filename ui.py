# sql get characteristic as user_parameter
from characteristic import Characteristic
from user_data import UserData

class UserInterface():
    def __init__(self, session, user_id):
        self.session = session
        self.user_id = user_id
        self.display_warning()

    def process_user_input(self, parameter, characteristic_id):
        value = input('Введите значение %s:' % (parameter.name))
        is_accepted = False
        if int(value)>=int(parameter.min_value) and int(value)<=int(parameter.max_value):
            is_accepted = True
            self.session.add(UserData(self.user_id, characteristic_id, int(value)))
        # enumeration
        # elif parameter.type == 'enum' and int(value) != 0:
        #     is_accepted = True
        return is_accepted

    def init_user_input(self):
        is_data_filled = False
        user_parameters = self.session.query(Characteristic)
        current_index = 0
        while not is_data_filled:
            parameter = user_parameters[current_index]
            input_result = self.process_user_input(parameter, user_parameters.id)
            if input_result == False:
                print('Экспертная система не предназначена для таких параметров')
            else:
                current_index+=1
        self.session.commit()

    def display_exercises(self, excercies):
        print("Список упражнений:")
        for exercise in excercies:
            value = "%s - %s (%s)" % (exercise.name,
                    exercise.description, 
                    exercise.muscle_group)
            print(value)
                
    def display_warning(self):
        warnings = [
            'Вес больше 150',
            'Проблемы с позвоночником',
            'Что-то еще',
        ]
        prefix_message = 'Не используйте экспертную систему если у вас:'
        postfix_message = 'Воспользуйтесь консультацией врача'
        print(prefix_message+'\n', '\n'.join(warnings) + '\n', postfix_message)
