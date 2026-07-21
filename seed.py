from datetime import datetime


def generar_datos_precarga():
    return [
        {
            "nombre_cliente": "Juan Pérez",
            "rut_cliente": "12345678-9",
            "telefono": "+56912345678",
            "email": "juan.perez@mail.com",
            "vehiculo": {
                "marca": "Toyota",
                "modelo": "Yaris",
                "anio": 2019,
                "patente": "ABCD12",
                "color": "Rojo"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 3, 10),
                    "tipo_servicio": "Cambio de aceite",
                    "descripcion": "Cambio de aceite y filtro",
                    "costo": 35000,
                    "mecanico_asignado": "Carlos Soto",
                    "estado": "Completado"
                },
                {
                    "fecha_servicio": datetime(2025, 8, 22),
                    "tipo_servicio": "Frenos",
                    "descripcion": "Cambio de pastillas de freno delanteras",
                    "costo": 60000,
                    "mecanico_asignado": "Carlos Soto",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2024, 11, 5)
        },
        {
            "nombre_cliente": "María González",
            "rut_cliente": "9876543-2",
            "telefono": "+56987654321",
            "email": "maria.gonzalez@mail.com",
            "vehiculo": {
                "marca": "Chevrolet",
                "modelo": "Spark",
                "anio": 2021,
                "patente": "XYZW88",
                "color": "Blanco"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 1, 15),
                    "tipo_servicio": "Revisión técnica",
                    "descripcion": "Revisión general previa a la RT",
                    "costo": 25000,
                    "mecanico_asignado": "Ana Reyes",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2025, 1, 2)
        },
        {
            "nombre_cliente": "Pedro Ramírez",
            "rut_cliente": "11222333-4",
            "telefono": "+56911223344",
            "email": "pedro.ramirez@mail.com",
            "vehiculo": {
                "marca": "Nissan",
                "modelo": "Versa",
                "anio": 2018,
                "patente": "JKLM45",
                "color": "Gris"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 5, 3),
                    "tipo_servicio": "Cambio de aceite",
                    "descripcion": "Mantención de 20.000 km",
                    "costo": 40000,
                    "mecanico_asignado": "Carlos Soto",
                    "estado": "Completado"
                },
                {
                    "fecha_servicio": datetime(2025, 9, 18),
                    "tipo_servicio": "Suspensión",
                    "descripcion": "Cambio de amortiguadores traseros",
                    "costo": 120000,
                    "mecanico_asignado": "Luis Fuentes",
                    "estado": "Pendiente"
                }
            ],
            "fecha_registro": datetime(2024, 12, 20)
        },
        {
            "nombre_cliente": "Camila Torres",
            "rut_cliente": "15788999-1",
            "telefono": "+56915788999",
            "email": "camila.torres@mail.com",
            "vehiculo": {
                "marca": "Hyundai",
                "modelo": "Accent",
                "anio": 2022,
                "patente": "PQRS77",
                "color": "Azul"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 6, 1),
                    "tipo_servicio": "Frenos",
                    "descripcion": "Cambio de pastillas y discos",
                    "costo": 85000,
                    "mecanico_asignado": "Ana Reyes",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2025, 2, 14)
        },
        {
            "nombre_cliente": "Diego Morales",
            "rut_cliente": "17344556-7",
            "telefono": "+56917344556",
            "email": "diego.morales@mail.com",
            "vehiculo": {
                "marca": "Toyota",
                "modelo": "Corolla",
                "anio": 2020,
                "patente": "TUVW33",
                "color": "Negro"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 4, 11),
                    "tipo_servicio": "Cambio de aceite",
                    "descripcion": "Mantención de 30.000 km",
                    "costo": 38000,
                    "mecanico_asignado": "Luis Fuentes",
                    "estado": "Completado"
                },
                {
                    "fecha_servicio": datetime(2025, 10, 2),
                    "tipo_servicio": "Batería",
                    "descripcion": "Cambio de batería",
                    "costo": 55000,
                    "mecanico_asignado": "Carlos Soto",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2024, 10, 30)
        },
        {
            "nombre_cliente": "Valentina Rojas",
            "rut_cliente": "18899001-2",
            "telefono": "+56918899001",
            "email": "valentina.rojas@mail.com",
            "vehiculo": {
                "marca": "Kia",
                "modelo": "Rio",
                "anio": 2017,
                "patente": "LMNO22",
                "color": "Plata"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 7, 7),
                    "tipo_servicio": "Neumáticos",
                    "descripcion": "Cambio de 4 neumáticos",
                    "costo": 180000,
                    "mecanico_asignado": "Ana Reyes",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2025, 3, 8)
        },
        {
            "nombre_cliente": "Andrés Silva",
            "rut_cliente": "19233445-8",
            "telefono": "+56919233445",
            "email": "andres.silva@mail.com",
            "vehiculo": {
                "marca": "Suzuki",
                "modelo": "Swift",
                "anio": 2023,
                "patente": "EFGH66",
                "color": "Amarillo"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 2, 20),
                    "tipo_servicio": "Cambio de aceite",
                    "descripcion": "Primera mantención",
                    "costo": 32000,
                    "mecanico_asignado": "Luis Fuentes",
                    "estado": "Completado"
                }
            ],
            "fecha_registro": datetime(2025, 1, 25)
        },
        {
            "nombre_cliente": "Francisca Muñoz",
            "rut_cliente": "20344556-9",
            "telefono": "+56920344556",
            "email": "francisca.munoz@mail.com",
            "vehiculo": {
                "marca": "Mazda",
                "modelo": "CX-3",
                "anio": 2021,
                "patente": "IJKL99",
                "color": "Rojo"
            },
            "historial_servicios": [
                {
                    "fecha_servicio": datetime(2025, 5, 30),
                    "tipo_servicio": "Frenos",
                    "descripcion": "Revisión y ajuste de freno de mano",
                    "costo": 20000,
                    "mecanico_asignado": "Carlos Soto",
                    "estado": "Completado"
                },
                {
                    "fecha_servicio": datetime(2025, 11, 15),
                    "tipo_servicio": "Aire acondicionado",
                    "descripcion": "Carga de gas refrigerante",
                    "costo": 45000,
                    "mecanico_asignado": "Ana Reyes",
                    "estado": "Pendiente"
                }
            ],
            "fecha_registro": datetime(2025, 4, 2)
        }
    ]
