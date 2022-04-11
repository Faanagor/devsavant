def read_file(path_playerlist):
    file = open(path_playerlist, 'r')
    line = file.readlines()
    cont_line = 0
    
    while (cont_line < len(line)):
        cont_line += 1
    #print(type(line))
    file.close()
    return line

def filter_h_in(playerlist_json):
    list_h_in = []
    for i in playerlist_json:
        if '"h_in":' in i:
            string = i.replace('"h_in": "',"")
            string_number = string.replace('",', '')
            string_to_int = int(string_number)
            list_h_in.append(string_to_int)
    #print(list_h_in)
    return list_h_in

def calculate_pairs_h(n, list_h_in):
    list_pair = []
    set_h_in = set(list_h_in)
    list_set = list(set_h_in)
    midle_n = int(n/2)
    for i in list_set:
        if midle_n < i:
            list_less = 
            list_plus =
            
            
        
    #     pass
    # else:
    #     pass
    print(list_set)
    return list_pair
    pass

def search_key_full_name(dict_playerlist, result_h_in):
    pass




n = 139

path_playerlist = "playerlist.txt"
playerlist_json = read_file(path_playerlist)
list_h_in = filter_h_in(playerlist_json)
list_pair = calculate_pairs_h(n, list_h_in)
    

'''
1. leo archivo +


4. Pasar value de "h_in" a list_h_in+
5. Funcion compare de lista con n
6. Tomar los resultados, y buscar las key de name, fullname en el diccionario
7. Crear list_full_name
8. Return list_full_name
'''

    
