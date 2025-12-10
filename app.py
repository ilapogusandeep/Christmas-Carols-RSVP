"""
Christmas Carols RSVP App
A festive invitation system for holiday gatherings
"""

import streamlit as st
import json
from datetime import datetime, date, time
from pathlib import Path
import socket

# Configuration
DATA_FILE = Path(__file__).parent / "data" / "rsvps.json"
HOST_PASSWORD = "IccCarols2025"

# Ensure data directory exists
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

# Initialize data file if it doesn't exist
if not DATA_FILE.exists():
    with open(DATA_FILE, "w") as f:
        json.dump({"responses": [], "event_details": {
            "title": "Indian Community Church, Santa Clara - Carols",
            "date": "2024-12-24",
            "time": "18:00",
            "location": "Indian Community Church, Santa Clara",
            "description": "Join us for an evening of joy, music, and Christmas carols!",
            "host_instructions": "Parking available in the church parking lot.\nFeel free to bring a dish to share!\nDress code: Festive casual"
        }}, f, indent=2)


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if "host_instructions" not in data.get("event_details", {}):
                data.setdefault("event_details", {})["host_instructions"] = ""
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"responses": [], "event_details": {"host_instructions": ""}}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_total_attendees(responses):
    return sum(r.get("num_guests", 0) for r in responses)


def get_app_url():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "localhost"
    return {"local": "http://localhost:8501", "network": f"http://{local_ip}:8501"}


