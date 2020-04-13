export class Voluntariado {
    nombre: string;
    id: number;
    descripcion: string;
    imagen: string;
    area: string;
    duracion: string;
    lugar: string;
    precio: number;
    calificaciones: Calificacion[];
    gustosRequeridos: Gusto[];
    idiomasRequeridos: Idioma[];
}

export class Calificacion {
    puntuacion: number;
    comentario: string;
    nombreVoluntario: string;
}

export class Gusto {
    nombre: string;
    grado: string;
}

export class Idioma {
    nombre: string;
    nivel: string;
}