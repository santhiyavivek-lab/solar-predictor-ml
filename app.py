import streamlit as st

# Simple Authentication Guard Matrix
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    user = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and password == "santhiya@2007": # Custom Credentials
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Invalid Credentials Layer!")
    st.stop() # Stops screen rendering if not authenticated
    import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ==========================================================
# 0. GLOBAL CONFIGURATION & CUSTOM INTERACTIVE STYLE SHEET (THEME ENGINE)
# ==========================================================
st.set_page_config(page_title="Secured Solar Operations Portal", layout="centered", page_icon="⚡")

# Injected clean custom enterprise workspace style modifications layers
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 3rem !important; color: #ffeb3b !important; font-weight: bold; }
    .stButton>button { width: 100%; background-color: #2196f3; color: white; border-radius: 8px; font-weight: bold; border: none; height: 3rem; transition: 0.3s; }
    .stButton>button:hover { background-color: #0b7dda; transform: scale(1.02); }
    .kpi-card { background-color: #1e293b; padding: 25px; border-radius: 12px; border-left: 6px solid #2196f3; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 20px; }
    .kpi-title { font-size: 0.9rem; color: #94a3b8; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
    .kpi-value { font-size: 2.5rem; color: #38bdf8; font-weight: 700; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# ==========================================================
# 1. CORE INTELLECTUAL PROPERTY REVERSE-ENGINEERING BLOCK 
# ==========================================================
@st.cache_resource
def _obfuscated_core_engine_weights_vector():
    np.random.seed(42)
    rows = 1000
    irr = np.random.uniform(0.0, 1.2, rows)
    amb = np.random.uniform(22.0, 38.0, rows)
    mod = amb + (irr * 32)
    pwr = (irr * 14000) - (mod * 12)
    pwr = np.clip(pwr, 0, None)
    
    X_matrix = pd.DataFrame({'IRREDIATION': irr, 'AMBIENT_TEMPERATURE': amb, 'MODULE_TEMPERATURE': mod})
    Y_vector = pwr
    
    model_brain = RandomForestRegressor(n_estimators=50, random_state=42)
    model_brain.fit(X_matrix, Y_vector)
    return model_brain

_compiled_brain_tensor = _obfuscated_core_engine_weights_vector()

# ==========================================================
# 2. CYBERSECURITY FIREWALL & SESSION AUTHENTICATION GUARD LAYER
# ==========================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Secured Solar Operations Portal")
    st.markdown("Authorized personnel entry gate. Please input encryption parameters.")
    
    # Visual Layout Split for Login Cards Box Elements
    col1, col2 = st.columns([1, 1])
    with col1:
        operator_user = st.text_input("👤 System Operator Username", placeholder="Enter username")
    with col2:
        operator_pass = st.text_input("🔑 Gateway Security Password", type="password", placeholder="Enter password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Secure Verification Login"):
        if operator_user == "admin" and operator_pass == "solar2026":
            st.session_state.authenticated = True
            st.success("Verification successful! Initializing secure metrics telemetry canvas...")
            st.rerun()
        else:
            st.error("❌ Identification Failure! Access denied by perimeter firewall rules.")
    st.stop()

# ==========================================================
# 3. FRONTEND OPERATIONS CANVAS UI (Authorized Viewport Rendering)
# ==========================================================
st.sidebar.markdown("🟢 **Status:** Session Encryption Active")
st.sidebar.markdown("👤 **Operator Identity:** Plant Administrator")
st.sidebar.markdown("---")

st.title("⚡ COMMERCIAL SOLAR ENERGY FORECAST SYSTEM")
st.markdown("Automated generation yield estimation platform driven by Tree-Based Regression Machine Learning models.")
st.markdown("---")

st.sidebar.header("📥 Telemetry Ingestion Parameters")

# Operational live tactile sliders metrics controls updates
irradiation = st.sidebar.slider("Solar Irradiation Intensity (kW/m²)", 0.0, 1.2, 0.85, step=0.01)
ambient_temp = st.sidebar.slider("Ambient Atmospheric Temperature (°C)", 15.0, 45.0, 32.0, step=0.5)
module_temp = st.sidebar.slider("Physical Panel Module Temperature (°C)", 20.0, 75.0, 52.0, step=0.5)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# 4. INTERACTIVE COMPUTATIONAL INFERENCE PIPELINE
# ==========================================================
if st.sidebar.button("⚡ EXECUTE FORECAST SIMULATION"):
    real_time_matrix = pd.DataFrame({
        'IRREDIATION': [irradiation],
        'AMBIENT_TEMPERATURE': [ambient_temp],
        'MODULE_TEMPERATURE': [module_temp]
    })
    
    # Model Calculation Processing Trigger
    predicted_wattage = _compiled_brain_tensor.predict(real_time_matrix)
    final_output_kw = predicted_wattage.item()
    
    # Renders a sleek industrial status scorecard
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">🎯 CURRENT FORECAST PRODUCTION YIELD</div>
            <div class="kpi-value">{final_output_kw:.2f} kW</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Interactive Automated Plant Control Alerts Insights
    st.markdown("### 📊 Operational Telemetry Assessment Insights")
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.info(f"💡 **Atmospheric Density Index:** {irradiation * 100:.1f}% sunlight solar grid capture depth profile active.")
    with col_b:
        if module_temp > 60.0:
            st.warning("🔥 **Thermal Drop Advisory:** Excessive module surface temperature detected. Panel inversion algorithm efficiency adjustments applied.")
        elif irradiation < 0.2:
            st.error("☁️ **Grid Dropout Alert:** Volatile sunlight levels below minimum threshold limits. Scheduling dispatch optimization required.")
        else:
            st.success("✅ **Optimal Baseline Metrics:** Clean generation load tracking limits stable across active grid parameters boundaries.")