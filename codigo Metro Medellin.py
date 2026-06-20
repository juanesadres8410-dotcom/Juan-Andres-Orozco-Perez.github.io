"""
Project: Medellín Metro Route Simulator
Author: Juan
Description: Uses NetworkX and Matplotlib to find and visualize the shortest path 
             between stations in the Medellín Metro system using Dijkstra's algorithm.
Usage: python "codigo Metro Medellin.py"
"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

G = nx.Graph()

stations = [
    "Niquía", "Bello", "Madera", "Acevedo", "Tricentenario", "Caribe", "Universidad",
    "Hospital", "Prado", "Parque Berrío", "San Antonio", "Alpujarra", "Exposiciones",
    "Industriales", "Poblado", "Aguacatala", "Ayurá", "Envigado", "Itagüí", "Sabaneta", "La Estrella",
    "Cisneros", "Suramericana", "Estadio", "Floresta", "Santa Lucía", "San Javier",
    "Andalucía", "Popular", "Santo Domingo",
    "Juan XXIII", "Vallejuelos", "La Aurora",
    "Arví"
]

G.add_nodes_from(stations)

line_a = [
    "Niquía", "Bello", "Madera", "Acevedo", "Tricentenario", "Caribe", "Universidad",
    "Hospital", "Prado", "Parque Berrío", "San Antonio", "Alpujarra", "Exposiciones",
    "Industriales", "Poblado", "Aguacatala", "Ayurá", "Envigado", "Itagüí", "Sabaneta", "La Estrella"
]

for i in range(len(line_a)-1):
    G.add_edge(line_a[i], line_a[i+1], weight=2, line='A') 

line_b = ["San Antonio", "Cisneros", "Suramericana", "Estadio", "Floresta", "Santa Lucía", "San Javier"]
for i in range(len(line_b)-1):
    G.add_edge(line_b[i], line_b[i+1], weight=2, line='B')

line_k = ["Acevedo", "Andalucía", "Popular", "Santo Domingo"]
for i in range(len(line_k)-1):
    G.add_edge(line_k[i], line_k[i+1], weight=3, line='K')

line_j = ["San Javier", "Juan XXIII", "Vallejuelos", "La Aurora"]
for i in range(len(line_j)-1):
    G.add_edge(line_j[i], line_j[i+1], weight=3, line='J')

G.add_edge("Santo Domingo", "Arví", weight=8, line='L')
G.add_edge("San Antonio", "San Antonio", weight=3)

pos = {
    "Niquía": (0, 21), "Bello": (0, 19), "Madera": (0, 17), "Acevedo": (0, 15),
    "Tricentenario": (0, 13.5), "Caribe": (0, 12), "Universidad": (0, 10.5),
    "Hospital": (0, 9), "Prado": (0, 7.5), "Parque Berrío": (0, 6),
    "San Antonio": (0, 4.5), "Alpujarra": (0, 3), "Exposiciones": (0, 1.5),
    "Industriales": (0, 0), "Poblado": (0, -2), "Aguacatala": (0, -3.5),
    "Ayurá": (0, -5), "Envigado": (0, -6.5), "Itagüí": (0, -8),
    "Sabaneta": (0, -9.5), "La Estrella": (0, -11),
    "Cisneros": (-2, 4), "Suramericana": (-3.5, 3.5), "Estadio": (-5, 3),
    "Floresta": (-6.5, 2.5), "Santa Lucía": (-8, 2), "San Javier": (-9.5, 1.5),
    "Andalucía": (1, 16), "Popular": (2, 17), "Santo Domingo": (3, 18),
    "Juan XXIII": (-10, 3), "Vallejuelos": (-11, 4.5), "La Aurora": (-12, 6),
    "Arví": (6, 19)
}

def find_optimal_route(origin, destination):
    if origin not in G or destination not in G:
        print("Estación no encontrada. Verifica el nombre.")
        return None, None

    try:
        path = nx.dijkstra_path(G, origin, destination, weight='weight')
        total_time = nx.dijkstra_path_length(G, origin, destination, weight='weight')
        
        print(f"\n✅ Ruta más rápida de **{origin}** a **{destination}**")
        print(f"   Estaciones: {' → '.join(path)}")
        print(f"   Tiempo estimado: {total_time} minutos")
        
        plt.figure(figsize=(14, 10))
        nx.draw_networkx_edges(G, pos, alpha=0.3, width=2)
        nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightgray')
        
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_size=400, node_color='red')
        nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
       
        legend_elements = [
            Line2D([0], [0], color='blue', lw=3, label='Línea A'),
            Line2D([0], [0], color='orange', lw=3, label='Línea B'),
            Line2D([0], [0], color='green', lw=3, label='Cable K'),
            Line2D([0], [0], color='purple', lw=3, label='Cable J'),
            Line2D([0], [0], color='brown', lw=3, label='Cable L'),
            Line2D([0], [0], color='red', lw=4, label='Ruta Óptima')
        ]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.title(f"Ruta más rápida: {origin} → {destination} ({total_time} min)", fontsize=16)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        return path, total_time
        
    except nx.NetworkXNoPath:
        print("No hay ruta entre estas estaciones.")
        return None, None

if __name__ == "__main__":
    print("🚇 Simulador de Rutas - Metro de Medellín (con NetworkX)")
    print("Estaciones disponibles:", sorted(stations))
    
    while True:
        origen = input("\nEstación de origen (o 'salir' para terminar): ").strip()
        if origen.lower() == 'salir':
            break
        destino = input("Estación de destino: ").strip()
        
        find_optimal_route(origen, destino)
    print("\n¡Gracias por usar el simulador de rutas del Metro de Medellín! Hasta pronto.")