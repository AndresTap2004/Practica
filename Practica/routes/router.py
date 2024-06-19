from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.comandoControllerDao import ComandoDaoControl
from controller.tda.linked.linkedList import LinkedList

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html')

@router.route('/comando')
def lista_comandos():
    cdc = ComandoDaoControl()
    return render_template('comando/lista.html', lista=cdc.to_dict())

@router.route('/comando/agregar_comando')
def nuevo_comando():
    return render_template('comando/guardar_comando.html')

@router.route('/comando/guardar/guardar_comando', methods = ['POST'])  
def guardar_comando():
    cdc = ComandoDaoControl()
    data = request.form
    if not "nombre_usuario" in data.keys():
       abort(400)
    cdc._comando._nombre_usuario = data['nombre_usuario']
    cdc._comando._apellido_usuario = data['apellido_usuario']
    cdc._comando._comando = data['comando']
    cdc._comando._lenguaje = data['lenguaje']
    cdc.save
    return redirect("/comando", code=302)

@router.route('/comando/sort/<tipo_ordenamiento>/<orden>/<attribute>')
def ordenar_comandos(tipo_ordenamiento, orden, attribute):
   
    print(tipo_ordenamiento, orden, attribute)
    cdc = ComandoDaoControl()
    lista = cdc._list()
    if tipo_ordenamiento == "ordenamiento_merge":
        lista_enviar = lista.metodos_merge_sort(lista, attribute = attribute, orden = int(orden))
    elif tipo_ordenamiento == "ordenamiento_shell":
        lista_enviar =lista.metodos_shell_sort(lista, attribute = attribute, orden = int(orden))
    elif tipo_ordenamiento == "ordenamiento_quick":
        lista_enviar =lista.metodos_quick_sort(lista, attribute = attribute, orden = int(orden))

    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": cdc.to_dict_listas(lista_enviar)}),
        200
    )
    
@router.route('/comando/search/<tipo_busqueda>/<busqueda_por_atributo>/<value>')
def buscar_comandos(tipo_busqueda, busqueda_por_atributo, value):
    cdc = ComandoDaoControl()
    lista = cdc._list()
    print(tipo_busqueda, busqueda_por_atributo, value)
    lista.metodos_merge_sort(lista, attribute = busqueda_por_atributo, orden = 1)
    if tipo_busqueda == "lineal_binaria":
        lista_enviar = lista.busqueda_lineal_binaria_linked(lista, attribute = busqueda_por_atributo, value = value)
        print("\n\n\n", type(lista_enviar), "\n\n\n")
    elif tipo_busqueda == "binaria":
        lista_enviar = lista.busqueda_binaria_linked(lista, attribute = busqueda_por_atributo, value = value)
        print("\n\n\n", type(lista_enviar), "\n\n\n")
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": cdc.to_dict_listas(lista_enviar)}),
        200
    )
    
