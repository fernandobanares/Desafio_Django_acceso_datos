from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    resultado = []
    for tarea in tareas:
        subtareas = SubTarea.objects.filter(tarea=tarea, eliminada=False)
        resultado.append({
            "tarea": tarea,
            "subtareas": list(subtareas)
        })
    return resultado

def crear_nueva_tarea(descripcion):
    nueva_tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id):
    sub_tarea = SubTarea.objects.get(id=sub_tarea_id)
    sub_tarea.eliminada = True
    sub_tarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla():
    arreglo_tareas = recupera_tareas_y_sub_tareas()
    for item in arreglo_tareas:
        tarea = item["tarea"]
        subtareas = item["subtareas"]
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")