import numpy as np
import pandas as pd
import cherrypy
from spyre import server
import my_script


class App(server.App):
    title = "Madyak"
    inputs = [{
        "type": "dropdown",
        "label": "Province1",
        "options": [{"label": i,"value": i} for i in my_script.city_list()],
        "key": "province1"},
        {
        "type": "dropdown",
        "label": "Province2",
        "options": [{"label": i,"value": i} for i in my_script.city_list()],
        "key": "province2"},
        {
        "type": "dropdown",
        "label": "Indexes",
        "options": [
            {"label": "VHI", "value" : "VHI"},
            {"label": "TCI", "value" : "TCI"},
            {"label": "VCI","value" : "VCI"}],
            "key":  "index"},
        {
        "type": 'slider',
        "label": 'Year',
        "key": 'year',
        "value": 2017,
        "min": 1981,
        "max": 2017
        },
        {
        "type":'slider',
        "label": 'Min',
        "key": 'freq1',
        "value": 0,
        "min": 0,
        "max": 53
        },
        {
        "type":'slider',
        "label": 'Max',
        "key": 'freq2',
        "value": 53,
        "min": 0,
        "max": 53
        }]


    tabs = ["Table_1", "Plot_1","Table_2", "Plot_2"]

    controls = [{
        "type": "button",
        "label": "Update",
        "id": "update_data"}]
    outputs = [
        {
            "type": "plot",
            "id": "plot1",
            "control_id": "update_data",
            "tab": "Plot_1"},
        {
            "type": "plot",
            "id": "plot2",
            "control_id": "update_data",
            "tab": "Plot_2"},
        {
            "type": "table",
            "id": "table_id_1",
            "control_id": "update_data",
            "tab": "Table_1"},
        {
            "type": "table",
            "id": "table_id_2",
            "control_id": "update_data",
            "tab": "Table_2"}]


    def table_id_1(self, params):
        prov = params['province1']
        ind = params['index']
        min = params['freq1']
        max = params['freq2']
        year = params['year']
        if min > max:
            return None
        df = my_script.data_frame_filter(province = prov,year=year, index = ind, min = min, max= max)
        return df


    def plot1(self, params):
        df = self.table_id_1(params)
        ind = params['index']
        obj = df[ind]
        plt_obj = obj.plot()
        return plt_obj


    def table_id_2(self, params):
        prov = params['province2']
        ind = params['index']
        min = params['freq1']
        max = params['freq2']
        year = params['year']
        if min > max:
            return None
        df = my_script.data_frame_filter(province = prov,year = year, index = ind, min = min, max= max)
        return df


    def plot2(self, params):
        df = self.table_id_2(params)
        ind = params['index']
        obj = df[ind]
        plt_obj = obj.plot()
        return plt_obj


app = App()
app.launch()