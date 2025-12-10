"""
🎄 Christmas Carols RSVP App 🎄
A festive invitation system for holiday gatherings
"""

import streamlit as st
import json
import os
from datetime import datetime, date, time
from pathlib import Path
import socket

# Configuration
DATA_FILE = Path(__file__).parent / "data" / "rsvps.json"
HOST_PASSWORD = "IccCarols2025"  # Host password

# Ensure data directory exists
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

# Initialize data file if it doesn't exist
if not DATA_FILE.exists():
    with open(DATA_FILE, "w") as f:
        json.dump({"responses": [], "event_details": {
            "title": "Indian Community Church, Santa Clara - Carols 🎄",
            "date": "2024-12-24",
            "time": "18:00",
            "location": "Indian Community Church, Santa Clara",
            "description": "Join us for an evening of joy, music, and Christmas carols! 🎵",
            "host_instructions": "🚗 Parking available in the church parking lot.\n🎁 Feel free to bring a dish to share!\n👗 Dress code: Festive casual"
        }}, f, indent=2)


def load_data():
    """Load RSVP data from file"""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if "host_instructions" not in data.get("event_details", {}):
                data.setdefault("event_details", {})["host_instructions"] = ""
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"responses": [], "event_details": {"host_instructions": ""}}


def save_data(data):
    """Save RSVP data to file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_total_attendees(responses):
    """Calculate total number of attendees"""
    return sum(r.get("num_guests", 0) for r in responses)


def get_app_url():
    """Get the URL for sharing the app"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "localhost"
    
    return {
        "local": "http://localhost:8501",
        "network": f"http://{local_ip}:8501"
    }


def format_date_display(date_str):
    """Format date string for display"""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%b %d, %Y")
    except:
        return date_str


def format_time_display(time_str):
    """Format time string for display"""
    try:
        t = datetime.strptime(time_str, "%H:%M")
        return t.strftime("%I:%M %p")
    except:
        return time_str


