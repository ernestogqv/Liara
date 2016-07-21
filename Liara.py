# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:30:38 2016

@author: ErnestoGabriel
"""

print("Quieres abrir desde la ruta predeterminada? (escriba si/no)")
ruta_answer = raw_input("->").lower().strip()
while ruta_answer != "si" and ruta_answer != "no":
    print("Por favor, vuelva a intentarlo, escriba si o no.")
    ruta_answer = raw_input("->").lower().strip()
if ruta_answer == "si":
    with open("E:/Ernesto/Python/Liara (inteligencia artificial)/DATA/predeterminated_route", "r") as predeterminated_route:
        route_process = predeterminated_route.readlines()
        for alpha_route in route_process:
            route = alpha_route
if ruta_answer == "no":
    print("Por favor escriba la ruta donde se encuentra la carpeta del programa. No olvide usar el signo / para separar las carpetas o directorios, y escribalo todo junto.")
    route = raw_input().strip()
    print("Gracias!")
    

with open(route + "/Liara (inteligencia artificial)/DATA/name", "r") as file_name:
        name_1 = file_name.readlines()
        for i in name_1:
            name_readed = i
print("Hola " + str(name_readed) + "!")
answer = "Hola"
while answer != "adios":

    with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "r") as file_recordatory:
        recordatory_1 = file_recordatory.readlines()
        for i2 in recordatory_1:
            recordatory_readed = i2
    answer = raw_input().lower().strip()
    interpretar = answer.split(" ")
    input_length = len(interpretar)
    with open(route + "/Liara (inteligencia artificial)/DATA/memory", "r") as file_memory_read:
        memory_1 = file_memory_read.readlines()
        for i3 in memory_1:
            memory_readed = i3
        memory_readed_splited = memory_readed.split(" ")
    with open(route + "/Liara (inteligencia artificial)/DATA/memory", "w") as file_memory_overwrite:
        file_memory_overwrite.write("nothing")
    with open(route + "/Liara (inteligencia artificial)/DATA/activated_syntax", "r") as activated_syntax_read:
        act_syn_1 = activated_syntax_read.readlines()
        for i6 in act_syn_1:
            activated_syntax_readed = i6
    with open(route + "/Liara (inteligencia artificial)/DATA/activated_syntax", "w") as overwrite_activated_syntax:
         overwrite_activated_syntax.write("nothing")
    with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "r") as number_of_recordatories:
        num_of_rec = number_of_recordatories.readlines()
        for i11 in num_of_rec:
            num_of_rec_ready = i11 
            
    dont_know_condition = "yes"            
            
            
    if interpretar[0] == "hola" or interpretar[0] == "hola!":
        print("Hola! Como estas?")
        dont_know_condition = "no"
    if memory_readed_splited[0] == "hola":
        if interpretar[0] == "bien":
            print("Me alegro de que estes bien " + str(name_readed) + "!")
            dont_know_condition = "no"
        elif interpretar[0] == "mal":
            with open(route + "/Liara (inteligencia artificial)/DATA/activated_syntax", "w") as write_module_hola:
                write_module_hola.write("answer_mal")
            print("Oh que mal, lo lamento, pero por que te sientes mal?")
            dont_know_condition = "no"
        elif interpretar[0] == "muy":
            a = 0
            while interpretar[a] == "muy":
                a += 1
            if interpretar[a] == "bien":
                print("Me alegro de que te sientas tan bien " + str(name_readed) + "!")
                dont_know_condition = "no"
            elif interpretar[a] == "mal":
                with open(route + "/Liara (inteligencia artificial)/DATA/activated_syntax", "w") as write_module_hola:
                    write_module_hola.write("answer_mal")
                print("Oh, lo lamento, pero por que te sientes tan mal?")
                dont_know_condition = "no"
    
    if activated_syntax_readed == "answer_mal":
        if memory_readed_splited[a] == "mal":
            if interpretar[0] == "porque":
                print("Te entiendo")
                dont_know_condition = "no"
    if interpretar[0] == "gracias":
        print("por nada")
        dont_know_condition = "no"
    if input_length > 2:
        if interpretar[0] == "mi":
            if interpretar[1] == "nombre":
                with open(route + "/Liara (inteligencia artificial)/DATA/activated_syntax", "w") as anterior_syntax:
                    anterior_syntax.write("name_module")
                if interpretar[2] == "es":
                    with open(route + "/Liara (inteligencia artificial)/DATA/name", "w") as name_overwrite:
                        name_overwrite.write(interpretar[3].capitalize())
                    with open(route + "/Liara (inteligencia artificial)/DATA/name", "r") as name_file_changed:
                        name_2 = name_file_changed.readlines()
                        for i4 in name_2:
                            name_readed = i4
                    print("Oh, hola " + str(name_readed) + "!")
                    dont_know_condition = "no"
                if interpretar[2] == "no":
                    if input_length > 4:
                        if interpretar[3] == "es":
                            if interpretar[4].capitalize() == name_readed:
                                print("Oh, entonces te llamare usuario")
                                dont_know_condition = "no"
                                with open(route + "/Liara (inteligencia artificial)/DATA/name", "w") as file_name:
                                    file_name.write("usuario")
                                with open(route + "/Liara (inteligencia artificial)/DATA/name", "r") as file_name_read:
                                    name_4 = file_name_read.readlines()
                                    for i5 in name_4:
                                        name_readed = i5
                            elif interpretar[4].capitalize() != name_readed:
                                print("Yo se que tu nombre no es " + str(interpretar[4]).capitalize() + ", tu nombre es " + str(name_readed) )
                                dont_know_condition = "no"
    if interpretar[0] == "recuerdame":
        with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "r") as rec_num_file:
            rec_num_str = rec_num_file.readlines()
            for i10 in rec_num_str:
                rec_num_int = int(i10)
            rec_num_write = rec_num_int + 1
        with open(route + "/Liara (inteligencia artificial)/DATA/rec_num.", "w") as overwrite_rec_num_file:
            overwrite_rec_num_file.write(str(rec_num_write))
        write_recordatory = open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "r+")
        read_recordatory = write_recordatory.readlines()
        for i7 in read_recordatory:
            nothing_elimination = i7
            if nothing_elimination == "nothing_added":
                write_recordatory.close()
                write_recordatory = open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "w")
        length = len(interpretar)
        length_recordatory_used = length - 1
        initial_recordatory = 1
        while initial_recordatory <= length_recordatory_used:
            words_of_recordatory = interpretar[initial_recordatory]
            write_recordatory.write(words_of_recordatory + " ")
            initial_recordatory += 1
        write_recordatory.write("\n")
        write_recordatory.close()
        print("Ok, he agregado ese recordatorio")
        dont_know_condition = "no"
    
    if input_length > 2:    
        if interpretar[0] == "borra":
            if interpretar[1] == "todos":
                if interpretar[2] == "los":
                    if input_length > 3:
                        if interpretar[3] == "recordatorios":
                            with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "w") as delete_recordatories:
                                delete_recordatories.write("nothing_added")
                            with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "w") as overwrite_num_of_rec:
                                overwrite_num_of_rec.write("0")
                            print("Ok, he borrado todos los recordatorios")
                            dont_know_condition = "no"
            if interpretar[1] == "los":
                if interpretar[2] == "recordatorios":
                    with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "w") as delete_recordatories:
                        delete_recordatories.write("nothing_added")
                    with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "w") as overwrite_num_of_rec:
                        overwrite_num_of_rec.write("0")
                    print("Ok, he borrado todos los recordatorios")
                    dont_know_condition = "no"

    if input_length > 3:                
        if interpretar[0] == "cuales":
            if interpretar[1] == "son":
                if interpretar[2] == "los" or interpretar[2] == "mis":
                    if interpretar[3] == "recordatorios":
                        numerador_de_rec = 0
                        for i8 in recordatory_1:
                            if i8 == "nothing_added":
                                print("No tienes ningun recordatorio")
                                dont_know_condition = "no"
                            else:
                                numerador_de_rec += 1
                                print (str(numerador_de_rec) + ". " + i8)
                                dont_know_condition = "no"
    if input_length > 3:                                
        if interpretar[0] == "que":
            if interpretar[1] == "tengo":
                if interpretar[2] == "que":
                    if interpretar[3] == "hacer":
                        numerador_de_rec = 0
                        for i9 in recordatory_1:
                            if i9 == "nothing_added":
                                print("No tienes ningun recordatorio")
                                dont_know_condition = "no"
                            else:
                                numerador_de_rec += 1
                                print (str(numerador_de_rec) + ". " + i9)
                                dont_know_condition = "no"
    if input_length > 2:
        if interpretar[0] == "cuantos":
            if interpretar[1] == "recordatorios":
                if interpretar[2] == "hay" or interpretar[2] == "tengo":
                    print("Tienes " + str(num_of_rec_ready) + " recordatorios")
                    dont_know_condition = "no"
    if input_length > 2:                    
        if interpretar[0] == "borra":
            if interpretar[1] == "el":
                if interpretar[2] == "recordatorio":
                    num_recordatorio_a_borrar = int(interpretar[3])
                    if num_recordatorio_a_borrar > num_of_rec_ready:
                        print("No existe ningun recordatorio #" + str(num_recordatorio_a_borrar))
                        dont_know_condition = "no"
                    if num_recordatorio_a_borrar <= num_of_rec_ready:
                        print("Estas seguro de que deseas borrar el recordatorio #" + str(num_recordatorio_a_borrar) + "?")
                        answer_to_delete = raw_input("->").lower().strip()
                        while answer_to_delete != "si" and answer_to_delete != "no":
                            print("Perdon, no he entendido eso, debes escribir si o no")
                            answer_to_delete = raw_input("->").lower().strip()
                        if answer_to_delete == "no":
                            print("Ok, orden cancelada")
                            dont_know_condition = "no"
                        if answer_to_delete == "si":
                            with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "r") as search_recordatory_to_delete:
                                x_counter = -1
                                for x1 in search_recordatory_to_delete:
                                    x_counter += 1
                                    x_counter_for_while = x_counter
                                    while x_counter_for_while < num_recordatorio_a_borrar:
                                        recordatory_to_delete_ready = x1
                                        x_counter_for_while +=1
                            recordatory_deleted_file_opened = open(route + "/Liara (inteligencia artificial)/DATA/recordatory_deleted", "w")
                            with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "r") as recordatories_readed_for_deleting:
                                recordatories_readed_again = recordatories_readed_for_deleting.readlines()
                            for x2 in recordatories_readed_again:
                                if x2 != recordatory_to_delete_ready:
                                    recordatory_deleted_file_opened.write(str(x2))
                            recordatory_deleted_file_opened.close()
                            with open(route + "/Liara (inteligencia artificial)/DATA/recordatory_deleted", "r") as new_recordatories_ready:
                                new_recordatories_ready_readed = new_recordatories_ready.readlines()
                            with open(route + "/Liara (inteligencia artificial)/DATA/recordatories", "w") as new_recordatories_write:
                                for x3 in new_recordatories_ready_readed:
                                    new_recordatories_write.write(str(x3))
                            with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "r") as change_num_of_rec:
                                last_num_of_rec = change_num_of_rec.readlines()
                            for x4 in last_num_of_rec:
                                last_num_of_rec_readed = x4
                            new_num_of_rec = int(last_num_of_rec_readed) - 1
                            with open(route + "/Liara (inteligencia artificial)/DATA/rec_num", "w") as change_num_of_rec:
                                change_num_of_rec.write(str(new_num_of_rec))
                            print("Se ha borrado exitosamente el recordatorio #" + str(num_recordatorio_a_borrar))
                            dont_know_condition = "no"
                        
    
    if input_length > 2:                        
        if interpretar[0] == "como":
            if interpretar[1] == "te":
                if interpretar[2] == "llamas" or interpretar[2] == "llamas?":
                    print("Yo me llamo Liara. Soy una inteligencia artificial.")
                    dont_know_condition = "no"
    if input_length > 3:                    
        if interpretar[0] == "cual":
            if interpretar[1] == "es":
                if interpretar[2] == "tu":
                    if interpretar[3] == "nombre" or interpretar[3] == "nombre?":
                        print("Mi nombre es Liara. Soy una inteligencia artficial.")
                        dont_know_condition = "no"
    if input_length > 2:                    
        if interpretar[0] == "quien":
            if interpretar[1] == "te":
                if interpretar[2] == "creo" or interpretar[2] == "creo?":
                    print("Mi creador se llama Ernesto Quincoces Vazquez. EL tambien creo el CDBMTM, el CDBTF, y muchos mas!")
                    dont_know_condition = "no"
                    
    if interpretar[0] == "adios":
        dont_know_condition = "no"
                    
    if dont_know_condition == "yes":
        print("Perdon, no he entendido eso.")
                
    
    with open(route + "/Liara (inteligencia artificial)/DATA/memory", "w") as file_memory:
        file_memory.write(str(answer))

print("Adios " + str(name_readed) + "!")
    