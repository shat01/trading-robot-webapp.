function analyzeImage() {
    const upload = document.getElementById('upload');
    const result = document.getElementById('result');
    if (!upload.files.length) {
        result.textContent = "Please upload a screenshot first.";
        return;
    }
    const file = upload.files[0];
    const fileName = file.name.toLowerCase();
    if (fileName.includes("bull") || fileName.includes("buy")) {
        result.innerHTML = "<h2>✅ Signal: BUY</h2>";
    } else if (fileName.includes("bear") || fileName.includes("sell")) {
        result.innerHTML = "<h2>❌ Signal: SELL</h2>";
    } else {
        result.innerHTML = "<h2>⚠️ Signal: Not clear - rename your screenshot with keywords like 'buy' or 'sell'.</h2>";
    }
}
