# 🎤 Munch Assistant

An amazing animated ASCII art project featuring Ice Spice with rotating text display!

## ✨ Features

- **Animated ASCII Art** - Beautiful portrait with smooth glowing animations
- **Dynamic Text Display** - Rotating text lines with pulse animations
- **Centered Display** - Non-scrollable, always-centered presentation
- **Responsive Design** - Adapts to different screen sizes
- **Gradient Background** - Eye-catching purple gradient backdrop

## 🚀 Quick Start

### Option 1: Open Locally

1. Clone or download this repository
2. Open `index.html` in your web browser
3. Enjoy the show!

### Option 2: Live Server (Recommended for Development)

```bash
# If you have Python installed:
cd munch-assistant
python -m http.server 8000

# Then visit: http://localhost:8000
```

### Option 3: VS Code Live Server

1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 📁 Project Structure

```
munch-assistant/
├── index.html      # Main HTML file
├── styles.css      # Styling and animations
├── script.js       # JavaScript for animations and text rotation
└── README.md       # This file
```

## 🎨 Customization

### Change Text Lines

Edit the `textLines` array in `script.js`:

```javascript
const textLines = [
    "✨ Your custom text here ✨",
    "💎 Add more lines as needed 💎",
    // Add or remove lines as desired
];
```

### Adjust Animation Speed

Modify the intervals at the bottom of `script.js`:

```javascript
setInterval(animateGlow, 50);   // Glow animation speed (milliseconds)
setInterval(updateText, 4000);  // Text change interval (milliseconds)
```

### Change Colors

Edit the gradient and colors in `styles.css`:

```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.ascii-art {
    color: #ffd700; /* Gold color */
}
```

## 🌐 Deployment

### GitHub Pages

1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Select your main branch as the source
4. Your site will be live at `https://yourusername.github.io/munch-assistant/`

### Netlify

1. Drag and drop the project folder to [Netlify Drop](https://app.netlify.com/drop)
2. Get an instant live URL

### Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd munch-assistant
vercel
```

## 💡 Tips

- **ASCII Art**: Replace the ASCII art in `script.js` with your own using tools like [ASCII Art Archive](https://www.asciiart.eu/)
- **Text Content**: Feel free to customize all text lines to match your theme
- **Font Size**: Adjust `.ascii-art` font-size in `styles.css` if the art doesn't fit your screen

## 📝 License

This project is open source and free to use for any purpose.

## 🎵 Credits

ASCII art converted using Image to ASCII Art tools.
Created with ❤️ for Ice Spice fans!

---

**Note**: This project does not contain copyrighted lyrics. All text is original and can be customized by you!
