import streamlit as st
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="RŪH | Fuel The Spirit",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BRAND ASSETS & STYLING ---
st.markdown("""
    <style>
    /* FORCE DARK THEME & INDUSTRIAL VIBE */
    .stApp {
        background-color: #0e0e0e;
        color: #e0e0e0;
    }
    
    /* HIDE DEFAULT STREAMLIT MENU/FOOTER */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* CUSTOM TYPOGRAPHY UTILITIES */
    .big-text {
        font-family: 'Arial Black', sans-serif;
        font-size: 4em;
        font-weight: 900;
        color: #FFFFFF;
        text-transform: uppercase;
        line-height: 1.1;
    }
    .highlight {
        color: #FF4500; /* Ember Orange */
    }
    .sub-text {
        font-family: 'Courier New', monospace;
        font-size: 1.2em;
        color: #888888;
    }
    
    /* BUTTON STYLING */
    .stButton>button {
        background-color: #1A1A1A;
        color: #FF4500;
        border: 1px solid #333;
        border-radius: 0px;
        font-family: 'Courier New', monospace;
        text-transform: uppercase;
        padding: 10px 24px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #FF4500;
        color: #FFFFFF;
        background-color: #FF4500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SVG ASSETS ---
HERO_SVG = """
<svg width="100%" height="100%" viewBox="0 0 1920 1080" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="1920" height="1080" fill="#1A1A1A"/>
    <rect width="1920" height="1080" fill="#000000" fill-opacity="0.2"/>
    <rect x="0" y="100" width="1920" height="15" fill="#FF4500"/>
    <text x="960" y="540" font-family="Impact, sans-serif" font-size="400" fill="#E0E0E0" text-anchor="middle" letter-spacing="20" font-weight="bold">RŪH</text>
    <text x="960" y="540" font-family="Arial, sans-serif" font-size="550" fill="#FF4500" fill-opacity="0.15" text-anchor="middle" dominant-baseline="middle" transform="rotate(-10 960 540)">روح</text>
    <text x="960" y="680" font-family="Courier New, monospace" font-size="40" fill="#FF4500" text-anchor="middle" letter-spacing="10" font-weight="bold">FUEL THE SPIRIT</text>
    <line x1="100" y1="950" x2="1820" y2="950" stroke="#555555" stroke-width="2"/>
    <text x="100" y="1000" font-family="Arial, sans-serif" font-size="24" fill="#888888">EST. SINGAPORE</text>
    <text x="1820" y="1000" font-family="Arial, sans-serif" font-size="24" fill="#888888" text-anchor="end">THE ANTI-ESTABLISHMENT KITCHEN</text>
</svg>
"""

def render_svg(svg_string):
    """Renders SVG string in Streamlit"""
    b64 = base64.b64encode(svg_string.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" width="100%"/>'
    st.markdown(html, unsafe_allow_html=True)

# --- SESSION STATE (Slide Navigation) ---
if 'slide' not in st.session_state:
    st.session_state.slide = 0

def next_slide():
    st.session_state.slide += 1

def prev_slide():
    st.session_state.slide -= 1

# --- SLIDE CONTENT FUNCTIONS ---

def slide_hero():
    render_svg(HERO_SVG)

def slide_manifesto():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('<div class="big-text">WE DON\'T DO <span class="highlight">NICE.</span><br>WE DO REAL.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("""
        ### **THE MANIFESTO**
        
        We’re on a mission to inject real soul into the city.
        Not just "good vibes." Not just "tasty food."
        
        We are talking about **RŪH**.
        That raw, contagious, fire-in-your-belly energy.
        The kind that shifts the atmosphere when you walk in.
        
        **WE SHARE THE RŪH.**
        Pass it on.
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1555939594-58d7cb561ad1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", caption="Industrial Soul")

def slide_menu():
    st.markdown('<div class="big-text" style="text-align:center;">THE <span class="highlight">LINEUP</span></div>', unsafe_allow_html=True)
    st.write("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🔥 THE GRIP (Wraps)")
        st.markdown("**The OG Fire**\n\nSlow-roasted lamb shoulder, harissa heat, sumac onions, dripping with garlic toum.")
    
    with col2:
        st.markdown("#### 🥣 THE STACK (Bowls)")
        st.markdown("**Concrete Jungle**\n\nTurmeric pearl couscous base, charcoal chicken, roasted cauliflower, pomegranate molasses.")
        
    with col3:
        st.markdown("#### 🍟 SIDE HUSTLE")
        st.markdown("**Afterburner Fries**\n\nShoestring fries dusted in za'atar and Aleppo pepper, smothered in feta cream.")

def slide_closing():
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 60vh; flex-direction: column; text-align: center;">
        <div class="big-text">YO-CHI OWNS THE LIGHT.</div>
        <div class="big-text"><span class="highlight">WE OWN THE FIRE.</span></div>
        <br><br>
        <div class="sub-text">RŪH | COMING SOON</div>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN APP LOGIC ---

# Slide Dictionary
slides = [slide_hero, slide_manifesto, slide_menu, slide_closing]

# Render Current Slide
slides[st.session_state.slide]()

# Navigation Controls (Bottom)
st.write("---")
c1, c2, c3 = st.columns([1, 8, 1])
with c1:
    if st.session_state.slide > 0:
        st.button("PREV", on_click=prev_slide)
with c3:
    if st.session_state.slide < len(slides) - 1:
        st.button("NEXT", on_click=next_slide)
        
       