def format_date_display(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except:
        return date_str


def format_time_display(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
    except:
        return time_str


def apply_christmas_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@400;700&family=Crimson+Pro:wght@400;600&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 25%, #1a472a 50%, #0d2818 100%);
        background-attachment: fixed;
    }
    
    /* Snow effect */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, white, transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 90px 40px, white, transparent);
        background-size: 200px 200px;
        animation: snow 10s linear infinite;
        z-index: 0;
    }
    
    @keyframes snow {
        0% { background-position: 0 0; }
        100% { background-position: 200px 400px; }
    }
    
    /* Main container - ULTRA COMPACT */
    .main .block-container {
        background: rgba(255, 252, 248, 0.99);
        border-radius: 12px;
        padding: 0.5rem 0.6rem !important;
        padding-top: 0.3rem !important;
        margin: 0.2rem auto !important;
        max-width: 100%;
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
        border: 2px solid #c41e3a;
        position: relative;
        z-index: 1;
    }
    
    @media (min-width: 768px) {
        .main .block-container {
            padding: 1rem 1.5rem !important;
            margin: 0.5rem auto !important;
            max-width: 650px;
        }
    }
    
    /* Title - NO TOP MARGIN */
    h1 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #c41e3a !important;
        text-align: center;
        font-size: 1.3rem !important;
        margin: 0 !important;
        padding: 0 !important;
        line-height: 1.1 !important;
    }
    
    @media (min-width: 768px) {
        h1 { font-size: 2rem !important; }
    }
    
    h2, h3, h4 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #1a472a !important;
        margin: 0.2rem 0 !important;
    }
    
    h2 { font-size: 1rem !important; }
    h3 { font-size: 0.95rem !important; }
    h4 { font-size: 0.9rem !important; }
    
    /* ALL TEXT - DARK */
    p, li, label, span, div, strong, em, .stMarkdown {
        font-family: 'Crimson Pro', serif !important;
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
        padding: 0.4rem !important;
    }
    
    /* Labels - DARK */
    .stTextInput label, .stNumberInput label, .stTextArea label,
    .stSelectbox label, .stRadio label {
        color: #1a1a1a !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
    }
    
    /* Radio buttons on main page - VISIBLE */
    .stRadio > div {
        background: #fff8f0;
        padding: 0.3rem 0.5rem;
        border-radius: 8px;
        border: 1px solid #d4af37;
    }
    
    .stRadio label span {
        color: #1a1a1a !important;
        font-weight: 600 !important;
    }
    
    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #c41e3a 0%, #8b0000 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.5rem 1rem !important;
        font-family: 'Mountains of Christmas', cursive !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        min-height: 42px !important;
        width: 100%;
    }
    
    /* Event card - COMPACT */
    .event-card {
        background: linear-gradient(135deg, #fffbf5 0%, #fff8ee 100%);
        border: 2px solid #d4af37;
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.3rem 0;
    }
    
    .event-card h2, .event-card p, .event-card strong, .event-card div {
        color: #1a1a1a !important;
    }
    
    /* Instructions card */
    .instructions-card {
        background: #f8fcff;
        border: 1px solid #1a472a;
        border-radius: 8px;
        padding: 0.4rem;
        margin: 0.3rem 0;
    }
    
    .instructions-card h3, .instructions-card p, .instructions-card div {
        color: #1a1a1a !important;
    }
    
    /* Stats cards */
    .stats-card {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 100%);
        border-radius: 8px;
        padding: 0.4rem;
        margin: 0.2rem 0;
        text-align: center;
    }
    
    .stats-card h3 {
        color: #ffd700 !important;
        font-size: 0.7rem !important;
        margin: 0 !important;
    }
    
    .stats-card p {
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        margin: 0.1rem 0 0 0 !important;
    }
    
    /* Compact spacing */
    hr { margin: 0.3rem 0 !important; }
    .element-container { margin-bottom: 0.2rem !important; }
    [data-testid="stFormSubmitButton"] { margin-top: 0.2rem !important; }
    
    /* Expander */
    .streamlit-expanderHeader {
        color: #1a472a !important;
        background-color: #fff8f0 !important;
        font-size: 0.9rem !important;
    }
    
    .streamlit-expanderContent p, .streamlit-expanderContent div, .streamlit-expanderContent span {
        color: #1a1a1a !important;
    }
    
    /* Password input in main area */
    .stTextInput input[type="password"] {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
    }
    
    /* Mobile columns */
    @media (max-width: 767px) {
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
        }
    }
    
    /* Success/Error */
    .stSuccess, .stError, .stInfo, .stWarning {
        padding: 0.4rem !important;
        font-size: 0.85rem !important;
    }
    </style>
    """, unsafe_allow_html=True)


def render_guest_view(data):
    """Render COMPACT guest RSVP form"""
    event = data.get("event_details", {})
    
    # Title - NO EXTRA SPACE
    st.title("You're Invited!")
    
    date_display = format_date_display(event.get('date', 'TBD'))
    time_display = format_time_display(event.get('time', 'TBD'))
    
    # Event card - NO EMOJIS
    st.markdown(f"""
    <div class="event-card">
        <h2 style="text-align: center; margin: 0 0 0.2rem 0;">{event.get('title', 'Christmas Carols')}</h2>
        <p style="text-align: center; font-size: 0.9rem; margin: 0 0 0.3rem 0;">{event.get('description', '')}</p>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; font-size: 0.85rem;">
            <span><strong>Date:</strong> {date_display}</span>
            <span><strong>Time:</strong> {time_display}</span>
            <span><strong>Place:</strong> {event.get('location', 'TBD')}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Host Instructions - NO EMOJIS
    host_instructions = event.get('host_instructions', '').strip()
    if host_instructions:
        st.markdown(f"""
        <div class="instructions-card">
            <h3 style="margin: 0 0 0.2rem 0; font-size: 0.85rem;">Info from Host:</h3>
            <div style="white-space: pre-line; font-size: 0.8rem;">{host_instructions}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # RSVP Form - NO EMOJIS
    st.markdown("#### RSVP Here")
    
    with st.form("rsvp_form", clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="Enter your name")
        num_guests = st.number_input("Number of Guests (including yourself)", min_value=1, max_value=20, value=1)
        
        submitted = st.form_submit_button("* Submit RSVP *", use_container_width=True)
        
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
                    st.success(f"Thanks {name}! RSVP updated!")
                else:
                    data["responses"].append(new_response)
                    save_data(data)
                    st.success(f"Thanks {name}! See you there!")
                st.balloons()


def render_host_view(data):
    """Render host dashboard"""
    st.title("Host Dashboard")
    
    # Check authentication
    if not st.session_state.get("host_authenticated", False):
        st.markdown("#### Enter Password")
        password = st.text_input("Password", type="password", key="host_pwd")
        if st.button("Login"):
            if password == HOST_PASSWORD:
                st.session_state["host_authenticated"] = True
                st.rerun()
            else:
                st.error("Wrong password!")
        return
    
    # Share URLs
    urls = get_app_url()
    with st.expander("Share URLs"):
        st.code(urls["local"])
        st.code(urls["network"])
    
    responses = data.get("responses", [])
    total_attendees = get_total_attendees(responses)
    
    # Stats
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stats-card"><h3>Responses</h3><p>{len(responses)}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stats-card"><h3>Total Guests</h3><p>{total_attendees}</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    if responses:
        st.markdown("### Guest List")
        for i, r in enumerate(sorted(responses, key=lambda x: x.get("timestamp", ""), reverse=True)):
            with st.expander(f"{r['name']} - {r['num_guests']} guest(s)"):
                st.write(f"RSVP: {r.get('timestamp', 'N/A')}")
                if st.button("Remove", key=f"del_{i}"):
                    data["responses"] = [x for x in data["responses"] if x["name"] != r["name"]]
                    save_data(data)
                    st.rerun()
        
        import pandas as pd
        df = pd.DataFrame([{"Name": r["name"], "Guests": r["num_guests"], "Date": r.get("timestamp", "")[:10]} for r in responses])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button("Download CSV", df.to_csv(index=False), f"rsvps_{datetime.now().strftime('%Y%m%d')}.csv")
    else:
        st.info("No RSVPs yet!")
    
    st.markdown("---")
    
    with st.expander("Edit Event"):
        event = data.get("event_details", {})
        with st.form("settings"):
            title = st.text_input("Title", event.get("title", ""))
            col1, col2 = st.columns(2)
            with col1:
                try:
                    d = datetime.strptime(event.get("date", "2024-12-24"), "%Y-%m-%d").date()
                except:
                    d = date(2024, 12, 24)
                new_date = st.date_input("Date", d)
            with col2:
                try:
                    t = event.get("time", "18:00").split(":")
                    new_time = st.time_input("Time", time(int(t[0]), int(t[1])))
                except:
                    new_time = st.time_input("Time", time(18, 0))
            loc = st.text_input("Location", event.get("location", ""))
            desc = st.text_area("Description", event.get("description", ""), height=50)
            instr = st.text_area("Host Instructions", event.get("host_instructions", ""), height=80)
            
            if st.form_submit_button("Save"):
                data["event_details"] = {
                    "title": title, "date": new_date.strftime("%Y-%m-%d"),
                    "time": new_time.strftime("%H:%M"), "location": loc,
                    "description": desc, "host_instructions": instr
                }
                save_data(data)
                st.success("Saved!")
                st.rerun()
    
    with st.expander("Clear All"):
        if st.button("Clear RSVPs"):
            data["responses"] = []
            save_data(data)
            st.rerun()


def main():
    st.set_page_config(
        page_title="ICC Carols RSVP",
        page_icon="*",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    apply_christmas_theme()
    data = load_data()
    
    # MODE TOGGLE ON MAIN PAGE - NO EMOJIS
    st.markdown("##### Select:")
    mode = st.radio("", ["Guest RSVP", "Host Login"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("---")
    
    if mode == "Guest RSVP":
        render_guest_view(data)
    else:
        render_host_view(data)


if __name__ == "__main__":
    main()
