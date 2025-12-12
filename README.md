# 🚀 SERCOP Pro | Buscador Inteligente de Contratación Pública

<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

**Plataforma web interactiva para búsqueda, análisis y monitoreo de procesos de contratación pública del SERCOP Ecuador**

[🎯 Características](#-características-principales) • [🚀 Instalación](#-instalación-rápida) • [📖 Uso](#-guía-de-uso)

</div>

---

## 📋 Descripción

**SERCOP Pro** es una aplicación web desarrollada con **Streamlit** que conecta directamente con la API oficial del **Servicio Nacional de Contratación Pública (SERCOP)** de Ecuador. Permite a empresas, consultores y analistas buscar oportunidades de negocio, analizar tendencias de mercado y exportar datos de licitaciones públicas de manera eficiente.

### 🎯 Problema que Resuelve

La plataforma oficial de SERCOP tiene limitaciones en búsquedas avanzadas, análisis estadístico y exportación masiva de datos. **SERCOP Pro** soluciona esto ofreciendo:

- ✅ **Búsqueda inteligente** con filtros múltiples simultáneos
- ✅ **Visualización de rubros (items)** detallados por proceso
- ✅ **Análisis visual** con gráficos interactivos
- ✅ **Exportación** a Excel con un clic
- ✅ **Guardado de búsquedas** frecuentes
- ✅ **Interfaz moderna** y responsive

---

## ✨ Características Principales

### 🔍 **Búsqueda Avanzada**
- Filtros por palabra clave, año fiscal, entidad contratante y región
- Rangos de presupuesto personalizables (mínimo y máximo)
- Filtrado por rango de fechas específico
- Resultados en tiempo real desde la API oficial del SERCOP
- Sistema de caché para consultas rápidas (1 hora de persistencia)

### 📦 **Vista Detallada de Rubros**
- Visualización completa de items (rubros) por proceso
- Información detallada: ID, descripción, cantidad, unidad, precio unitario
- Código CPC (Clasificador Central de Productos)
- Navegación intuitiva mediante selección de filas

### 📊 **Dashboard de Analíticas**
- **Gráfico circular**: Distribución de oportunidades por tipo de proceso
- **Gráfico de barras horizontal**: Top 7 entidades compradoras principales
- Visualizaciones interactivas con Plotly (zoom, hover, exportación)
- Análisis automático de resultados filtrados

### 💾 **Gestión de Búsquedas**
- Guardado de palabras clave frecuentes
- Lista persistente durante la sesión
- Eliminación individual de búsquedas guardadas
- Notificaciones toast de confirmación

### 📥 **Exportación de Datos**
- Exportación directa a Excel (.xlsx)
- Formato profesional con nombres de columna descriptivos
- Incluye todos los campos relevantes: ID, descripción, entidad, presupuesto, fecha, tipo, región
- Un clic para descargar resultados completos

### 🎨 **Interfaz Profesional**
- Diseño moderno con cards interactivas y efectos hover
- Sistema de badges codificados por color (presupuesto, fecha, tipo)
- Tema claro optimizado para productividad
- Layout de 3 columnas adaptable
- Sidebar organizado con paneles colapsables

---

## 🛠️ Stack Tecnológico

### **Frontend**
- **Streamlit**: Framework principal de UI interactiva
- **CSS Personalizado**: Estilos profesionales con hover effects y transiciones
- **Plotly Express**: Gráficos interactivos y visualizaciones dinámicas

### **Backend & Data Processing**
- **Python 3.8+**: Lenguaje principal
- **Pandas**: Manipulación y análisis de datos
- **OpenPyXL**: Generación de archivos Excel

### **API & Conexión**
- **SercopClient**: Cliente personalizado para API de SERCOP
- **Caché de Streamlit**: Optimización de consultas (TTL: 1 hora)

---

## 🚀 Instalación Rápida

### Prerrequisitos
```bash
Python 3.8 o superior
pip (gestor de paquetes)
```

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/Henrry-Lojan/Procesos_SERCOP.git
cd Procesos_SERCOP
```

### Paso 2: Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en: `http://localhost:8501`

---

## 📖 Guía de Uso

### 1️⃣ **Configurar Filtros**
En el panel lateral izquierdo:
- Selecciona el **año fiscal** de interés
- Ingresa el nombre de la **entidad** (opcional)
- Especifica la **provincia/región** (opcional)
- Define rangos de **presupuesto** en dólares
- Ajusta el **rango de fechas**

### 2️⃣ **Realizar Búsqueda**
- En la pestaña "🔍 Buscador", ingresa una **palabra clave** (ej: "limpieza", "seguridad", "transporte")
- Los resultados se cargarán automáticamente con el conteo de oportunidades
- Opcionalmente, guarda la búsqueda con el botón "💾 Guardar Búsqueda"

### 3️⃣ **Explorar Resultados**
- Visualiza la tabla interactiva con todos los procesos encontrados
- **Haz clic en cualquier fila** para ver los rubros (items) detallados del proceso
- Los rubros aparecerán debajo de la tabla con información completa

### 4️⃣ **Exportar Datos**
- Usa el botón "📥 Exportar Excel" para descargar los resultados
- El archivo incluirá todos los campos filtrados en formato profesional

### 5️⃣ **Analizar Tendencias**
- Ve a la pestaña "📊 Analíticas"
- Visualiza gráficos de distribución por tipo y principales compradores
- Interactúa con los gráficos (zoom, hover para detalles)

### 6️⃣ **Gestionar Búsquedas Guardadas**
- Accede a la pestaña "⭐ Guardados"
- Consulta tus búsquedas frecuentes
- Elimina las que ya no necesites

---

## 📊 Estructura del Proyecto

```
Procesos_SERCOP/
├── app.py                      # Aplicación principal Streamlit
├── sercop_client.py            # Cliente API SERCOP (conexión y requests)
├── requirements.txt            # Dependencias del proyecto
├── .gitignore                  # Archivos ignorados por Git
├── debug_api_response.py       # Script de pruebas de API
├── debug_filters.py            # Validación de filtros
├── details_sample.json         # Ejemplo de respuesta de detalles
├── test_api.py                 # Tests de endpoints
└── test_rubros_flow.py         # Tests de flujo de rubros
```

---

## 🎯 Casos de Uso

### **Para Empresas Proveedoras**
- Identificar oportunidades de licitación en tiempo real
- Filtrar por presupuesto objetivo y región de operación
- Analizar rubros específicos para preparar ofertas precisas
- Monitorear actividad de entidades clave

### **Para Consultores de Negocios**
- Análisis de mercado de contratación pública
- Identificación de tendencias por sector y entidad
- Generación de reportes de oportunidades para clientes
- Benchmarking de presupuestos en procesos similares

### **Para Analistas e Investigadores**
- Estudios de transparencia en compras públicas
- Análisis estadístico de distribución de contratos
- Investigación de patrones de gasto gubernamental
- Extracción de datos para estudios académicos

### **Para Entidades Públicas**
- Benchmarking de procesos similares de otras entidades
- Análisis de precios de mercado por rubro
- Planificación de procesos futuros con datos históricos

---

## 💡 Características Técnicas Destacadas

### **Optimización de Rendimiento**
- Sistema de caché de Streamlit con TTL de 1 hora
- Carga diferida de detalles (solo al seleccionar proceso)
- Cliente API reutilizable con `@st.cache_resource`

### **Manejo de Datos OCDS**
- Procesamiento del estándar **Open Contracting Data Standard (OCDS)**
- Extracción correcta de estructura: `releases[0].tender.items`
- Manejo robusto de errores en estructuras variables

### **Experiencia de Usuario**
- Estado de sesión persistente para búsquedas guardadas
- Notificaciones toast no intrusivas
- Sistema de rerun inteligente para actualizaciones dinámicas
- Feedback visual en cada acción (spinners, mensajes de éxito/error)

---

## 🔧 Dependencias Principales

```txt
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
openpyxl>=3.1.0
requests>=2.31.0
```

Para la lista completa, consulta `requirements.txt`

---

## 🚦 Roadmap

### ✅ **Versión Actual (v1.0)**
- Búsqueda con filtros múltiples
- Visualización de rubros detallados
- Dashboard de analíticas básicas
- Exportación a Excel

### 🔜 **Próximas Versiones**
- [ ] Sistema de alertas por email para nuevas oportunidades
- [ ] Modo oscuro (dark theme)
- [ ] Exportación a PDF con formato de reporte
- [ ] Filtros avanzados por código CPC
- [ ] Comparador de procesos similares
- [ ] Predicción de adjudicación con Machine Learning
- [ ] API REST propia para integración con otros sistemas
- [ ] Dashboard de administrador con métricas de uso

---

## 📝 Notas Importantes

### **Conexión con API Oficial**
Este proyecto utiliza la API pública oficial del SERCOP. Asegúrate de cumplir con los términos de uso del servicio.

### **Limitaciones**
- Los datos dependen de la disponibilidad y estructura de la API de SERCOP
- Algunas estructuras OCDS pueden variar entre procesos
- El caché de 1 hora puede retrasar la visualización de procesos muy recientes

### **Privacidad**
Todos los datos procesados provienen de fuentes públicas oficiales. No se almacena información privada o sensible.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/MejoraBusqueda`)
3. Commit tus cambios (`git commit -m 'Agrega filtro por modalidad'`)
4. Push a la rama (`git push origin feature/MejoraBusqueda`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**Henrry Lojan Tenesaca**

🏗️ Ingeniero Civil | 🌍 Especialista en Geomática y Geoinformación | 💻 Python Developer

Apasionado por la automatización de procesos y el análisis de datos aplicado a ingeniería civil y contratación pública.

### 📫 Contacto

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/tu-perfil)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tu.correo@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Henrry-Lojan)

---

## 🙏 Agradecimientos

- **SERCOP Ecuador** por proporcionar API pública de datos de contratación
- **Streamlit** por el excelente framework de desarrollo rápido
- Comunidad de desarrolladores Python Ecuador

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella ⭐**

*Desarrollado con ❤️ para facilitar el acceso a información de contratación pública en Ecuador*

</div>
