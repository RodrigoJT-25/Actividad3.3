import streamlit as st
import pandas as pd
from maze_solver import MAZE, START, END, solve_maze_bfs, solve_maze_dfs, solve_maze_astar

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

# Función para renderizar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀")  # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")  # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🔹")  # Camino resuelto
            elif col == 1:
                display_row.append("⬛")  # Muro
            else:
                display_row.append("⬜")  # Camino libre
        display_maze.append("".join(display_row))
    
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# Sidebar para controles
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo",
    ["BFS", "DFS", "A*"]
)
solve_button = st.sidebar.button("Resolver Laberinto")

# Mostrar laberinto inicial sin camino
render_maze(MAZE)

# Resolver cuando se presiona el botón
if solve_button:
    if algorithm == "BFS":
        path = solve_maze_bfs(MAZE, START, END)
    elif algorithm == "DFS":
        path = solve_maze_dfs(MAZE, START, END)
    else:  # A*
        path = solve_maze_astar(MAZE, START, END)

    if path:
        st.success(f"¡Camino encontrado con {algorithm}! Longitud del camino: {len(path)} pasos.")
        render_maze(MAZE, path)
    else:
        st.error("No se encontró un camino.")
