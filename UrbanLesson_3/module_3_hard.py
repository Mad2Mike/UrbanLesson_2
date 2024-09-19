data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    struct_list = []
    list_for_slice = [data_structure]
    while list_for_slice:
        data_str_pop = list_for_slice.pop()
        if isinstance(data_str_pop, int):
            struct_list.append(data_str_pop)
        elif isinstance(data_str_pop, str):
            struct_list.append(len(data_str_pop))
        elif isinstance(data_str_pop, dict):
            for key in data_str_pop.keys():
                list_for_slice.append(key)
            for value in data_str_pop.values():
                list_for_slice.append(value)
        elif isinstance(data_str_pop, (list, tuple, set, dict)):
                list_for_slice.extend(data_str_pop)
        else:
            print("Неизвестный элемент! Проверьте состав передаваемой структуры!")

    return sum(struct_list)

result = calculate_structure_sum(data_structure)
print(result)


# У меня еще была функция с рекурсией, но ее нужно было вызывать в другой функции, поэтому не подходит по условия (полная реализация в рамках одной функции) :(
# def action_for_type(index_type):
#     if isinstance(index_type,int):
#         struct_list.append(index_type)
#     elif isinstance(index_type,str):
#         struct_list.append(len(index_type))
#     elif isinstance(index_type, dict):
#         for key in index_type.keys():
#             action_for_type(key)
#         for value in index_type.values():
#             action_for_type(value)
#     elif isinstance(index_type, (list, tuple, set, dict)):
#         for element in index_type:
#             action_for_type(element)
#
#     else:
#         print("Неизвестный элемент! Проверьте состав передаваемой структуры!")


