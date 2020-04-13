import { Voluntariado } from "./Voluntariado";

import * as http from 'http';


let proyectos:Voluntariado[] = []

const url: string = 'localhost:8080/voluntariados/list';

try {
    const response = http.get(url);
    console.log(response.on())
} catch (exception) {
    console.error(exception)
}