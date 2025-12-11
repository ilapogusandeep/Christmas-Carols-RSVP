# 🎄 Christmas Carols RSVP App

A beautiful, festive invitation and RSVP system for Christmas Carols gatherings - similar to Evite but simpler and self-hosted!

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## ✨ Features

### For Guests
- 🎁 Beautiful Christmas-themed RSVP form
- 📝 Enter name and number of guests attending
- 🍽️ Optional dietary restrictions field
- 💬 Optional message to host
- 🔄 Update your RSVP anytime

### For Hosts
- 🔐 Password-protected dashboard
- 📊 See total responses and headcount
- 📋 View detailed guest list
- 📥 Download guest list as CSV
- 🍽️ Dietary requirements summary
- ⚙️ Edit event details
- 🗑️ Manage RSVPs

## 🚀 Quick Start

### Local Setup

1. **Navigate to the project directory:**
   ```bash
   cd ~/Documents/CarolsScheduler
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   The app will open automatically at `http://localhost:8501`

### Host Password

Default host password: `carols2024`

To change it, edit the `HOST_PASSWORD` variable in `app.py`:
```python
HOST_PASSWORD = "your_new_password"
```

## 🌐 Sharing Your App

### Option 1: Streamlit Cloud (Free & Easy!)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy your app
5. Share the URL with guests!

### Option 2: Local Network Sharing

Run with network access:
```bash
streamlit run app.py --server.address 0.0.0.0
```
Share your local IP address with guests on the same network.

### Option 3: ngrok (Temporary Public URL)

```bash
# Install ngrok
brew install ngrok

# Run your app
streamlit run app.py

# In another terminal, create tunnel
ngrok http 8501
```
Share the ngrok URL with your guests!

## 📁 Project Structure

```
CarolsScheduler/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── data/
    └── rsvps.json     # RSVP data storage (auto-created)
```

## 🎨 Customization

### Event Details

1. Run the app
2. Go to Host Dashboard (use password)
3. Expand "Edit Event Details"
4. Update title, date, time, location, description
5. Save!

### Styling

The app includes a beautiful Christmas theme with:
- Festive green and red color scheme
- Snowfall animation
- Mountains of Christmas font for headings
- Gold accents

To customize colors, edit the `apply_christmas_theme()` function in `app.py`.

## 🎁 Tips for Hosts

1. **Share Early**: Send the link a few days before the event
2. **Track Daily**: Check the dashboard regularly for new RSVPs
3. **Download List**: Export guest list before the event for easy check-in
4. **Dietary Planning**: Use the dietary summary to plan your menu

## 🛠️ Troubleshooting

**App won't start?**
```bash
pip install --upgrade streamlit pandas
```

**Data not saving?**
Ensure the `data/` directory has write permissions.

**Fonts not loading?**
The app uses Google Fonts, so internet connection is required for the full visual experience.

---

Made with ❤️ for the holiday season! 🎄🎵


