import streamlit as st
import pandas as pd
from sercop_client import SercopClient
import datetime
import plotly.express as px
import io

# --- CONFIGURATION & SETUP ---
st.set_page_config(
    page_title="SERCOP Pro | Buscador Inteligente",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State for Saved Searches
if 'saved_searches' not in st.session_state:
    st.session_state.saved_searches = []

# --- CUSTOM CSS (PRO THEME) ---
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Card Style */
    .result-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    .result-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        border-color: #0066cc;
    }
    
    /* Typography */
    h1, h2, h3 {
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        color: #1a1a1a;
    }
    .card-title {
        color: #0066cc;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .card-meta {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 0.25rem;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    .badge-budget { background-color: #e3f2fd; color: #1565c0; }
    .badge-date { background-color: #f3e5f5; color: #7b1fa2; }
    .badge-type { background-color: #e8f5e9; color: #2e7d32; }
    
    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# --- CLIENT & CACHING ---
@st.cache_resource
def get_client():
    return SercopClient()

client = get_client()

@st.cache_data(ttl=3600) # Cache results for 1 hour
def search_api(keyword, year):
    return client.search_processes(keyword, year=year)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🎛️ Panel de Control")
    
    # Global Filters
    st.subheader("Filtros de Búsqueda")
    current_year = datetime.datetime.now().year
    year = st.number_input("Año Fiscal", min_value=2015, max_value=current_year, value=current_year)
    
    st.markdown("---")
    st.subheader("📍 Ubicación & Entidad")
    entity_filter = st.text_input("Entidad", placeholder="Ej: Municipio...")
    region_filter = st.text_input("Provincia/Región", placeholder="Ej: Pichincha...")
    
    st.markdown("---")
    st.subheader("💰 Presupuesto ($)")
    col_b1, col_b2 = st.columns(2)
    min_budget = col_b1.number_input("Mín", value=0.0, step=1000.0)
    max_budget = col_b2.number_input("Máx", value=0.0, step=1000.0)
    
    st.markdown("---")
    st.subheader("📅 Fechas")
    date_range = st.date_input(
        "Rango",
        value=(datetime.date(year, 1, 1), datetime.date(year, 12, 31))
    )

# --- MAIN LAYOUT ---
st.title("🚀 SERCOP Pro")

# Tabs for Navigation
tab_search, tab_analytics, tab_saved = st.tabs(["🔍 Buscador", "📊 Analíticas", "⭐ Guardados"])

# --- TAB 1: SEARCH ---
with tab_search:
    col_search, col_save = st.columns([4, 1])
    with col_search:
        keyword = st.text_input("Palabra Clave", placeholder="Ej: Limpieza, Seguridad, Transporte...", label_visibility="collapsed")
    with col_save:
        if st.button("💾 Guardar Búsqueda"):
            if keyword:
                if keyword not in st.session_state.saved_searches:
                    st.session_state.saved_searches.append(keyword)
                    st.toast(f"Búsqueda '{keyword}' guardada!", icon="✅")
    
    if keyword:
        with st.spinner("Consultando bases de datos..."):
            results = search_api(keyword, year)
            
            if results and 'data' in results:
                data = results['data']
                filtered_data = []
                
                # --- FILTERING ---
                start_date, end_date = date_range if len(date_range) == 2 else (None, None)
                
                for item in data:
                    # Entity
                    if entity_filter and entity_filter.lower() not in item.get('buyerName', '').lower(): continue
                    # Region
                    if region_filter:
                        if region_filter.lower() not in item.get('region', '').lower() and \
                           region_filter.lower() not in item.get('locality', '').lower(): continue
                    # Budget
                    try:
                        b_val = float(item.get('budget', '0'))
                        if max_budget > 0 and not (min_budget <= b_val <= max_budget): continue
                        if min_budget > 0 and b_val < min_budget: continue
                    except: pass
                    # Date
                    if start_date and end_date:
                        try:
                            d_val = datetime.datetime.strptime(item.get('date', '').split('T')[0], "%Y-%m-%d").date()
                            if not (start_date <= d_val <= end_date): continue
                        except: pass
                    
                    filtered_data.append(item)
                
                # --- DISPLAY RESULTS ---
                if filtered_data:
                    st.success(f"✅ {len(filtered_data)} oportunidades encontradas")
                    
                    # Prepare DataFrame for Display
                    df_display = pd.DataFrame(filtered_data)
                    
                    # Select and rename columns for the grid
                    cols_to_show = {
                        'ocid': 'ID Proceso',
                        'description': 'Descripción',
                        'buyerName': 'Entidad Contratante',
                        'budget': 'Presupuesto',
                        'date': 'Fecha',
                        'internal_type': 'Tipo',
                        'region': 'Región'
                    }
                    
                    # Filter columns that exist in the data
                    available_cols = [c for c in cols_to_show.keys() if c in df_display.columns]
                    df_grid = df_display[available_cols].rename(columns=cols_to_show)
                    
                    # Export Button
                    buffer = io.BytesIO()
                    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                        df_grid.to_excel(writer, index=False)
                    st.download_button("📥 Exportar Excel", buffer.getvalue(), f"resultados_{keyword}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    
                    # Interactive Dataframe
                    st.markdown("### 📋 Resultados (Selecciona una fila para ver rubros)")
                    
                    event = st.dataframe(
                        df_grid,
                        use_container_width=True,
                        hide_index=True,
                        on_select="rerun",
                        selection_mode="single-row",
                        column_config={
                            "Presupuesto": st.column_config.NumberColumn(format="$%.2f"),
                            "Fecha": st.column_config.DateColumn(format="YYYY-MM-DD"),
                        }
                    )
                    
                    # --- DETAIL VIEW (RUBROS) ---
                    if len(event.selection.rows) > 0:
                        selected_index = event.selection.rows[0]
                        selected_row = df_grid.iloc[selected_index]
                        selected_ocid = selected_row['ID Proceso']
                        
                        st.divider()
                        st.subheader(f"📦 Rubros: {selected_row['Descripción']}")
                        
                        with st.spinner(f"Cargando detalles del proceso {selected_ocid}..."):
                            details = client.get_process_details(selected_ocid)
                            
                            if details:
                                # Extract Items
                                try:
                                    # OCDS structure: releases[0].tender.items
                                    items = details['releases'][0]['tender']['items']
                                    
                                    if items:
                                        item_data = []
                                        for item in items:
                                            item_data.append({
                                                "ID Item": item.get('id', 'N/A'),
                                                "Descripción": item.get('description', 'N/A'),
                                                "Cantidad": item.get('quantity', 0),
                                                "Unidad": item.get('unit', {}).get('name', 'N/A'),
                                                "Precio Unit.": item.get('unit', {}).get('value', {}).get('amount', 0),
                                                "CPC": item.get('classification', {}).get('id', 'N/A')
                                            })
                                            
                                        df_items = pd.DataFrame(item_data)
                                        st.dataframe(
                                            df_items,
                                            use_container_width=True,
                                            hide_index=True,
                                            column_config={
                                                "Precio Unit.": st.column_config.NumberColumn(format="$%.4f")
                                            }
                                        )
                                    else:
                                        st.info("No se encontraron rubros (items) para este proceso.")
                                        
                                except (KeyError, IndexError, TypeError) as e:
                                    st.error(f"No se pudo extraer la estructura de items. Posible formato diferente.")
                                    # st.write(details) # Uncomment for debugging
                            else:
                                st.error("Error al conectar con la API de detalles.")

                else:
                    st.warning("No hay resultados con estos filtros.")
            else:
                st.info("No se encontraron procesos. Intenta con otra palabra o año.")

# --- TAB 2: ANALYTICS ---
with tab_analytics:
    if keyword and 'filtered_data' in locals() and filtered_data:
        st.subheader("📊 Análisis de Resultados")
        df_viz = pd.DataFrame(filtered_data)
        
        c1, c2 = st.columns(2)
        with c1:
            if 'internal_type' in df_viz.columns:
                fig = px.pie(df_viz, names='internal_type', title='Oportunidades por Tipo', hole=0.4)
                st.plotly_chart(fig, use_container_width=True)
        with c2:
            if 'buyerName' in df_viz.columns:
                top = df_viz['buyerName'].value_counts().head(7)
                fig2 = px.bar(top, orientation='h', title='Principales Compradores')
                st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Realiza una búsqueda para ver las analíticas.")

# --- TAB 3: SAVED SEARCHES ---
with tab_saved:
    st.subheader("⭐ Búsquedas Guardadas")
    if st.session_state.saved_searches:
        for i, saved_kw in enumerate(st.session_state.saved_searches):
            col_txt, col_del = st.columns([4, 1])
            with col_txt:
                st.markdown(f"**{saved_kw}**")
            with col_del:
                if st.button("❌", key=f"del_{i}"):
                    st.session_state.saved_searches.pop(i)
                    st.rerun()
    else:
        st.write("No tienes búsquedas guardadas aún.")
