import streamlit as st
import pandas as pd
from sercop_client import SercopClient
import datetime

# Page Configuration
st.set_page_config(
    page_title="Oportunidades SERCOP",
    page_icon="🇪🇨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #0066cc;
        color: white;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0052a3;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .search-container {
        background-color: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }
    h3 {
        color: #333;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 500;
        margin-right: 0.5rem;
    }
    .tag-budget {
        background-color: #e3f2fd;
        color: #0d47a1;
    }
    .tag-date {
        background-color: #f3e5f5;
        color: #7b1fa2;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Client
@st.cache_resource
def get_client():
    return SercopClient()

client = get_client()

# Sidebar Filters
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Ecuador_flag_300.png/300px-Ecuador_flag_300.png", width=50)
    st.title("Filtros")
    
    current_year = datetime.datetime.now().year
    year = st.number_input("Año", min_value=2015, max_value=current_year, value=current_year)
    
    process_type = st.multiselect(
        "Tipo de Procedimiento",
        ["Menor Cuantía", "Ínfima Cuantía", "Cotización", "Licitación", "Subasta Inversa"],
        default=["Menor Cuantía", "Ínfima Cuantía"]
    )
    
    st.info("💡 Tip: Las 'Ínfimas Cuantías' son ideales para empezar.")

# Main Content
st.title("🚀 Buscador de Oportunidades SERCOP")
st.markdown("Encuentra procesos de contratación pública de manera fácil y rápida.")

# Search Section
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        keyword = st.text_input("¿Qué estás buscando?", placeholder="Ej: Limpieza, Papelería, Mantenimiento...")
    with col2:
        st.write("") # Spacer
        st.write("") # Spacer
        search_button = st.button("Buscar")

if search_button and keyword:
    with st.spinner(f"Buscando oportunidades para '{keyword}'..."):
        results = client.search_processes(keyword, year=year)
        
        if results and 'data' in results:
            data = results['data']
            
            # Filter by process type (Client side filtering as API doesn't support it directly in search)
            # Note: The API returns 'internal_type' or similar fields. We need to check the exact field name.
            # Based on the example: "internal_type": "Licitación"
            
            filtered_data = []
            if process_type:
                for item in data:
                    p_type = item.get('internal_type', '')
                    # Simple partial match
                    if any(pt.lower() in p_type.lower() for pt in process_type):
                        filtered_data.append(item)
            else:
                filtered_data = data
                
            st.success(f"Se encontraron {len(filtered_data)} procesos relevantes.")
            
            for item in filtered_data:
                # Extract details
                title = item.get('description', 'Sin descripción')
                ocid = item.get('ocid')
                buyer = item.get('buyerName', 'Entidad desconocida')
                date = item.get('date', 'Fecha no disponible')
                p_type = item.get('internal_type', 'N/A')
                
                # Render Card
                st.markdown(f"""
                <div class="result-card">
                    <h3>{title}</h3>
                    <p><strong>Entidad:</strong> {buyer}</p>
                    <div>
                        <span class="tag tag-budget">{p_type}</span>
                        <span class="tag tag-date">📅 {date}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("Ver Detalles"):
                    st.write(f"**ID del Proceso:** {ocid}")
                    st.write(f"**Descripción Completa:** {item.get('description')}")
                    if st.button("Ver en SERCOP", key=ocid):
                        # Construct URL (This is a guess, usually needs specific ID)
                        # Using the API link for now or a generic search link
                        st.write(f"Consulta el detalle oficial usando el ID: {ocid}")
                        
        else:
            st.warning("⚠️ No se encontraron resultados.")
            st.markdown("""
            **Sugerencias:**
            - Intenta con palabras más generales (ej: "limpieza", "alimentos", "obra").
            - **Prueba cambiando el año** en la barra lateral (ej: 2024).
            - Verifica que la ortografía sea correcta.
            """)

elif search_button and not keyword:
    st.error("Por favor ingresa una palabra clave.")

# Footer
st.markdown("---")
st.markdown("Desarrollado con ❤️ para las PYMES de Ecuador")
