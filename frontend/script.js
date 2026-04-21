const API_BASE = "https://ai-link-intelligence-tool.onrender.com";

async function analyzeLink() {

    const url = document.getElementById("urlInput").value;

    if (!url) {
        alert("Please enter a URL");
        return;
    }

    document.getElementById("status").innerText = "Analyzing...";

    try {
        const response = await fetch(`${API_BASE}/analyze?url=${encodeURIComponent(url)}`);
        const data = await response.json();

        document.getElementById("status").innerText = "Done ✅";

        document.getElementById("url").innerText = data.url || "-";
        document.getElementById("summary").innerText = data.summary || "-";
        document.getElementById("category").innerText = data.category || "-";
        document.getElementById("safety").innerText = data.url_safety || "-";

    } catch (error) {
        document.getElementById("status").innerText = "❌ Backend Error";
        console.error(error);
    }
}
