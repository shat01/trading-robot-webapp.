# 📈 Trading Robot Web App

This web app is a **Flask-based trading assistant** that uses basic image processing to analyze uploaded chart screenshots and generate a **BUY or SELL signal**, with an optional user comment and example trade setup (entry, stop loss, take profit).

### ✅ Current Features

- Upload a chart image (JPG or PNG)  
- Detect edges (representing candlesticks) using OpenCV  
- Analyze edge density to estimate market pressure (BUY/SELL)  
- Simulated entry, stop loss, and take profit generation  
- Optional "Buy/Sell Comment" input  
- Results display with signal and trade setup  
- Designed for future pattern detection and indicator extraction  

---

## 🚀 How It Works

1. **Image Upload**  
   You upload a candlestick chart screenshot.

2. **Image Processing**  
   - The image is converted to grayscale.  
   - Edges (candlestick shapes) are detected using OpenCV's `Canny` filter.

3. **Signal Estimation**  
   - The rightmost part of the chart (most recent area) is analyzed.  
   - Based on edge density, the app estimates either a BUY or SELL signal.

4. **Simulated Output**  
   Sample entry, SL, and TP values are generated for demonstration.

5. **User Comment**  
   You can optionally include your trading rationale or notes.
