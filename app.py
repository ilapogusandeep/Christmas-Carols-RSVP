"""
Christmas Carols RSVP App
"""

import streamlit as st
import json
from datetime import datetime, date, time
from pathlib import Path
import socket

DATA_FILE = Path(__file__).parent / "data" / "rsvps.json"
HOST_PASSWORD = "IccCarols2025"

DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

if not DATA_FILE.exists():
    with open(DATA_FILE, "w") as f:
        json.dump({"responses": [], "event_details": {
            "title": "Indian Community Church, Santa Clara - Carols",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": "18:00",
            "location": "Indian Community Church, Santa Clara",
            "description": "Join us in the Christmas Caroling to share the joy of Christmas with our brothers and sisters families!",
            "host_instructions": "Parking available in the church parking lot.\nFeel free to bring a dish to share!\nDress code: Festive casual"
        }}, f, indent=2)


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if "host_instructions" not in data.get("event_details", {}):
                data.setdefault("event_details", {})["host_instructions"] = ""
            return data
    except:
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
    return f"http://{local_ip}:8501"


def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except:
        return date_str


def format_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
    except:
        return time_str


def apply_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@700&family=Crimson+Pro:wght@400;600&display=swap');
    
    #MainMenu, footer, header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 50%, #0d2818 100%);
        background-attachment: fixed;
    }
    
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, white, transparent),
            radial-gradient(2px 2px at 80px 60px, rgba(255,255,255,0.7), transparent);
        background-size: 150px 150px;
        animation: snow 8s linear infinite;
        z-index: 0;
    }
    
    @keyframes snow {
        0% { background-position: 0 0; }
        100% { background-position: 150px 300px; }
    }
    
    /* ZERO TOP PADDING */
    .main .block-container {
        background: rgba(255, 253, 250, 0.98);
        border-radius: 12px;
        padding: 0.3rem 0.5rem !important;
        padding-top: 0 !important;
        margin: 0 auto !important;
        margin-top: 0 !important;
        max-width: 100%;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        border: 2px solid #c41e3a;
        position: relative;
        z-index: 1;
    }
    
    .main > div { padding-top: 0 !important; }
    .block-container { padding-top: 0 !important; }
    
    @media (min-width: 768px) {
        .main .block-container {
            padding: 0.6rem 1rem !important;
            padding-top: 0.2rem !important;
            max-width: 600px;
        }
    }
    
    h1 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #c41e3a !important;
        text-align: center;
        font-size: 1.4rem !important;
        margin: 0 !important;
        margin-top: 0 !important;
        padding: 0 !important;
        padding-top: 0.2rem !important;
        line-height: 1.1 !important;
    }
    
    h2, h3, h4, h5 {
        font-family: 'Mountains of Christmas', cursive !important;
        color: #1a472a !important;
        margin: 0.2rem 0 !important;
    }
    
    /* ALL TEXT DARK */
    p, li, label, span, div, strong, em, .stMarkdown, h5 {
        font-family: 'Crimson Pro', serif !important;
        color: #222222 !important;
    }
    
    /* Form labels - dark green color */
    label, .stTextInput label, .stNumberInput label, .stTextArea label {
        color: #1a472a !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }
    
    /* Form submit button - RED */
    [data-testid="stFormSubmitButton"] button {
        background: linear-gradient(135deg, #c41e3a 0%, #8b0000 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        font-family: 'Mountains of Christmas', cursive !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }
    
    input, textarea {
        border: 2px solid #1a472a !important;
        border-radius: 8px !important;
        font-size: 16px !important;
        color: #222222 !important;
        background: #ffffff !important;
    }
    
    /* Radio buttons - white text on green */
    .stRadio > div {
        background: #1a472a;
        padding: 0.3rem 0.5rem;
        border-radius: 8px;
        border: 1px solid #d4af37;
    }
    
    .stRadio label, .stRadio span, .stRadio p, .stRadio div {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* Checkbox - white text */
    .stCheckbox label, .stCheckbox span, .stCheckbox p {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    .stCheckbox > div {
        background: rgba(26, 71, 42, 0.8);
        padding: 0.3rem 0.5rem;
        border-radius: 6px;
    }
    
    /* All text outside main container - white */
    .stApp > div > div > div > div > div:not(.main) label,
    .stApp > div > div > div > div > div:not(.main) span,
    .stApp > div > div > div > div > div:not(.main) p {
        color: #ffffff !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #c41e3a 0%, #8b0000 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.5rem 1rem !important;
        font-family: 'Mountains of Christmas', cursive !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        min-height: 44px !important;
    }
    
    .event-card {
        background: linear-gradient(135deg, #fffbf5 0%, #fff8ee 100%);
        border: 2px solid #d4af37;
        border-radius: 10px;
        padding: 0.5rem;
        margin: 0.3rem 0;
    }
    
    .event-card * { color: #222222 !important; }
    
    .info-card {
        background: #f5f9ff;
        border: 1px solid #1a472a;
        border-radius: 8px;
        padding: 0.4rem;
        margin: 0.3rem 0;
    }
    
    .info-card * { color: #222222 !important; }
    
    .stats-card {
        background: linear-gradient(135deg, #1a472a 0%, #2d5016 100%);
        border-radius: 8px;
        padding: 0.4rem;
        margin: 0.2rem 0;
        text-align: center;
    }
    
    .stats-card h4 { color: #ffd700 !important; font-size: 0.75rem !important; margin: 0 !important; }
    .stats-card p { color: white !important; font-size: 1.2rem !important; font-weight: bold !important; margin: 0 !important; }
    
    .guest-row {
        background: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 6px;
        padding: 0.4rem 0.5rem;
        margin: 0.2rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .guest-row * { color: #222222 !important; }
    
    .delete-btn {
        background: #dc3545;
        color: white !important;
        border: none;
        border-radius: 4px;
        padding: 0.2rem 0.5rem;
        font-size: 0.75rem;
        cursor: pointer;
    }
    
    .bottom-toggle {
        background: #1a472a;
        border-radius: 8px;
        padding: 0.3rem;
        margin-top: 0.5rem;
        text-align: center;
    }
    
    .bottom-toggle * { color: #ffd700 !important; }
    
    hr { margin: 0.3rem 0 !important; border-color: #ddd !important; }
    
    .stSuccess, .stError, .stInfo { font-size: 0.85rem !important; }
    </style>
    """, unsafe_allow_html=True)


def render_guest_view(data):
    event = data.get("event_details", {})
    
    st.title("You're Invited!")
    
    date_disp = format_date(event.get('date', 'TBD'))
    time_disp = format_time(event.get('time', 'TBD'))
    
    st.markdown(f"""
    <div class="event-card">
        <h2 style="text-align: center; margin: 0 0 0.4rem 0; font-size: 1.3rem; font-family: Cambria, Georgia, serif; color: #1a472a !important; font-weight: 700; line-height: 1.3;">{event.get('title', 'Christmas Carols')}</h2>
        <p style="text-align: center; font-size: 0.85rem; margin: 0 0 0.4rem 0; color: #333 !important;">{event.get('description', '')}</p>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; font-size: 1rem; margin: 0.3rem 0;">
            <span style="font-weight: bold; color: #c41e3a !important;">Date: {date_disp}</span>
            <span style="font-weight: bold; color: #c41e3a !important;">Time: {time_disp}</span>
        </div>
        <p style="text-align: center; font-size: 0.9rem; margin: 0.3rem 0 0 0; font-weight: bold;">Place: {event.get('location', 'TBD')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    instr = event.get('host_instructions', '').strip()
    if instr:
        st.markdown(f"""
        <div class="info-card">
            <h4 style="margin: 0 0 0.2rem 0; font-size: 0.85rem;">Info from Host:</h4>
            <div style="white-space: pre-line; font-size: 0.8rem;">{instr}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="background:#1a472a; color:white; padding:0.4rem; border-radius:8px; text-align:center; margin:0.3rem 0;"><b style="color:white !important; font-size:1rem;">RSVP Here</b></div>', unsafe_allow_html=True)
    
    with st.form("rsvp_form", clear_on_submit=True):
        name = st.text_input("Your Name", placeholder="Enter your name")
        num = st.number_input("Number of Guests (including yourself)", min_value=1, max_value=20, value=1)
        
        if st.form_submit_button("Submit RSVP", use_container_width=True):
            if not name.strip():
                st.error("Please enter your name!")
            else:
                existing = [r for r in data["responses"] if r["name"].lower() == name.strip().lower()]
                resp = {"name": name.strip(), "num_guests": num, "message": "", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                
                if existing:
                    for i, r in enumerate(data["responses"]):
                        if r["name"].lower() == name.strip().lower():
                            data["responses"][i] = resp
                            break
                    save_data(data)
                    st.success(f"Thanks {name}! RSVP updated!")
                else:
                    data["responses"].append(resp)
                    save_data(data)
                    st.success(f"Thanks {name}! See you there!")
                st.balloons()


def render_host_view(data):
    st.title("Host Dashboard")
    
    if not st.session_state.get("host_authenticated", False):
        st.markdown('<p style="color:#1a472a; font-weight:bold; font-size:1.1rem;">Enter Password:</p>', unsafe_allow_html=True)
        password = st.text_input("Password", type="password", key="host_pwd", label_visibility="collapsed")
        if st.button("Login"):
            if password == HOST_PASSWORD:
                st.session_state["host_authenticated"] = True
                st.rerun()
            else:
                st.error("Wrong password!")
        return
    
    url = get_app_url()
    st.markdown(f'<div class="info-card"><b>Share link:</b> <code style="color:#222;">{url}</code></div>', unsafe_allow_html=True)
    
    responses = data.get("responses", [])
    total = get_total_attendees(responses)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="stats-card"><h4>Responses</h4><p>{len(responses)}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stats-card"><h4>Total Guests</h4><p>{total}</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Guest List with DELETE option
    if responses:
        st.markdown('<h4 style="color:#1a472a;">Guest List</h4>', unsafe_allow_html=True)
        
        for i, r in enumerate(sorted(responses, key=lambda x: x.get("timestamp", ""), reverse=True)):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f'<div style="padding:0.3rem;"><b>{r["name"]}</b> - {r["num_guests"]} guest(s)</div>', unsafe_allow_html=True)
            with col2:
                if st.button("Delete", key=f"del_{i}_{r['name']}"):
                    data["responses"] = [x for x in data["responses"] if x["name"] != r["name"]]
                    save_data(data)
                    st.rerun()
        
        st.markdown("---")
        
        import pandas as pd
        df = pd.DataFrame([{"Name": r["name"], "Guests": r["num_guests"]} for r in responses])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button("Download CSV", df.to_csv(index=False), "rsvps.csv")
    else:
        st.info("No RSVPs yet!")
    
    st.markdown("---")
    
    # Edit Event
    if st.checkbox("Edit Event"):
        event = data.get("event_details", {})
        with st.form("settings"):
            title = st.text_input("Title", event.get("title", ""))
            col1, col2 = st.columns(2)
            with col1:
                # Default to today's date if not set or invalid
                try:
                    d = datetime.strptime(event.get("date", ""), "%Y-%m-%d").date()
                except:
                    d = date.today()
                new_date = st.date_input("Date", d)
            with col2:
                try:
                    t = event.get("time", "18:00").split(":")
                    new_time = st.time_input("Time", time(int(t[0]), int(t[1])))
                except:
                    new_time = st.time_input("Time", time(18, 0))
            loc = st.text_input("Location", event.get("location", ""))
            desc = st.text_area("Description", event.get("description", ""), height=50)
            instr = st.text_area("Host Instructions", event.get("host_instructions", ""), height=60)
            
            if st.form_submit_button("Save"):
                data["event_details"] = {
                    "title": title, "date": new_date.strftime("%Y-%m-%d"),
                    "time": new_time.strftime("%H:%M"), "location": loc,
                    "description": desc, "host_instructions": instr
                }
                save_data(data)
                st.success("Saved!")
                st.rerun()
    
    # Clear All RSVPs / Start Fresh
    if st.checkbox("Manage RSVPs"):
        st.warning("Use these options to manage RSVP data:")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear All RSVPs", help="Delete all RSVPs but keep event details"):
                data["responses"] = []
                save_data(data)
                st.success("All RSVPs cleared!")
                st.rerun()
        
        with col2:
            if st.button("Start Fresh Event", help="Clear RSVPs and reset event to defaults"):
                data["responses"] = []
                data["event_details"] = {
                    "title": "Indian Community Church, Santa Clara - Carols",
                    "date": date.today().strftime("%Y-%m-%d"),
                    "time": "18:00",
                    "location": "Indian Community Church, Santa Clara",
                    "description": "Join us in the Christmas Caroling to share the joy of Christmas with our brothers and sisters families!",
                    "host_instructions": ""
                }
                save_data(data)
                st.success("Fresh event created!")
                st.rerun()


def main():
    st.set_page_config(page_title="ICC Carols RSVP", page_icon="*", layout="centered", initial_sidebar_state="collapsed")
    
    apply_theme()
    data = load_data()
    
    if "mode" not in st.session_state:
        st.session_state.mode = "Guest RSVP"
    
    if st.session_state.mode == "Guest RSVP":
        render_guest_view(data)
    else:
        render_host_view(data)
    
    st.markdown("---")
    st.markdown('<div class="bottom-toggle"><b>Switch View:</b></div>', unsafe_allow_html=True)
    mode = st.radio("", ["Guest RSVP", "Host Login"], horizontal=True, label_visibility="collapsed", 
                    index=0 if st.session_state.mode == "Guest RSVP" else 1)
    
    if mode != st.session_state.mode:
        st.session_state.mode = mode
        st.rerun()


if __name__ == "__main__":
    main()