def apply_christmas_theme():
    """Apply festive Christmas styling - COMPACT MOBILE VIEW"""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@400;700&family=Crimson+Pro:wght@400;600&display=swap');
    
    /* Hide Streamlit branding for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 25%, #1a472a 50%, #0d2818 100%);
        background-attachment: fixed;
    }
    
    /* Snowfall animation */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, white, transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 90px 40px, white, transparent);
        background-size: 200px 200px;
        animation: snowfall 10s linear infinite;
        z-index: 0;
    }
    
    @keyframes snowfall {
        0% { background-position: 0 0; }
        100% { background-position: 200px 400px; }
    }
    
    /* COMPACT Main container for mobile */
    .main .block-container {
        background: rgba(255, 250, 245, 0.98);
        border-radius: 15px;
        padding: 0.8rem 0.8rem !important;
        margin: 0.3rem auto !important;
        max-width: 100%;
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        border: 2px solid #c41e3a;
        position: relative;
        z-index: 1;
    }
    
    @media (min-width: 768px) {
        .main .block-container {
            padding: 1.5rem 2rem !important;
            margin: 1rem auto !important;
            max-width: 700px;
            border-radius: 20px;
        }
    }
    
    /* COMPACT Header */
    h1 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #c41e3a !important;
        text-align: center;
        font-size: 1.4rem !important;
        margin: 0 0 0.3rem 0 !important;
        padding: 0 !important;
        line-height: 1.2 !important;
    }
    
    @media (min-width: 768px) {
        h1 {
            font-size: 2.2rem !important;
            margin-bottom: 0.5rem !important;
        }
    }
    
    h2 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #1a472a !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
    }
    
    h3 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #1a472a !important;
        font-size: 1rem !important;
        margin: 0.3rem 0 !important;
    }
    
    @media (min-width: 768px) {
        h2 { font-size: 1.5rem !important; }
        h3 { font-size: 1.2rem !important; }
    }
    
    /* ALL TEXT - DARK & VISIBLE */
    p, li, label, .stMarkdown, span, div, strong, em {
        font-family: 'Crimson Pro', serif !important;
        color: #1a1a1a !important;
    }
    
    /* Force dark text everywhere in main area */
    .main p, .main span, .main label, .main div, .main strong {
        color: #1a1a1a !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea textarea {
        border: 2px solid #1a472a !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        color: #1a1a1a !important;
        background-color: #ffffff !important;
        padding: 0.5rem !important;
    }
    
    /* Labels */
    .stTextInput label, .stNumberInput label, .stTextArea label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }
    
    /* COMPACT Button */
    .stButton > button {
        background: linear-gradient(135deg, #c41e3a 0%, #8b0000 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.6rem 1.2rem !important;
        font-family: 'Mountains of Christmas', cursive !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        min-height: 44px !important;
        width: 100%;
    }
    
    @media (min-width: 768px) {
        .stButton > button {
            font-size: 1.2rem !important;
            padding: 0.75rem 2rem !important;
        }
    }
    
    /* Success/Error messages */
    .stSuccess p, .stError p, .stInfo p, .stWarning p {
        color: inherit !important;
    }
    
    /* COMPACT Event card */
    .event-card {
        background: linear-gradient(135deg, #fffaf5 0%, #fff5eb 100%);
        border: 2px solid #d4af37;
        border-radius: 12px;
        padding: 0.6rem;
        margin: 0.4rem 0;
    }
    
    @media (min-width: 768px) {
        .event-card {
            padding: 1rem;
            margin: 0.8rem 0;
        }
    }
    
    .event-card h2, .event-card p, .event-card strong, .event-card div {
        color: #1a1a1a !important;
    }
    
    /* COMPACT Instructions card */
    .instructions-card {
        background: linear-gradient(135deg, #f5faff 0%, #eaf4ff 100%);
        border: 2px solid #1a472a;
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.4rem 0;
    }
    
    @media (min-width: 768px) {
        .instructions-card {
            padding: 1rem;
        }
    }
    
    .instructions-card h3, .instructions-card p, .instructions-card div {
        color: #1a1a1a !important;
    }
    
    /* COMPACT Stats cards */
    .stats-card {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 100%);
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.2rem 0;
        text-align: center;
    }
    
    .stats-card h3 {
        color: #ffd700 !important;
        font-size: 0.75rem !important;
        margin: 0 !important;
    }
    
    .stats-card p {
        color: white !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        margin: 0.2rem 0 0 0 !important;
    }
    
    @media (min-width: 768px) {
        .stats-card {
            padding: 1rem;
        }
        .stats-card h3 { font-size: 1rem !important; }
        .stats-card p { font-size: 1.8rem !important; }
    }
    
    /* Compact ornament */
    .ornament {
        font-size: 1.2rem;
        text-align: center;
        margin: 0.2rem 0;
        line-height: 1;
    }
    
    @media (min-width: 768px) {
        .ornament {
            font-size: 1.8rem;
            margin: 0.5rem 0;
        }
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a472a 0%, #0d2818 100%);
    }
    
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffd700 !important;
    }
    
    /* Horizontal rule - compact */
    hr {
        margin: 0.4rem 0 !important;
    }
    
    /* Reduce spacing between elements */
    .stMarkdown {
        margin-bottom: 0 !important;
    }
    
    .element-container {
        margin-bottom: 0.3rem !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        color: #1a472a !important;
        background-color: #fff8f0 !important;
    }
    
    .streamlit-expanderContent p,
    .streamlit-expanderContent div,
    .streamlit-expanderContent span {
        color: #1a1a1a !important;
    }
    
    /* Code blocks */
    .stCode code {
        color: #1a1a1a !important;
        background-color: #fffacd !important;
    }
    
    /* Date/Time inputs */
    .stDateInput input, .stTimeInput input {
        color: #1a1a1a !important;
        background-color: #ffffff !important;
        font-size: 16px !important;
    }
    
    /* Form submit button container - reduce spacing */
    [data-testid="stFormSubmitButton"] {
        margin-top: 0.3rem !important;
    }
    
    /* Mobile column stacking */
    @media (max-width: 767px) {
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_guest_view(data):
    """Render the COMPACT guest RSVP form"""
    event = data.get("event_details", {})
    
    # Compact header
    st.markdown('<div class="ornament">🎄 ⭐ 🎄</div>', unsafe_allow_html=True)
    st.title("You're Invited!")
    
    # Format date and time
    date_display = format_date_display(event.get('date', 'TBD'))
    time_display = format_time_display(event.get('time', 'TBD'))
    
    # COMPACT Event details card
    st.markdown(f"""
    <div class="event-card">
        <h2 style="text-align: center; margin: 0 0 0.3rem 0; font-size: 1.1rem;">{event.get('title', 'Christmas Carols')}</h2>
        <p style="text-align: center; font-size: 0.95rem; margin: 0 0 0.5rem 0; color: #333 !important;">{event.get('description', '')}</p>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 0.3rem; font-size: 0.9rem;">
            <div style="text-align: center;">
                <strong style="color: #1a472a !important;">📅</strong> {date_display}
            </div>
            <div style="text-align: center;">
                <strong style="color: #1a472a !important;">🕐</strong> {time_display}
            </div>
            <div style="text-align: center;">
                <strong style="color: #1a472a !important;">📍</strong> {event.get('location', 'TBD')}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Host Instructions (compact)
    host_instructions = event.get('host_instructions', '').strip()
    if host_instructions:
        st.markdown(f"""
        <div class="instructions-card">
            <h3 style="margin: 0 0 0.3rem 0; font-size: 0.95rem;">📋 Info from Host</h3>
            <div style="white-space: pre-line; font-size: 0.85rem; color: #1a1a1a !important;">{host_instructions}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # COMPACT RSVP Form
    st.markdown("#### 📝 RSVP")
    
    with st.form("rsvp_form", clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="Enter your name")
        num_guests = st.number_input("Number of Guests (including yourself)", min_value=1, max_value=20, value=1)
        
        submitted = st.form_submit_button("🎄 Submit RSVP 🎄", use_container_width=True)
        
        if submitted:
            if not name.strip():
                st.error("Please enter your name!")
            else:
                existing = [r for r in data["responses"] if r["name"].lower() == name.strip().lower()]
                
                new_response = {
                    "name": name.strip(),
                    "num_guests": num_guests,
                    "message": "",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                if existing:
                    for i, r in enumerate(data["responses"]):
                        if r["name"].lower() == name.strip().lower():
                            data["responses"][i] = new_response
                            break
                    save_data(data)
                    st.success(f"✨ Thanks {name}! RSVP updated. See you there! 🎉")
                else:
                    data["responses"].append(new_response)
                    save_data(data)
                    st.success(f"✨ Thanks {name}! See you there! 🎉")
                
                st.balloons()
    
    # Minimal footer
    st.markdown('<p style="text-align: center; font-size: 0.8rem; color: #555 !important; margin-top: 0.5rem;">🎵 Spread Christmas cheer! 🎵</p>', unsafe_allow_html=True)


def render_host_view(data):
    """Render the host dashboard"""
    st.title("🎅 Host Dashboard")
    
    # Share URL Section
    urls = get_app_url()
    with st.expander("🔗 Share URLs", expanded=False):
        st.code(urls["local"], language=None)
        st.code(urls["network"], language=None)
        st.info("💡 Deploy to Streamlit Cloud for public URL!")
    
    responses = data.get("responses", [])
    total_attendees = get_total_attendees(responses)
    
    # Stats cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <h3>Responses</h3>
            <p>{len(responses)}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <h3>Total Guests</h3>
            <p>{total_attendees}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Guest List
    if responses:
        st.markdown("### 📋 Guest List")
        for i, r in enumerate(sorted(responses, key=lambda x: x.get("timestamp", ""), reverse=True)):
            with st.expander(f"**{r['name']}** - {r['num_guests']} guest(s)"):
                st.write(f"**RSVP:** {r.get('timestamp', 'N/A')}")
                if st.button(f"❌ Remove", key=f"delete_{i}"):
                    data["responses"] = [resp for resp in data["responses"] if resp["name"] != r["name"]]
                    save_data(data)
                    st.rerun()
        
        # Summary table
        import pandas as pd
        df = pd.DataFrame([{
            "Name": r["name"],
            "Guests": r["num_guests"],
            "RSVP Date": r.get("timestamp", "N/A")[:10]
        } for r in responses])
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.download_button(
            label="📥 Download CSV",
            data=df.to_csv(index=False),
            file_name=f"carols_rsvps_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No RSVPs yet. Share your event link!")
    
    st.markdown("---")
    
    # Event Settings
    with st.expander("⚙️ Edit Event Details"):
        event = data.get("event_details", {})
        
        with st.form("event_settings"):
            new_title = st.text_input("Title", value=event.get("title", ""))
            
            col1, col2 = st.columns(2)
            with col1:
                try:
                    default_date = datetime.strptime(event.get("date", "2024-12-24"), "%Y-%m-%d").date()
                except:
                    default_date = date(2024, 12, 24)
                new_date = st.date_input("Date", value=default_date)
            
            with col2:
                try:
                    time_parts = event.get("time", "18:00").split(":")
                    default_time = time(int(time_parts[0]), int(time_parts[1]))
                except:
                    default_time = time(18, 0)
                new_time = st.time_input("Time", value=default_time)
            
            new_location = st.text_input("Location", value=event.get("location", ""))
            new_description = st.text_area("Description", value=event.get("description", ""), height=60)
            new_instructions = st.text_area("Host Instructions (parking, etc.)", value=event.get("host_instructions", ""), height=100)
            
            if st.form_submit_button("💾 Save"):
                data["event_details"] = {
                    "title": new_title,
                    "date": new_date.strftime("%Y-%m-%d"),
                    "time": new_time.strftime("%H:%M"),
                    "location": new_location,
                    "description": new_description,
                    "host_instructions": new_instructions
                }
                save_data(data)
                st.success("Saved!")
                st.rerun()
    
    with st.expander("🗑️ Danger Zone"):
        if st.button("Clear All RSVPs"):
            data["responses"] = []
            save_data(data)
            st.success("Cleared!")
            st.rerun()


def main():
    """Main application entry point"""
    st.set_page_config(
        page_title="ICC Santa Clara - Carols RSVP 🎄",
        page_icon="🎄",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    apply_christmas_theme()
    data = load_data()
    
    with st.sidebar:
        st.markdown("## 🎄 Menu")
        view = st.radio("", ["🎁 Guest RSVP", "🎅 Host"], label_visibility="collapsed")
        
        if view == "🎅 Host":
            st.markdown("---")
            password = st.text_input("Password", type="password")
            if password:
                if password == HOST_PASSWORD:
                    st.success("✅ Access granted!")
                    st.session_state["host_authenticated"] = True
                else:
                    st.error("❌ Wrong password")
                    st.session_state["host_authenticated"] = False
    
    if view == "🎁 Guest RSVP":
        render_guest_view(data)
    else:
        if st.session_state.get("host_authenticated", False):
            render_host_view(data)
        else:
            st.warning("🔐 Enter host password in sidebar")


if __name__ == "__main__":
    main()
